# ToolkitX

AI 工具集聚合仓库，集中管理各种 AI 编程工具、技能和相关资源。

## 项目简介

本仓库用于存放各种 AI 工具集，采用统一的管理方式：

- **GitHub 官方仓库**：通过 Git Submodules 方式管理，保持与上游同步
- **自定义内容**：在主仓库中直接跟踪，便于版本控制和分享

## 目录结构

```
ToolkitX/
├── claude-code/                    # Claude Code 相关工具
│   ├── skills/
│   │   ├── hub/                    # 自定义技能（主仓库跟踪）
│   │   │   ├── maven-converter/    # Java 项目转 Maven 结构
│   │   │   └── skill-creator/      # 技能创建指南
│   │   └── repos/                  # 官方技能仓库（submodules）
│   │       ├── skills/             # Anthropic 官方技能
│   │       └── awesome-claude-skills/  # 社区精选技能
│   └── utils/                      # 工具类（submodules）
│       ├── claude-code-image-paste-wsl/  # WSL 图片粘贴工具
│       └── claude-image-paste/     # 图片粘贴工具
├── cursor/                         # Cursor 编辑器工具
├── open-code/                      # OpenCode 工具
└── open-spec/                      # 规范驱动开发 OpenSpec
```

## Submodules 列表

| 子模块 | 说明 | 仓库地址 |
|--------|------|----------|
| skills | Anthropic 官方技能集 | https://github.com/anthropics/skills |
| awesome-claude-skills | 社区精选技能集合 | https://github.com/BehiSecc/awesome-claude-skills |
| claude-code-image-paste-wsl | WSL 环境下的图片粘贴工具 | https://github.com/git-qiaozq/claude-code-image-paste-wsl |
| claude-image-paste | Claude Code 图片粘贴工具 | https://github.com/aggroot/claude-image-paste |

## 自定义 Skills

位于 `claude-code/skills/hub/` 目录，可直接拷贝到任意平台的 skills 目录中使用。

| 技能 | 说明 |
|------|------|
| maven-converter | 将 Java 项目转换为标准 Maven 结构，自动重组目录、转换包名并生成 pom.xml |
| skill-creator | 创建 Claude Code 技能的完整指南，包含最佳实践和工具脚本 |

## 快速开始

### 克隆仓库（包含所有子模块）

```bash
git clone --recurse-submodules https://github.com/your-username/ToolkitX.git
```

或者先克隆再初始化子模块：

```bash
git clone https://github.com/your-username/ToolkitX.git
cd ToolkitX
git submodule update --init --recursive
```

### 更新所有子模块

```bash
git submodule update --remote --merge
```

### 使用 Skills

将 `claude-code/skills/hub/` 中的技能文件夹拷贝到 Claude Code 的 skills 目录：

```bash
# 查看可用技能
ls claude-code/skills/hub/

# 拷贝技能到 Claude Code（示例）
cp -r claude-code/skills/hub/maven-converter ~/.claude/skills/
```

## 工具分类

### Claude Code

Claude Code 是 Anthropic 推出的 AI 编程助手，本仓库收集了：

- **官方技能**：来自 Anthropic 的标准技能集
- **社区技能**：经过筛选的优质社区贡献
- **自定义技能**：针对特定场景开发的技能
- **辅助工具**：提升 Claude Code 使用体验的工具

### Cursor

Cursor 是基于 VS Code 的 AI 编程编辑器，此目录用于存放相关工具和配置。

### OpenCode

OpenCode 是开源的 AI 编程工具，此目录用于存放相关资源。

### OpenSpec

OpenSpec 是规范驱动开发工具，此目录用于存放相关规范和模板。

## 贡献指南

欢迎提交 Issue 和 Pull Request！

### 添加新的自定义技能

1. 在 `claude-code/skills/hub/` 下创建新的技能目录
2. 按照 skill-creator 的指南编写 SKILL.md
3. 提交 PR

### 建议新的 Submodule

如果发现优质的开源项目，可以通过 Issue 提出添加建议。

## 许可证

本仓库中的自定义内容采用 MIT 许可证。各子模块遵循其原始许可证。
