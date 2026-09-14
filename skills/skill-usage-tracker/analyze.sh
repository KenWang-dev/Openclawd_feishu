#!/bin/bash
# Skill Usage Tracker - Analyze tool/skill usage from session history

WORKSPACE="${HOME}/.openclaw/workspace"
TRACKER_DIR="${WORKSPACE}/skills/skill-usage-tracker"
LOG_FILE="${TRACKER_DIR}/usage.log"
REPORT_FILE="${TRACKER_DIR}/report.md"
STATS_FILE="${TRACKER_DIR}/stats.json"

mkdir -p "$TRACKER_DIR"

echo "📊 Skill Usage Analysis"
echo "======================"
echo ""

# Get session list to find active sessions
SESSIONS=$(openclaw sessions list --limit 20 --json 2>/dev/null)

if [ -z "$SESSIONS" ] || [ "$SESSIONS" = "[]" ]; then
    # Try direct API call
    SESSIONS='[{"key":"agent:main:main"}]'
fi

echo "🔍 Analyzing session history..."
echo ""

# Initialize counters
declare -A tool_count daily_stats

# Parse sessions and extract tool calls
for session_key in $(echo "$SESSIONS" | jq -r '.[].key' 2>/dev/null); do
    if [ -z "$session_key" ]; then
        session_key="agent:main:main"
    fi
    
    # Get history for this session (limit to last 50 messages to avoid too much data)
    HISTORY=$(openclaw sessions history "$session_key" --limit 50 --json 2>/dev/null)
    
    if [ -n "$HISTORY" ]; then
        # Extract tool names from toolCall entries using jq
        tools=$(echo "$HISTORY" | jq -r '.messages[]?.content[]? | select(.type == "toolCall") | .name' 2>/dev/null)
        
        for tool in $tools; do
            if [ -n "$tool" ]; then
                tool_count["$tool"]=$((tool_count["$tool"] + 1))
            fi
        done
    fi
done

# If we couldn't get from API, try parsing the current session
if [ ${#tool_count[@]} -eq 0 ]; then
    echo "📝 Using current session analysis..."
    
    # Get current session history
    HISTORY=$(openclaw sessions history agent:main:main --limit 100 --json 2>/dev/null)
    
    if [ -n "$HISTORY" ]; then
        tools=$(echo "$HISTORY" | jq -r '.messages[]?.content[]? | select(.type == "toolCall") | .name' 2>/dev/null)
        
        for tool in $tools; do
            if [ -n "$tool" ]; then
                tool_count["$tool"]=$((tool_count["$tool"] + 1))
            fi
        done
    fi
fi

# Also check the main session transcript file
if [ -f "/root/.openclaw/workspace/51ea741d-d02e-4fdc-8c5d-7e05dc7fe7d8.jsonl" ]; then
    echo "📂 Found transcript file, parsing..."
    tools=$(cat /root/.openclaw/workspace/51ea741d-d02e-4fdc-8c5d-7e05dc7fe7d8.jsonl | jq -r '.messages[]?.content[]? | select(.type == "toolCall") | .name' 2>/dev/null)
    
    for tool in $tools; do
        if [ -n "$tool" ]; then
            tool_count["$tool"]=$((tool_count["$tool"] + 1))
        fi
    done
fi

# Generate JSON stats
echo "{" > "$STATS_FILE"
first=true
for tool in "${!tool_count[@]}"; do
    if [ "$first" = true ]; then
        first=false
    else
        echo "," >> "$STATS_FILE"
    fi
    count=${tool_count[$tool]}
    echo -n "\"$tool\": $count" >> "$STATS_FILE"
done
echo "}" >> "$STATS_FILE"

# Generate markdown report
cat > "$REPORT_FILE" << EOF
# 📊 Skill Usage Report

> Generated: $(date '+%Y-%m-%d %H:%M:%S')

## Usage Statistics

| Skill/Tool | Usage Count | Analysis |
|------------|-------------|----------|
EOF

# Sort by count and add to report
for tool in $(echo "${!tool_count[@]}" | tr ' ' '\n' | sort -t$'\t' -k2 -rn); do
    count=${tool_count[$tool]}
    
    # Determine status
    if [ "$count" -gt 20 ]; then
        status="🟢 高频"
    elif [ "$count" -gt 5 ]; then
        status="🟡 中频"
    else
        status="🔴 低频"
    fi
    
    echo "| $tool | $count | $status |" >> "$REPORT_FILE"
done

# Add recommendations
cat >> "$REPORT_FILE" << 'EOF'

## 📋 Recommendations

### 🟢 Keep & Expand (高频使用)
Skills used > 20 times - core capabilities, consider enhancing

### 🟡 Review (中频使用)  
Skills used 5-20 times - useful but not critical

### 🔴 Consider Removing (低频)
Skills used < 5 times - evaluate necessity

EOF

echo ""
echo "📈 Results:"
echo "----------"

if [ ${#tool_count[@]} -eq 0 ]; then
    echo "⚠️ No tool usage data found"
else
    # Print sorted results
    for tool in $(echo "${!tool_count[@]}" | tr ' ' '\n' | sort -k2 -rn); do
        count=${tool_count[$tool]}
        printf "  %-25s %d\n" "$tool:" "$count"
    done
fi

echo ""
echo "📄 Full report: $REPORT_FILE"
echo "📄 Stats JSON: $STATS_FILE"
