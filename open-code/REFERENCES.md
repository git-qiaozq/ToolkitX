# OpenCode 参考资料

OpenCode 是一个开源的 AI 编程代理，可在终端、IDE 或桌面环境中帮助你编写代码。

## 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官方网站 | https://opencode.ai | OpenCode 官方主页 |
| GitHub 仓库 | https://github.com/anomalyco/opencode | 源代码仓库（50K+ Stars） |
| 官方文档 | https://opencode.ai/docs | 完整使用文档 |
| 下载页面 | https://opencode.ai/download | 桌面应用下载（macOS、Windows、Linux） |
| Discord 社区 | https://opencode.ai/discord | 社区讨论和支持 |
| X (Twitter) | https://x.com/opencode | 官方社交媒体 |

## 安装方式

```bash
# curl 安装
curl -fsSL https://opencode.ai/install | bash

# npm 安装
npm install -g opencode

# bun 安装
bun install -g opencode

# brew 安装 (macOS)
brew install opencode

# paru 安装 (Arch Linux)
paru -S opencode
```

## 核心特性

- **LSP 支持**：自动为 LLM 加载合适的语言服务器
- **多会话**：在同一项目上并行启动多个代理
- **分享链接**：分享任意会话的链接供参考或调试
- **Claude Pro**：登录 Anthropic 使用 Claude Pro 或 Max 账户
- **多模型支持**：通过 Models.dev 支持 75+ LLM 提供商，包括本地模型
- **多编辑器**：支持终端界面、桌面应用和 IDE 扩展

## 相关服务

| 服务 | 链接 | 说明 |
|------|------|------|
| Zen | https://opencode.ai/zen | 经过优化和基准测试的编程代理模型 |
| Enterprise | https://opencode.ai/enterprise | 企业版服务 |
| Models.dev | https://models.dev | 多模型提供商聚合平台 |

## 隐私说明

OpenCode 不存储任何代码或上下文数据，可在隐私敏感环境中运行。

详情参考：https://opencode.ai/docs/enterprise/

## 更新日志

- 2026-01：桌面应用 Beta 版发布（macOS、Windows、Linux）
