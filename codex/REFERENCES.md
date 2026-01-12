# OpenAI Codex CLI 参考资料

Codex CLI 是 OpenAI 推出的轻量级 AI 编程代理，运行在终端环境中，帮助开发者更高效地编写代码。

## 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方网站 | https://openai.com/codex | Codex 产品主页 |
| GitHub 仓库 | https://github.com/openai/codex | 源代码仓库（56K+ Stars） |
| 官方文档 | https://developers.openai.com/codex | 完整使用文档 |
| CLI 文档 | https://developers.openai.com/codex/cli | CLI 专属文档 |
| IDE 集成 | https://developers.openai.com/codex/ide | VS Code、Cursor、Windsurf 集成 |
| 更新日志 | https://github.com/openai/codex/blob/main/CHANGELOG.md | 版本更新记录 |
| Discussions | https://github.com/openai/codex/discussions | 社区讨论 |

## 安装方式

```bash
# npm 全局安装（推荐）
npm install -g @openai/codex

# Homebrew 安装 (macOS)
brew install --cask codex

# 直接下载二进制文件
# 访问 https://github.com/openai/codex/releases/latest
```

### 平台支持

| 平台 | 架构 | 下载文件 |
|------|------|----------|
| macOS | Apple Silicon (arm64) | `codex-aarch64-apple-darwin.tar.gz` |
| macOS | x86_64 | `codex-x86_64-apple-darwin.tar.gz` |
| Linux | x86_64 | `codex-x86_64-unknown-linux-musl.tar.gz` |
| Linux | arm64 | `codex-aarch64-unknown-linux-musl.tar.gz` |

## 认证方式

### 使用 ChatGPT 账户登录（推荐）

运行 `codex` 后选择 **Sign in with ChatGPT**，支持以下订阅计划：
- ChatGPT Plus
- ChatGPT Pro
- ChatGPT Team
- ChatGPT Edu
- ChatGPT Enterprise

详情：https://help.openai.com/en/articles/11369540-codex-in-chatgpt

### 使用 API Key

需要额外配置，参考：https://developers.openai.com/codex/auth#sign-in-with-an-api-key

## 核心特性

### 1. 终端 AI 编程代理
- 理解代码库上下文
- 自动生成和修改代码
- 执行多步骤编程任务

### 2. 多模型支持
- 默认使用 GPT-5
- 支持 OpenAI 最新的编程模型 `codex-1`

### 3. IDE 集成
支持主流代码编辑器：
- VS Code
- Cursor
- Windsurf

### 4. 实时协作
- 在代码中实时协作
- 端到端委托任务
- 与团队工程流程集成

## 产品矩阵

| 产品 | 说明 | 链接 |
|------|------|------|
| Codex CLI | 终端 AI 编程代理 | `npm i -g @openai/codex` |
| Codex Web | 云端编程代理 | https://chatgpt.com/codex |
| Codex IDE | 编辑器集成 | https://developers.openai.com/codex/ide |

## 项目结构

```
codex/
├── codex-cli/          # CLI 实现（TypeScript）
├── codex-rs/           # Rust 实现
├── sdk/typescript/     # TypeScript SDK
├── shell-tool-mcp/     # MCP Shell 工具
├── docs/               # 文档
└── scripts/            # 构建脚本
```

## 技术栈

- **主要语言**：Rust (97.4%)
- **构建系统**：Bazel
- **包管理**：pnpm
- **许可证**：Apache-2.0

## 相关资源

### 开发者资源

| 资源 | 链接 |
|------|------|
| OpenAI 开发者门户 | https://developers.openai.com |
| API 文档 | https://platform.openai.com/docs |
| MCP 注册表 | https://github.com/mcp |

### 社区资源

| 平台 | 链接 |
|------|------|
| GitHub Issues | https://github.com/openai/codex/issues |
| GitHub Discussions | https://github.com/openai/codex/discussions |

## 与其他 AI CLI 工具对比

| 工具 | 厂商 | 开源 | 主要特点 |
|------|------|------|----------|
| Codex CLI | OpenAI | ✅ | GPT-5 驱动，与 ChatGPT 订阅集成 |
| Claude Code | Anthropic | ❌ | Claude 驱动，专注代码理解 |
| Gemini CLI | Google | ✅ | Gemini 驱动，多模态支持 |
| OpenCode | Anomaly | ✅ | 多模型支持，75+ 提供商 |

## 最近更新

| 版本 | 日期 | 主要更新 |
|------|------|----------|
| 0.80.0 | 2026-01-09 | 最新稳定版本 |

详细更新日志：https://github.com/openai/codex/blob/main/CHANGELOG.md

## 贡献指南

- 贡献文档：https://github.com/openai/codex/blob/main/docs/contributing.md
- 安装和构建：https://github.com/openai/codex/blob/main/docs/install.md
- 开源基金：https://github.com/openai/codex/blob/main/docs/open-source-fund.md
