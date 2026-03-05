# Memory - Expert_team 项目

## 2025-02-27 递归压缩灾难

**问题**：打包 skill 目录时产生 1.7GB 巨大文件

**根因**：ZIP 打包时没有排除自身文件，导致：
```
expert-skill.skill (ZIP)
└── references/experts/expert-skill.skill  ← 自己包含自己
```

**教训**：
- 打包目录时**必须排除**输出文件本身
- 命令示例：`zip -r output.zip . -x "output.zip"`
- 或者打包到上级目录：`zip -r ../output.zip .`

**已删除文件**（释放 5.1GB）：
- `expert-skill.skill` (项目根)
- `.claude/expert-skill.zip`
- `.claude/skills/expert-skill/references/experts/expert-skill.skill`
