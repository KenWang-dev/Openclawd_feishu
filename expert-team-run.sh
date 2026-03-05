#!/bin/bash

# ========================================
# Expert Team Automation v1.0
# 采购专家团智能讨论系统
# ========================================

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
LOG_DIR="/root/.openclaw/workspace/expert-team-logs"
PROMPTS_DIR="/root/.openclaw/workspace/skills/expert_team/prompts"

# 获取日期
DATE=$(date +%Y-%m-%d)
MONTH=$(date +%Y-%m)

# 创建目录
mkdir -p "$LOG_DIR/$MONTH"

# 清理问题标题，生成安全文件名
clean_filename() {
    echo "$1" | sed 's/[^a-zA-Z0-9_]/_/g' | cut -c1-40
}

# 打印分隔线
print_separator() {
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# 主函数
main() {
    if [ -z "$1" ]; then
        echo -e "${RED}用法: $0 \"你的问题\"${NC}"
        echo ""
        echo "示例:"
        echo "  $0 \"供应商涨价30%怎么处理\""
        exit 1
    fi

    QUESTION="$1"
    FILENAME=$(clean_filename "$QUESTION")
    LOG_FILE="$LOG_DIR/$MONTH/${DATE}-${FILENAME}.md"

    print_separator
    echo -e "${BLUE}🎯 Expert Team 专家团系统${NC}"
    print_separator
    echo ""
    echo -e "问题: ${YELLOW}$QUESTION${NC}"
    echo ""
    echo -e "日志: ${GREEN}$LOG_FILE${NC}"
    echo ""

    # 创建讨论文档
    cat > "$LOG_FILE" << EOF
# 专家团讨论记录

> **问题**: $QUESTION
> **日期**: $DATE
> **状态**: 进行中

---

## 📋 问题分析

### 复杂度判定
[待判定]

### 涉及领域
[待填写]

---

## 👥 专家组

| 专家 | 角色 | 状态 |
|------|------|------|
| | | 待邀请 |

---

## 💬 讨论过程

### 专家A
[讨论中...]

### 专家B
[讨论中...]

---

## ✅ 结论

[待汇总]

---

## 📎 行动项

- [ ]

---

*由 Expert Team 系统自动生成*
EOF

    echo -e "${GREEN}✅ 讨论文档已创建${NC}"
    echo ""
    echo "下一步：编辑文档，开始专家讨论"
    echo "命令: vim $LOG_FILE"
}

# 运行主函数
main "$@"
