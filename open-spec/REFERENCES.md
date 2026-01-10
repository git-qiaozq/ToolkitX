# OpenSpec 参考资料

OpenSpec 是一个轻量级的规范驱动开发框架，让你在编写代码之前先明确需求和设计。

## 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方网站 | https://openspec.dev | OpenSpec 官方主页 |
| GitHub 仓库 | https://github.com/Fission-AI/OpenSpec | 源代码仓库 |
| Discord 社区 | https://discord.gg/YctCnvvshC | 社区讨论和支持 |

## 安装方式

```bash
npm install -g @fission-ai/openspec@latest
```

## 核心特性

### 1. 审查意图，而非仅审查代码

每个 OpenSpec 变更会生成一个规范差异（spec delta），捕获系统需求的变化。这使得：
- 开发者理解如何修改系统以及需要改变什么
- 审查者无需深入代码就能理解变更本身

### 2. 持久化的上下文

规范与代码一起存储在仓库中，按功能模块组织：
- 当代理需要了解功能如何工作时，它读取规范
- 新开发者可以浏览规范库来理解系统
- 上下文不会因聊天会话结束或团队成员离开而消失

### 3. 秒级审查

当描述想要的变更时，OpenSpec 生成审查所需的一切：
- 提案文档
- 分解的实施任务
- 技术设计决策
- 显示需求变化的规范差异

## 支持的工具

OpenSpec 原生支持以下 AI 编程工具：

| 工具 | 支持状态 |
|------|----------|
| Claude Code | 原生支持 |
| Cursor | 原生支持 |
| Codex | 原生支持 |
| GitHub Copilot | 原生支持 |
| OpenCode | 原生支持 |
| Windsurf | 原生支持 |
| Gemini CLI | 原生支持 |
| Cline | 原生支持 |
| RooCode | 原生支持 |
| Amazon Q | 原生支持 |

## 目录结构

典型的 OpenSpec 项目结构：

```
openspec/
├── specs/                    # 规范文件
│   ├── auth-login/
│   │   └── spec.md
│   ├── auth-session/
│   │   └── spec.md
│   └── checkout-cart/
│       └── spec.md
└── changes/                  # 变更提案
    └── add-remember-me/
        ├── proposal.md       # 变更描述
        ├── design.md         # 技术决策
        ├── tasks.md          # 实施任务
        └── specs/            # 规范差异
            └── auth-session/
                └── spec.md
```

## 使用示例

```bash
# 创建变更提案
/openspec:proposal Add remember me checkbox with 30-day sessions
```

OpenSpec 会自动：
1. 搜索现有规范中的认证需求
2. 搜索代码库中的会话处理逻辑
3. 创建提案并分解实施任务

## 核心理念

- **轻量级**：最少的步骤，最少的流程，快速开始构建
- **存量优先**：专注于成熟代码库，而非从零开始
- **规范即代码**：功能需求作为活文档保存，始终知道代码应该做什么

## 常见问题

### OpenSpec 与 AI 工具的计划模式有什么不同？

计划模式适合单个聊天会话。OpenSpec 专注于跨多个会话的计划，或需要与他人分享的计划。

### 可以在现有代码库上使用吗？

可以！规范在构建过程中逐步创建，无需一次性生成所有规范。

### 规范存储在哪里？

存储在代码库中，建议提交到版本控制，提供系统工作方式和构建意图的可见性。

## 即将推出

- **Workspaces**：针对团队协作的功能
  - 大型代码库支持
  - 多仓库规划
  - 自定义和集成
  - 更好的协作体验
