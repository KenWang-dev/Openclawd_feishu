#!/usr/bin/env python3
"""
A股深度分析工具 - 基于新浪财经 API（服务器稳定可用）
支持：实时行情、K线、技术指标（MA/RSI/MACD/布林带）、量价分析
数据源：新浪财经（money.finance.sina.com.cn）
"""

import argparse
import sys
import json
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)
pd.set_option('display.unicode.east_asian_width', True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://finance.sina.com.cn'
}


def get_market_prefix(symbol: str) -> str:
    """股票代码转市场前缀"""
    if symbol.startswith("6"):
        return "sh"
    elif symbol.startswith("0") or symbol.startswith("3"):
        return "sz"
    elif symbol.startswith("8") or symbol.startswith("4"):
        return "bj"
    return "sh"


def fetch_realtime(symbol: str):
    """实时行情（腾讯财经 qt.gtimg.cn）"""
    prefix = get_market_prefix(symbol)
    code = f"v_{prefix}{symbol}"
    url = f"http://qt.gtimg.cn/q={prefix}{symbol}"
    headers = {'User-Agent': 'Mozilla/5.0', 'Referer': 'https://gu.qq.com'}
    r = requests.get(url, headers=headers, timeout=10)
    r.encoding = 'gbk'
    text = r.text.strip()
    if '~' not in text or '""' in text:
        return None
    # 解析: v_sh600519="1~名称~代码~当前~昨收~开盘~成交量(手)~外盘~内盘~..."
    data = text.split('"')[1].split('~')
    if len(data) < 46:
        return None
    cur = float(data[3])
    pre_close = float(data[4])
    open_price = float(data[5])
    high = float(data[33])
    low = float(data[34])
    vol = int(data[6])
    amount = float(data[37])  # 成交额（万）
    return {
        '名称': data[1],
        '当前': cur,
        '昨收': pre_close,
        '开盘': open_price,
        '最高': high,
        '最低': low,
        '成交量(手)': vol,
        '成交额(万)': round(amount, 2),
        '涨跌额': round(cur - pre_close, 2),
        '涨跌幅': round((cur - pre_close) / pre_close * 100, 2),
    }


