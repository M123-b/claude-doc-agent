# 🤖 Claude 智能文档助手 Agent

一个基于 Claude API 构建的智能文档处理 Agent，能够自动总结文档、提取关键信息、生成结构化报告。

**A smart document processing Agent built with Claude API — auto-summarize, extract key points, and generate structured reports.**

---

## ✨ 功能特性 / Features

- 📄 **文档自动摘要** — 一键生成文档核心摘要
- 🔍 **关键信息提取** — 自动识别并列出文档要点
- 📊 **结构化报告生成** — 输出专业格式的分析报告
- 🔄 **多任务 Agent 调度** — 支持按需切换处理模式

---

## 🧠 核心逻辑 / Core Logic

```
用户输入文档
      ↓
Agent 判断任务类型（summarize / extract / report）
      ↓
调用 Claude API 执行对应 Prompt
      ↓
结构化输出结果
```

- 基于 Claude `claude-opus-4-5` 模型
- 支持长文档处理（最大 2048 tokens 输出）
- 中英文文档均可处理

---

## 🚀 快速开始 / Quick Start

### 1. 安装依赖

```bash
pip install anthropic
```

### 2. 设置 API Key

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

### 3. 运行 Agent

```bash
python agent.py
```

---

## 📖 使用示例 / Usage Example

```python
from agent import run_agent

document = "你的文档内容..."

# 生成摘要
run_agent(document, task="summarize")

# 提取关键要点
run_agent(document, task="extract")

# 生成完整报告
run_agent(document, task="report")
```

---

## 🛠 技术栈 / Tech Stack

| 技术 | 用途 |
|------|------|
| Python 3.8+ | 主语言 |
| Anthropic Claude API | 核心 AI 能力 |
| claude-opus-4-5 | 推理模型 |

---

## 📁 项目结构 / Project Structure

```
claude-doc-agent/
├── agent.py        # 主 Agent 逻辑
├── requirements.txt
└── README.md
```

---

## 📋 依赖 / Requirements

```
anthropic>=0.20.0
```

---

## 📄 License

MIT License

---

> Built with ❤️ using [Claude API](https://www.anthropic.com) by M123-b
