# AGENTS.md - AI 编程代理指南

本文档为 AI 编程代理（Claude Code、OpenCode、Cursor 等）提供操作指南。

## 项目概述

ToolkitX 是一个 AI 工具集聚合仓库，采用 Git Submodules 管理外部项目，主仓库直接跟踪自定义内容。

### 目录结构

```
ToolkitX/
├── claude-code/          # Claude Code 相关工具
│   ├── skills/hub/       # 自定义技能（可修改）
│   ├── skills/repos/     # 官方技能仓库（submodules，只读）
│   └── utils/            # 工具类（submodules，只读）
├── cursor/               # Cursor 编辑器工具
├── open-code/            # OpenCode 工具
└── open-spec/            # OpenSpec 规范驱动开发
```

**重要**：`repos/` 和 `utils/` 下的子模块为只读，不要直接修改。

---

## 构建和测试命令

### Python 脚本

此仓库主要包含 Python 脚本，无需构建步骤。

```bash
# 直接运行脚本
python3 claude-code/skills/hub/maven-converter/scripts/maven_converter.py --help

# 运行技能初始化脚本
python3 claude-code/skills/hub/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir>

# 运行技能打包脚本
python3 claude-code/skills/hub/skill-creator/scripts/package_skill.py <path/to/skill>

# 运行技能验证脚本
python3 claude-code/skills/hub/skill-creator/scripts/quick_validate.py <path/to/skill>
```

### 测试单个脚本

```bash
# 预演模式（不修改任何文件）
python3 scripts/maven_converter.py /path/to/project --dry-run

# 测试技能初始化（在临时目录）
python3 scripts/init_skill.py test-skill --path /tmp
```

### Git Submodules

```bash
# 初始化所有子模块
git submodule update --init --recursive

# 更新所有子模块到最新版本
git submodule update --remote --merge

# 查看子模块状态
git submodule status
```

---

## 代码风格指南

### Python 代码规范

#### 导入顺序

```python
# 1. 标准库
import os
import sys
from pathlib import Path
from typing import List, Dict

# 2. 第三方库
import requests

# 3. 本地模块
from .utils import helper
```

#### 命名规范

| 类型 | 规范 | 示例 |
|------|------|------|
| 文件名 | snake_case | `maven_converter.py` |
| 类名 | PascalCase | `MavenConverter` |
| 函数/方法 | snake_case | `find_java_files()` |
| 常量 | UPPER_SNAKE | `SKILL_TEMPLATE` |
| 变量 | snake_case | `project_path` |

#### 类型注解

始终为函数参数和返回值添加类型注解：

```python
def find_java_files(self) -> List[Path]:
    """查找项目中的所有 Java 文件"""
    ...

def determine_maven_path(
    self, 
    file_path: Path, 
    package: str, 
    is_test: bool
) -> Path:
    ...
```

#### 文档字符串

使用中文编写文档字符串，简洁明了：

```python
def convert_package_name(self, package: str) -> str:
    """将包名从 'test' 转换为 'example'"""
    ...
```

#### 错误处理

```python
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
except Exception as e:
    self.log(f"警告：无法读取 {file_path}: {e}")
    return ""  # 返回合理的默认值
```

### Markdown 文档规范

#### SKILL.md 结构

```markdown
---
name: skill-name
description: 完整描述技能功能和触发条件
---

# 技能标题

## 概述
[1-2 句话说明功能]

## 主要内容
[根据技能类型组织：工作流程/任务/参考]

## 资源
- scripts/：可执行脚本
- references/：参考文档
- assets/：模板和资源文件
```

#### YAML 前置内容

- `name`：小写，连字符分隔，最多 40 字符
- `description`：包含功能说明和触发条件

---

## 文件组织约定

### 技能目录结构

```
skill-name/
├── SKILL.md          # 必需：主入口文件
├── scripts/          # 可选：可执行脚本
├── references/       # 可选：参考文档（按需加载）
└── assets/           # 可选：模板和资源文件
```

### 不应包含的文件

- README.md（技能内）
- INSTALLATION_GUIDE.md
- CHANGELOG.md（技能内）
- 其他辅助文档

---

## Git 提交规范

### 提交信息格式

```
[类型] 简短描述

详细说明（可选）
```

### 提交类型

| 类型 | 说明 |
|------|------|
| 添加 | 新增功能、文件或特性 |
| 修复 | 修复 bug 或问题 |
| 重构 | 代码结构调整，不改变功能 |
| 优化 | 性能改进或代码优化 |
| 更新 | 更新依赖、文档、配置等 |
| 删除 | 移除代码、文件或功能 |
| 测试 | 添加或修改测试 |
| 文档 | 仅文档更改 |

### 示例

```
添加 maven-converter 技能的 dry-run 模式支持
修复 init_skill.py 路径处理的空指针异常
更新 README 文档和使用说明
```

---

## 编码最佳实践

### 脚本编写

1. **使用 shebang**：`#!/usr/bin/env python3`
2. **支持 --dry-run**：预览更改而不执行
3. **UTF-8 编码**：文件读写始终指定编码
4. **路径处理**：使用 `pathlib.Path`
5. **日志输出**：清晰的中文提示信息

### 错误处理原则

1. 捕获具体异常，避免空的 `except:`
2. 提供有意义的错误信息
3. 失败时返回合理的默认值或优雅退出
4. 使用 `sys.exit(1)` 表示失败

### 文件编码

- 所有文本文件使用 UTF-8 编码
- Python 文件读写显式指定 `encoding='utf-8'`

---

## 常见任务指南

### 创建新技能

```bash
# 1. 初始化技能目录
python3 claude-code/skills/hub/skill-creator/scripts/init_skill.py my-skill --path claude-code/skills/hub

# 2. 编辑 SKILL.md，完成待办事项

# 3. 添加脚本、参考文档或资源（按需）

# 4. 验证技能
python3 claude-code/skills/hub/skill-creator/scripts/quick_validate.py claude-code/skills/hub/my-skill

# 5. 打包技能
python3 claude-code/skills/hub/skill-creator/scripts/package_skill.py claude-code/skills/hub/my-skill
```

### 修改现有技能

1. 只修改 `skills/hub/` 下的自定义技能
2. 不要修改 `skills/repos/` 下的官方技能（子模块）
3. 测试所有脚本更改后再提交

### 添加新的参考资源

在对应目录的 `REFERENCES.md` 中添加：
- cursor/REFERENCES.md
- open-code/REFERENCES.md
- open-spec/REFERENCES.md

---

## 注意事项

### Submodules 处理

- 子模块变更需要分开提交
- 更新子模块：`git submodule update --remote`
- 不要在主仓库提交子模块内的修改

### 语言偏好

- 所有文档、注释、提交信息使用中文
- 技术术语（API、GitHub 等）保留英文
- 代码变量名使用英文

### 安全考虑

- 不要提交敏感信息（API 密钥、凭据）
- 检查 `.gitignore` 是否正确配置
- 脚本中不要硬编码路径

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Claude Code Skills 官方文档 | https://support.claude.com/en/articles/12512176-what-are-skills |
| Agent Skills 规范 | https://agentskills.io |
| OpenCode 文档 | https://opencode.ai/docs |
| Cursor 文档 | https://cursor.com/docs |
| OpenSpec 官网 | https://openspec.dev |
