# AI Tutor API 接口设计（AI Tutor API Design）V1.0

> 本文档定义 AI 导师 V1 的 API 接口：用户 / 目标 / 项目 / 任务 / AI 建议 / 对话，以及 AI 请求上下文结构。
> API 连接 Frontend、Backend、Database、AI Model 四层，是模块间通信的规则。
> 面向 AI 应用开发初学者，不使用复杂企业架构。

---

## 1. API 基础概念

### API 是什么

- API（Application Programming Interface）是不同模块之间交流的规则
- 定义：谁可以调用、传什么数据（请求）、返回什么数据（响应）
- 本系统 API 采用 REST 风格，通过 HTTP 传输 JSON 数据

### 为什么软件系统需要 API

- 模块解耦：前端不关心数据如何存储，后端不关心页面如何展示
- 统一入口：所有数据读写与 AI 调用经过 API，行为可控制、可记录
- 分工明确：每层只做自己的事，便于独立开发与调试

### 模块间数据流

```
Frontend（用户界面）
    ↓  HTTP 请求（JSON）
API（接口层）
    ↓
Backend（业务逻辑）
    ├──→ Database（读写数据）
    └──→ AI Model（组织上下文并调用）
    ↓  HTTP 响应（JSON）
Frontend（展示结果）
```

---

## 2. API 设计原则

| 原则 | 说明 |
| --- | --- |
| 简单优先 | V1 不设计复杂企业级接口，一个资源一套基础操作 |
| 单一职责 | 一个接口只负责一个明确任务，不做"万能接口" |
| 服务产品目标 | 所有 API 围绕三件事：用户理解、项目推进、AI 建议 |

---

## 3. 用户相关 API

### 获取用户信息

- **接口**：`GET /api/users/{id}`
- **作用**：获取用户基本信息
- **请求数据**：路径参数 `id`（用户 ID）
- **返回数据**：

```json
{
  "id": "u_001",
  "name": "杏珠",
  "created_time": "2026-08-09T10:00:00Z"
}
```

### 获取用户档案

- **接口**：`GET /api/profile/{user_id}`
- **作用**：获取 AI 理解用户所需的档案
- **返回数据**：

```json
{
  "user_id": "u_001",
  "identity": "AI 应用开发学习者",
  "skills": ["需求表达", "AI 生态了解"],
  "learning_style": ["项目驱动", "边做边学"],
  "preferences": ["实践优先", "简单方案优先", "MVP 思维"]
}
```

---

## 4. 目标相关 API

| 接口 | 作用 | 说明 |
| --- | --- | --- |
| `POST /api/goals` | 创建目标 | 请求含 title / description / start_date / target_date |
| `GET /api/goals` | 获取目标列表 | 返回当前用户全部目标及状态 |
| `PUT /api/goals/{id}` | 更新目标 | 修改描述、日期或状态 |

### 目标如何影响 AI 判断

- AI 建议围绕**当前进行中的目标**生成，而非泛泛而谈
- 目标状态（active / paused / completed）决定 AI 是否围绕它给建议
- 目标变化（修改 / 归档）会触发 AI 重新评估下一步

---

## 5. 项目相关 API

| 接口 | 作用 | 说明 |
| --- | --- | --- |
| `POST /api/projects` | 创建项目 | 请求含 goal_id / name |
| `GET /api/projects/{id}` | 获取项目状态 | 返回 current_stage / progress / status |
| `PUT /api/projects/{id}` | 更新项目状态 | 更新阶段、进度、状态 |

### 项目数据如何帮助 AI 理解当前阶段

- `current_stage`：AI 知道用户做到哪一步，建议下一步该做什么
- `progress`：AI 判断进度是否正常，是否需要提醒
- `status`：项目受阻（blocked）时，AI 优先处理阻塞问题而非新增任务

---

## 6. 任务相关 API

| 接口 | 作用 | 说明 |
| --- | --- | --- |
| `POST /api/tasks` | 创建任务 | 请求含 project_id / title / priority |
| `GET /api/tasks` | 获取任务列表 | 返回待办与进行中任务 |
| `PUT /api/tasks/{id}` | 更新任务状态 | 更新 status、completed_time |

### 任务是 AI 推荐行动的重要依据

- AI 从任务列表中挑选"当前最值得做的一项"作为建议
- 完成任务后更新状态，AI 据此判断项目推进情况
- 任务优先级（high / medium / low）参与 AI 排序判断

---

## 7. AI 核心 API

### 接口

- **接口**：`POST /api/ai/recommend`
- **作用**：请求 AI 生成下一步建议（核心能力）

### 完整流程

```
用户输入
    ↓
Frontend
    ↓
API
    ↓
Backend
    ↓
读取：Profile / Goal / Project / Task / Memory
    ↓
生成 Prompt
    ↓
调用 AI Model
    ↓
保存 AI Recommendation
    ↓
返回结果
```

### 请求示例

```json
{
  "user_id": "u_001",
  "input": "我今天应该做什么？"
}
```

### 返回示例

```json
{
  "recommendation_id": "r_001",
  "recommendation": "完成目标拆解：将 AI 导师 MVP 拆为 3 个阶段",
  "reason": "当前项目处于起步阶段，拆解是生成下一步行动的前提",
  "tasks": [
    {
      "title": "拆分 MVP 阶段并定义各阶段完成标准",
      "priority": "high",
      "completed_standard": "输出 3-5 个阶段，每阶段有明确完成标准"
    }
  ]
}
```

