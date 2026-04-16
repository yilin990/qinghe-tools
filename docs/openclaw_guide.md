# OpenClaw 完全指南

> 基于官方文档研究的清禾学习笔记

## 什么是 OpenClaw

OpenClaw 是一个AI Agent运行时平台，核心是 **Gateway守护进程**，通过WebSocket连接所有客户端（CLI、Web UI、手机节点等）。

```
用户 → 渠道(Telegram/飞书/Discord) → Gateway → Agent → 工具 → 记忆
```

## 核心架构

### 1. Gateway（网关）
- 单进程守护进程
- 所有渠道+Agent+记忆+调度由它管
- WebSocket协议连接所有客户端
- 设备配对+认证机制

### 2. Agent（智能体）
- 单个运行 + 多Agent路由（isolated sessions）
- 每个Agent有独立workspace、agentDir、记忆、skills
- per-agent模型配置、thinking level、skills白名单
- ACP协议支持（可接Codex等外部Agent）
- 分身spawn机制（sessions_spawn）

### 3. 工具层
- exec（shell执行）
- browser（Playwright浏览器）
- MCP工具调用（接外部工具）
- 文件操作（read/write/edit）
- elevated权限（sudo执行）

### 4. 记忆层
- SQLite + 向量搜索（内置）
- 支持Ollama本地向量
- 自动索引MEMORY.md和memory/*.md
- 关键词+FTS5+语义混合检索

### 5. 自动化层
- **Cron定时任务**：内置调度器，持久化到jobs.json
- **Standing Orders**：自主执行规则，不用每次确认
- **Webhooks**：外部触发
- **TaskFlow**：多步骤工作流编排
- 循环检测+熔断机制

### 6. 渠道层
- 30+渠道内置支持
- Discord/iMessage/Signal/Slack/Telegram/WhatsApp/飞书等
- 插件化设计，可扩展

### 7. 模型层
- 35+模型提供商支持
- 支持自定义provider（OpenAI兼容格式）
- 多模型fallback配置
- 本地模型支持（Ollama/vLLM）

### 8. 技能系统
- ClawHub市场（clawhub.ai）
- AgentSkills兼容格式
- per-agent技能白名单

## 多Agent配置

```json5
{
  agents: {
    list: [
      { id: "main", default: true, workspace: "~/.openclaw/workspace" },
      { id: "image", skills: ["..."], model: "..." },
      { id: "xhs", skills: ["..."], model: "..." },
    ]
  },
  bindings: [
    { agentId: "image", match: { channel: "feishu" } },
  ]
}
```

## Cron定时任务

```bash
# 添加定时任务
openclaw cron add \
  --name "日报" \
  --cron "0 9 * * *" \
  --session main \
  --system-event "生成日报" \
  --delete-after-run

# 查看任务
openclaw cron list

# 查看运行历史
openclaw cron runs <job-id>
```

## Standing Orders（自主规则）

放在AGENTS.md中，定义永久操作授权：

```markdown
## 程序：每周状态报告

**权限：** 收集数据、生成报告、发送给利益相关方
**触发：** 每周五下午4点（通过cron执行）
**审批门：** 无（标准报告）
**升级：** 数据源不可用或指标异常（>2σ）时停止并上报
```

## 记忆配置

```json5
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "ollama",
        model: "llava:latest",
      }
    }
  }
}
```

## 工具权限

```json5
{
  tools: {
    allow: ["exec", "browser", "read", "write"],
    deny: ["canvas"],
    elevated: {
      enabled: true,
      allowFrom: { feishu: ["ou_xxx"] }
    }
  }
}
```

## 浏览器配置

```json5
{
  browser: {
    enabled: true,
    evaluateEnabled: true,
    attachOnly: false  // 设为true需手动开Chrome调试端口
  }
}
```

## 清禾的感悟

OpenClaw本身就是一个完整的AI Agent操作系统。以下能力已经有了：
- ✅ 多Agent分身系统
- ✅ 定时任务调度
- ✅ 自主规则执行
- ✅ 记忆持久化
- ✅ 浏览器自动化

清禾要做的不是重复造轮子，是把这些能力配置好、用起来。

## 参考

- 官方文档：`~/.nvm/versions/node/v24.13.1/lib/node_modules/openclaw/docs/`
- ClawHub市场：https://clawhub.ai