def fetch_kline(symbol: str, days: int = 30):
    """K线数据（新浪） scale=240为日K, scale=1200为周K"""
    prefix = get_market_prefix(symbol)
    url = f"https://money.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_MarketData.getKLineData"
    params = {
        'symbol': f'{prefix}{symbol}',
        'scale': 240,       # 日K
        'ma': 'no',
        'datalen': days + 60  # 多取用于MA计算
    }
    r = requests.get(url, headers=HEADERS, params=params, timeout=10)
    data = json.loads(r.text)
    if not data:
        return pd.DataFrame()
    
    df = pd.DataFrame(data)
    df['日期'] = pd.to_datetime(df['day'])
    df = df.sort_values('日期').reset_index(drop=True)
    # 转数值
    for col in ['open', 'high', 'low', 'close', 'volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def quote(symbol: str):
    """显示实时行情"""
    try:
        data = fetch_realtime(symbol)
        if data is None:
            print("  ⚠️ 当前非交易时段或代码无效")
            return
        print(f"  {data['名称']}（{symbol}）")
        print(f"  当前: {data['当前']}  |  涨跌幅: {data['涨跌幅']:+.2f}%")
        print(f"  开盘: {data['开盘']}  |  最高: {data['最高']}  |  最低: {data['最低']}")
        print(f"  昨收: {data['昨收']}  |  涨跌额: {data['涨跌额']:+.2f}")
        print(f"  成交量: {data['成交量(手)']}手  |  成交额: {data['成交额(万)']}万")
    except Exception as e:
        print(f"  ❌ 获取行情失败: {e}")


def kline(symbol: str, days: int = 30):
    """K线数据展示"""
    df = fetch_kline(symbol, days)
    if df.empty:
        print("  ❌ 无K线数据")
        return
    
    show = df.tail(days)
    # 计算涨跌幅
    show = show.copy()
    show['涨跌幅'] = ((show['close'] - show['close'].shift(1)) / show['close'].shift(1) * 100).round(2)
    show['涨跌幅'] = show['涨跌幅'].fillna(0)
    
    print(show[['日期', 'open', 'close', 'high', 'low', 'volume', '涨跌幅']].rename(
        columns={'open': '开盘', 'close': '收盘', 'high': '最高', 'low': '最低', 'volume': '成交量'}
    ).to_string(index=False))
    
    total_chg = show['涨跌幅'].sum()
    print(f"\n  📊 {days}日累计涨跌: {total_chg:+.2f}%")
    print(f"  📊 区间最高: {show['high'].max()}, 最低: {show['low'].min()}")


def tech_indicators(symbol: str, days: int = 60):
    """技术指标（本地计算）"""
    df = fetch_kline(symbol, days + 30)
    if len(df) < 30:
        print("  ❌ 数据不足")
        return
    
    close = df['close']
    
    # MA
    df['MA5'] = close.rolling(5).mean()
    df['MA10'] = close.rolling(10).mean()
    df['MA20'] = close.rolling(20).mean()
    df['MA60'] = close.rolling(60).mean()
    
    # RSI(14)
    delta = close.diff()
    gain = delta.where(delta > 0, 0)
    loss = (-delta).where(delta < 0, 0)
    avg_gain = gain.rolling(14, min_periods=14).mean()
    avg_loss = loss.rolling(14, min_periods=14).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))
    
    # MACD
    ema12 = close.ewm(span=12, adjust=False).mean()
    ema26 = close.ewm(span=26, adjust=False).mean()
    df['DIF'] = ema12 - ema26
    df['DEA'] = df['DIF'].ewm(span=9, adjust=False).mean()
    df['MACD'] = 2 * (df['DIF'] - df['DEA'])
    
    # BOLL
    df['MID'] = close.rolling(20).mean()
    std = close.rolling(20).std()
    df['UPPER'] = df['MID'] + 2 * std
    df['LOWER'] = df['MID'] - 2 * std
    
    latest = df.iloc[-1]
    prev = df.iloc[-2]
    
    print(f"  📈 技术指标（收盘: {latest['close']}，{latest['日期'].strftime('%Y-%m-%d')}）\n")
    
    # MA
    print(f"  ┌─ 均线系统 ─────────────────────────┐")
    for p in [5, 10, 20, 60]:
        v = latest[f'MA{p}']
        if pd.notna(v):
            print(f"  │ MA{p:<2}: {v:>10.2f}                      │")
    ma5, ma10, ma20 = latest['MA5'], latest['MA10'], latest['MA20']
    if pd.notna(ma5) and pd.notna(ma10) and pd.notna(ma20):
        if ma5 > ma10 > ma20:
            print(f"  │ 信号: 🟢 多头排列                     │")
        elif ma5 < ma10 < ma20:
            print(f"  │ 信号: 🔴 空头排列                     │")
        else:
            print(f"  │ 信号: 🟡 交叉/交织                     │")
    print(f"  └────────────────────────────────────┘")
    
    # RSI
    print(f"\n  ┌─ RSI(14) ────────────────────────────┐")
    if pd.notna(latest['RSI']):
        print(f"  │ RSI: {latest['RSI']:>8.2f}                      │")
        if latest['RSI'] > 70:
            print(f"  │ ⚠️  超买区（>70）                      │")
        elif latest['RSI'] < 30:
            print(f"  │ ✅ 超卖区（<30）                      │")
        elif latest['RSI'] > 50:
            print(f"  │ 📊 偏强（>50）                        │")
        else:
            print(f"  │ 📊 偏弱（<50）                        │")
    print(f"  └────────────────────────────────────┘")
    
    # MACD
    print(f"\n  ┌─ MACD ──────────────────────────────┐")
    if pd.notna(latest['DIF']):
        print(f"  │ DIF:  {latest['DIF']:>10.2f}              │")
        print(f"  │ DEA:  {latest['DEA']:>10.2f}              │")
        print(f"  │ MACD: {latest['MACD']:>10.2f}              │")
        if latest['MACD'] > 0:
            print(f"  │ 🟢 红柱（多头动能）                   │")
            if pd.notna(prev['MACD']) and prev['MACD'] <= 0:
                print(f"  │ 🔔 金叉！DIF上穿DEA                  │")
        else:
            print(f"  │ 🔴 绿柱（空头动能）                   │")
            if pd.notna(prev['MACD']) and prev['MACD'] >= 0:
                print(f"  │ ⚠️  死叉！DIF下穿DEA                  │")
    print(f"  └────────────────────────────────────┘")
    
    # BOLL
    print(f"\n  ┌─ 布林带(20,2) ──────────────────────┐")
    if pd.notna(latest['UPPER']):
        print(f"  │ 上轨: {latest['UPPER']:>10.2f}              │")
        print(f"  │ 中轨: {latest['MID']:>10.2f}              │")
        print(f"  │ 下轨: {latest['LOWER']:>10.2f}              │")
        bw = latest['UPPER'] - latest['LOWER']
        if bw > 0:
            pos = (latest['close'] - latest['LOWER']) / bw * 100
            print(f"  │ 位置: {pos:>5.1f}%                       │")
            if pos > 80:
                print(f"  │ ⚠️  接近上轨，短期承压               │")
            elif pos < 20:
                print(f"  │ ✅ 接近下轨，存在支撑                │")
    print(f"  └────────────────────────────────────┘")
    
    # 量价
    print(f"\n  ┌─ 量价分析 ──────────────────────────┐")
    chg = ((latest['close'] - prev['close']) / prev['close'] * 100) if prev['close'] > 0 else 0
    vol_chg = ((latest['volume'] - prev['volume']) / prev['volume'] * 100) if prev['volume'] > 0 else 0
    print(f"  │ 涨跌: {chg:>+7.2f}%  量变: {vol_chg:>+7.1f}%     │")
    if chg > 0 and vol_chg > 20:
        print(f"  │ 📈 放量上涨，动能较强                 │")
    elif chg > 0 and vol_chg < -20:
        print(f"  │ 📊 缩量上涨，追涨需谨慎               │")
    elif chg < 0 and vol_chg > 20:
        print(f"  │ 📉 放量下跌，抛压较重                 │")
    elif chg < 0 and vol_chg < -20:
        print(f"  │ 📊 缩量下跌，抛压减弱                 │")
    else:
        print(f"  │ 📊 量价变化不明显                     │")
    print(f"  └────────────────────────────────────┘")