说明：保存的 AI Recommendation 同时写入数据库（见 06 文档），用于后续复盘与反馈循环。

---

## 8. 对话 API

### 接口

- **接口**：`POST /api/chat`
- **作用**：用户与 AI 导师自由对话

### 流程

```
用户消息
    ↓
读取上下文（Profile / Goal / Project / Task / Memory / 近期对话）
    ↓
调用 AI
    ↓
保存 Conversation（user + assistant 两条）
    ↓
返回回复
```

### 请求示例

```json
{
  "user_id": "u_001",
  "message": "我遇到一个报错，卡住了"
}
```

### 返回示例

```json
{
  "reply": "先别急，告诉我报错信息和你正在做哪一步，我来判断这是技术问题还是方向问题。",
  "conversation_id": "c_001"
}
```

与 `POST /api/ai/recommend` 的区别：chat 是开放式对话；recommend 是结构化建议（含推荐任务 / 原因 / 完成标准）。

---

## 9. API 与数据库关系

```
Frontend
    ↓  API
Backend
    ↓  SQL / ORM
Database
```

### API 不负责长期保存数据

- API 只传递请求与响应，数据持久化由 Backend 写入 Database
- API 层不存状态，每次请求独立处理

### 为什么不能让前端直接访问数据库

| 原因 | 说明 |
| --- | --- |
| 安全 | 数据库连接信息不能暴露给浏览器 |
| 控制 | 数据读写需经过校验与业务逻辑，不能任意操作 |
| 统一 | AI 调用、权限校验集中在 Backend，行为一致可追踪 |
| 解耦 | 前端改动不影响数据库，数据库结构调整不影响前端 |

---

## 10. V1 API 范围

### 支持

- 用户管理
- 用户档案
- 目标管理
- 项目管理
- 任务管理
- AI 建议
- AI 聊天

### 暂不支持

- 多用户协作
- 复杂权限系统
- 第三方开放接口
- 企业级功能（批量、审计、限流配额等）

---

## 11. AI Request Context 设计

### 核心说明

- AI 请求不是简单发送用户一句话
- 一次 AI 请求需要携带完整上下文，AI 才能给出针对性建议

### 上下文组成

| 组成 | 内容 | 来源 |
| --- | --- | --- |
| User Profile | 用户身份、技能、偏好 | Profile 表 |
| Goal | 用户目标 | Goal 表 |
| Project State | 项目当前状态 | Project 表 |
| Task List | 当前行动 | Task 表 |
| Recent History | 近期记录 | Conversation / Growth Log |
| Memory | 长期信息 | Memory 表 |
| User Input | 当前问题 | 请求参数 |

### 数据结构示例

```json
{
  "user_id": "u_001",
  "context": {
    "profile": {
      "identity": "AI 应用开发学习者",
      "skills": ["需求表达", "AI 生态了解"],
      "learning_style": ["项目驱动", "边做边学"],
      "preferences": ["实践优先", "简单方案优先", "MVP 思维"]
    },
    "goal": {
      "title": "构建 AI 导师 MVP",
      "status": "active",
      "target_date": "2026-12-31"
    },
    "project_state": {
      "name": "AI Tutor",
      "current_stage": "起步期",
      "progress": 10,
      "status": "active"
    },
    "task_list": [
      {
        "title": "完成 MVP 功能拆解",
        "priority": "high",
        "status": "todo"
      }
    ],
    "recent_history": [
      {
        "type": "growth_log",
        "content": "完成用户场景文档",
        "date": "2026-08-09"
      }
    ],
    "memory": [
      {
        "content": "用户偏好项目驱动学习",
        "category": "preference",
        "importance": 5
      }
    ]
  },
  "user_input": "我今天应该做什么？"
}
```

组装逻辑：Backend 读取数据库 → 按上表组合 → 生成 Prompt → 调用 AI（见第 12 节）。

---

## 12. 数据流完整示例

示例问题："我今天应该做什么？"

```
用户输入（Frontend）
    ↓
POST /api/ai/recommend
    ↓
Backend 读取数据库：
    Profile / Goal / Project / Task / Memory / History
    ↓
组合 AI Request Context（第 11 节结构）
    ↓
生成 Prompt
    ↓
调用 AI Model
    ↓
保存 AI Recommendation + Conversation
    ↓
返回建议（推荐任务 / 原因 / 完成标准）
    ↓
Frontend 展示，用户执行
```

| 环节 | 动作 | 产出 |
| --- | --- | --- |
| 1 | 用户输入问题 | 请求体 |
| 2 | 调用 AI 接口 | API 请求 |
| 3 | 读取用户状态 | Context 数据 |
| 4 | 组合上下文 | Request Context |
| 5 | 生成并调用 | Prompt → AI 结果 |
| 6 | 保存记录 | AI Recommendation / Conversation |
| 7 | 返回建议 | 用户可见结果 |

---

*文档版本：V1.0　|　维护人：杏珠　|　对应文档：05_Tech_Architecture.md（技术架构）、06_Database_Design.md（数据库）*
