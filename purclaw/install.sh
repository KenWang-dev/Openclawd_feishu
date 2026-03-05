#!/bin/bash
# purclaw 一键安装脚本
# 适用于 Ubuntu/CentOS/Debian 系统

set -e

echo "========================================"
echo "🚀 purclaw 一键安装脚本"
echo "========================================"
echo ""

# 检测操作系统
if [ -f /etc/os-release ]; then
    . /etc/os-release
    OS=$ID
    VERSION=$VERSION_ID
    echo "检测到操作系统: $OS $VERSION"
else
    echo "⚠️  无法检测操作系统，尝试继续..."
    OS="unknown"
fi

echo ""

# 1. 检查 Node.js
echo "📦 检查 Node.js..."
if command -v node &> /dev/null; then
    NODE_VERSION=$(node -v)
    echo "✅ Node.js 已安装: $NODE_VERSION"

    # 检查版本是否满足要求（>= 18）
    MAJOR_VERSION=$(echo $NODE_VERSION | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$MAJOR_VERSION" -lt 18 ]; then
        echo "⚠️  Node.js 版本过低（需要 >= 18），将升级..."
        INSTALL_NODE=1
    else
        INSTALL_NODE=0
    fi
else
    echo "❌ Node.js 未安装"
    INSTALL_NODE=1
fi

echo ""

# 2. 安装 Node.js（如果需要）
if [ "$INSTALL_NODE" = 1 ]; then
    echo "📦 安装 Node.js 22.x..."

    if [[ "$OS" == "ubuntu" ]] || [[ "$OS" == "debian" ]]; then
        echo "使用 apt 安装..."
        curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
        sudo apt-get install -y nodejs
    elif [[ "$OS" == "centos" ]] || [[ "$OS" == "rhel" ]] || [[ "$OS" == "fedora" ]]; then
        echo "使用 yum 安装..."
        curl -fsSL https://rpm.nodesource.com/setup_22.x | sudo bash -
        sudo yum install -y nodejs
    else
        echo "⚠️  不支持的操作系统，请手动安装 Node.js >= 18"
        echo "   访问: https://nodejs.org/"
        exit 1
    fi

    echo "✅ Node.js 安装完成: $(node -v)"
    echo ""
fi

# 3. 检查脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "📁 purclaw 目录: $SCRIPT_DIR"

# 4. 检查必需文件
echo ""
echo "📋 检查必需文件..."

REQUIRED_FILES=(
    "scripts/fetch-mouser-api.js"
    "scripts/fetch-mouser-monitor.js"
    "scripts/data-store.js"
    "data/components.json"
)

MISSING_FILES=0

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$SCRIPT_DIR/$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file (缺失)"
        MISSING_FILES=$((MISSING_FILES + 1))
    fi
done

if [ $MISSING_FILES -gt 0 ]; then
    echo ""
    echo "❌ 缺少 $MISSING_FILES 个必需文件，请检查"
    exit 1
fi

echo ""

# 5. 创建历史数据目录
echo "📁 创建历史数据目录..."
mkdir -p "$SCRIPT_DIR/data/history"
echo "✅ 目录已创建: $SCRIPT_DIR/data/history"
echo ""

# 6. 检查 API Key
echo "🔑 检查 API Key..."
if grep -q "4fe47ba4-9c76-4e20-9443-08e82f79ad33" "$SCRIPT_DIR/scripts/fetch-mouser-api.js"; then
    echo "⚠️  使用默认 API Key（建议替换为你自己的）"
    echo "   在 scripts/fetch-mouser-api.js 中修改: const API_KEY = 'your-key'"
else
    echo "✅ API Key 已配置"
fi

echo ""

# 7. 运行测试
echo "🧪 运行测试..."
cd "$SCRIPT_DIR"

if node scripts/fetch-mouser-monitor.js; then
    echo ""
    echo "========================================"
    echo "✅ 安装成功！"
    echo "========================================"
    echo ""
    echo "📖 使用说明："
    echo ""
    echo "1. 手动运行："
    echo "   cd $SCRIPT_DIR"
    echo "   node scripts/fetch-mouser-monitor.js"
    echo ""
    echo "2. 使用启动脚本："
    echo "   bash $SCRIPT_DIR/run-monitor.sh"
    echo ""
    echo "3. 配置定时任务（可选）："
    echo "   # 添加到 crontab"
    echo "   0 */4 * * * cd $SCRIPT_DIR && node scripts/fetch-mouser-monitor.js >> /var/log/purclaw.log 2>&1"
    echo ""
    echo "📋 监控物料列表："
    echo "   文件: $SCRIPT_DIR/data/components.json"
    echo ""
    echo "📊 历史数据："
    echo "   目录: $SCRIPT_DIR/data/history/"
    echo ""
    echo "📖 详细文档："
    echo "   $SCRIPT_DIR/MIGRATION.md"
    echo ""
    echo "========================================"
else
    echo ""
    echo "========================================"
    echo "❌ 测试失败"
    echo "========================================"
    echo ""
    echo "请检查："
    echo "1. API Key 是否正确"
    echo "2. 网络连接是否正常"
    echo "3. 查看详细错误信息"
    exit 1
fi