def fund_flow_proxy(symbol: str, days: int = 10):
    """量价资金流向替代分析"""
    df = fetch_kline(symbol, days + 5)
    if df.empty:
        return
    
    show = df.tail(days).copy()
    show['涨跌幅'] = ((show['close'] - show['close'].shift(1)) / show['close'].shift(1) * 100).round(2)
    show['涨跌幅'] = show['涨跌幅'].fillna(0)
    
    print(show[['日期', 'close', '涨跌幅', 'volume']].rename(
        columns={'close': '收盘', 'volume': '成交量'}
    ).to_string(index=False))
    
    # 量价趋势
    recent5_vol = show['volume'].tail(5).mean()
    early5_vol = show['volume'].head(5).mean() if len(show) >= 8 else recent5_vol
    ratio = recent5_vol / early5_vol - 1 if early5_vol > 0 else 0
    print(f"\n  💡 近5日均量 vs 前5日均量: {ratio:+.1%}")
    if ratio > 0.2:
        print("  📈 近期放量，市场关注度提升")
    elif ratio < -0.2:
        print("  📉 近期缩量，市场参与度下降")


def full_analysis(symbol: str):
    """完整分析报告"""
    print(f"\n{'='*55}")
    print(f"  📊 {symbol} 深度分析报告")
    print(f"  ⏰ {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*55}\n")
    
    print("📌 实时行情")
    quote(symbol)
    
    print(f"\n📈 近30日K线")
    kline(symbol, days=30)
    
    print(f"\n🔬 技术指标")
    tech_indicators(symbol, days=60)
    
    print(f"\n💰 量价资金分析")
    fund_flow_proxy(symbol, days=10)
    
    print(f"\n{'='*55}")
    print(f"  ✅ 报告完成 | 数据源: 新浪财经")
    print(f"{'='*55}")


def main():
    parser = argparse.ArgumentParser(description="A股深度分析工具（新浪财经数据源）")
    parser.add_argument("symbol", help="股票代码（如 600519）")
    parser.add_argument("--kline", action="store_true", help="仅查看K线")
    parser.add_argument("--flow", action="store_true", help="仅查看量价分析")
    parser.add_argument("--tech", action="store_true", help="仅查看技术指标")
    parser.add_argument("--quote", action="store_true", help="仅查看实时行情")
    parser.add_argument("--days", type=int, default=30, help="K线天数（默认30）")
    args = parser.parse_args()
    
    if args.kline:
        kline(args.symbol, days=args.days)
    elif args.flow:
        fund_flow_proxy(args.symbol, days=args.days)
    elif args.tech:
        tech_indicators(args.symbol, days=args.days)
    elif args.quote:
        quote(args.symbol)
    else:
        full_analysis(args.symbol)


if __name__ == "__main__":
    main()
