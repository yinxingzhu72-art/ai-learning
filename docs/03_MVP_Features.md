# AI 导师 MVP 功能需求文档（AI Tutor MVP Features）V1.0

> 本文档定义 AI 导师系统 V1（MVP）的功能范围、数据模型与页面结构。
> 系统形态为工作台型 AI 成长伙伴，而非普通聊天机器人。
> 第一阶段用户：杏珠（项目创作者本人）。

---

## 1. 产品定位

### 1.1 AI 导师解决什么问题

- 帮助用户管理目标、推进项目、记录成长
- 通过 AI 分析提供"下一步行动"建议，解决"知道该做什么但不确定下一步做什么"的问题
- 形成目标 → 行动 → 反馈 → 成长的闭环，避免学习与项目推进陷入停滞

### 1.2 与普通聊天机器人的区别

| 维度 | 普通聊天机器人 | AI 导师 |
| --- | --- | --- |
| 交互模式 | 问题 → 答案 | 问题 → 分析 → 判断 → 行动 |
| 上下文 | 单次对话 | 用户档案 + 项目状态 + 历史记录 |
| 输出 | 信息 | 建议 + 可执行行动 |
| 记忆 | 无跨会话记忆 | 持续记录成长并更新理解 |
| 目标 | 完成一次问答 | 推动用户长期成长 |

### 1.3 V1 的核心价值

- 跑通"用户目标创建 → AI 理解用户状态 → 项目拆解 → 生成下一步行动 → 用户执行 → 记录成长 → AI 更新理解"的核心闭环
- 用最小功能集验证：AI 导师能否持续提供有价值的行动建议
- 为后续迭代（复盘、长期分析）积累真实使用数据

---

## 2. MVP 功能范围

### P0 必须功能

#### User Profile 用户档案模块

- **作用**：让 AI 理解用户是谁
- **数据**：
  - 用户身份
  - 当前阶段
  - 长期目标
  - 技能水平
  - 学习方式
  - 决策偏好
- **功能**：查看 / 编辑档案；档案作为 AI 对话的固定上下文

#### Goal Management 目标管理模块

- **作用**：管理用户想完成什么
- **功能**：
  - 创建目标
  - 修改目标
  - 查看目标状态
  - AI 分析目标（明确目标、分析价值、定义用户、确定 MVP 范围）

#### Project State 项目状态模块

- **作用**：记录目标当前进展
- **数据**：
  - 当前阶段
  - 完成内容
  - 当前任务
  - 项目进度
- **功能**：查看与更新项目状态；状态变化后触发 AI 重新评估下一步

#### AI Mentor Chat 智能导师对话模块

- **作用**：核心交互入口
- **区别**：
  - 普通聊天：问题 → 答案
  - AI 导师：问题 → 分析 → 判断 → 行动
- **要求**：对话必须结合用户档案、项目状态、历史记录生成回答，而非孤立应答

#### Next Action 下一步行动模块

- **作用**：核心能力。回答"现在最值得做什么？"
- **输出**：
  - 推荐任务
  - 推荐原因
  - 完成标准
- **要求**：建议不超过 3 项，每项含时长与完成标准

### P1 重要功能

#### Growth Log 成长记录模块

- **作用**：沉淀成长数据，反哺 AI 理解
- **记录**：
  - 完成事项
  - 学习内容
  - 遇到问题
  - 阶段总结

#### 周期复盘模块

- **作用**：周期性回顾，确认成长、校准方向
- **支持**：
  - 每日总结
  - 每周复盘
  - 阶段成长分析

### P2 后续功能（暂不开发）

- 自动联网搜索
- 自动课程推荐
- 多 Agent 系统
- 知识图谱
- 社区功能

> 说明：P2 功能在 V1 明确不做，仅记录方向，避免范围蔓延。

---

## 3. 数据模型设计

> V1 逻辑数据结构。字段为逻辑字段，实际存储层可自由映射。

### User

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 用户唯一标识 |
| name | string | 用户名称 |
| created_time | datetime | 创建时间 |

### Profile 用户档案

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| user_id | string | 关联 User.id（1:1） |
| identity | string | 用户身份 / 定位 |
| skills | list | 技能水平（含已具备 / 待提升） |
| learning_style | list | 学习方式 |
| preferences | list | 决策偏好 |
| long_term_goal | string | 长期目标 |

### Goal

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 目标唯一标识 |
| user_id | string | 关联 User.id |
| title | string | 目标标题 |
| description | string | 目标描述（含成功标准） |
| start_date | date | 开始日期 |
| target_date | date | 目标日期 |
| status | enum | 状态：active / paused / completed / archived |

### Project

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 项目唯一标识 |
| goal_id | string | 关联 Goal.id |
| name | string | 项目名称 |
| current_stage | string | 当前阶段 |
| progress | number | 进度（0-100） |
| status | enum | 状态：active / blocked / done / archived |

### Task

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 任务唯一标识 |
| project_id | string | 关联 Project.id |
| title | string | 任务标题 |
| priority | enum | 优先级：high / medium / low |
| status | enum | 状态：todo / doing / done / cancelled |
| created_time | datetime | 创建时间 |
| completed_time | datetime | 完成时间（可空） |

### Conversation

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 会话唯一标识 |
| user_id | string | 关联 User.id |
| message | string | 消息内容 |
| role | enum | 消息类型：user / assistant |
| time | datetime | 消息时间 |

### Growth Log

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 记录唯一标识 |
| user_id | string | 关联 User.id |
| achievement | string | 完成事项 |
| learning | string | 学习内容 |
| problem | string | 遇到问题 |
| reflection | string | 阶段总结 / 反思 |
| date | date | 记录日期 |

### Memory

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 记忆唯一标识 |
| user_id | string | 关联 User.id |
| content | string | 记忆内容 |
| category | enum | 分类：goal / progress / preference / event |
| importance | number | 重要度（1-5） |
| created_time | datetime | 创建时间 |

### AI Recommendation AI 建议记录

- **作用**：保存 AI 提供的重要行动建议（核心数据对象）
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 建议唯一标识 |
| user_id | string | 关联 User.id |
| project_id | string | 关联 Project.id（可空） |
| task_id | string | 关联 Task.id（可空） |
| recommendation | string | 建议内容 |
| reason | string | 推荐原因 |
| status | enum | 状态：suggested / accepted / done / ignored |
| created_time | datetime | 创建时间 |

- **为什么 AI Recommendation 是核心数据**：
  - 保存 AI 输出结果（建议 + 原因），使 AI 产出可追溯
  - 支持后续复盘（哪些建议被采纳、执行效果如何），形成反馈循环
  - 连接用户行动（关联 Task 的执行状态，连接 Project 的推进）
- **与其他数据对象的关系**：
  - 与 Project：建议可关联到项目（N:1，可空），用于方向类建议
  - 与 Task：建议可关联到任务（N:1，可空），行动类建议直接落到任务
  - 与 Growth Log：建议执行后沉淀为成长记录，复盘时对照分析

---

## 4. 数据关系

```
User
 │
 ├── 1:1 ──> Profile
 │
 ├── 1:N ──> Goal
 │              │
 │              └── 1:1 ──> Project
 │                              │
 │                              └── 1:N ──> Task
 │
 ├── 1:N ──> Conversation
 │
 ├── 1:N ──> Growth Log
 │
 ├── 1:N ──> Memory
 │
 └── 1:N ──> AI Recommendation
                    │
                    ├── N:1 ──> Project（可空）
                    └── N:1 ──> Task（可空）
```

关系说明：

- `User` 是核心实体，所有数据以用户为中心组织
- `Goal` 与 `Project` 一对一：一个目标对应一个项目（V1 简化，不区分多项目）
- `Project` 与 `Task` 一对多：一个项目包含多个任务
- `Conversation`、`Growth Log`、`Memory` 均直接挂在 `User` 下，不与 Goal/Task 强关联（V1 简化）
- `AI Recommendation` 直接挂在 `User` 下，可关联到具体 Project / Task（可空）

---

## 5. V1 页面结构建议

工作台布局（单页）：

```
┌─────────────────────────────────────────────┐
│  AI 导师工作台                                  │
├──────────────────────┬──────────────────────┤
│  用户状态区域          │  AI 导师聊天区域        │
│  - 当前阶段            │  - 对话窗口            │
│  - 技能水平            │  - 结合档案/项目状态    │
│  - 学习方式            │  - 输出行动建议         │
├──────────────────────┤                      │
│  当前目标区域          │                      │
│  - 目标列表/状态        │                      │
│  - 创建/编辑目标        │                      │
├──────────────────────┤                      │
│  项目进度区域          │                      │
│  - 当前阶段            │                      │
│  - 进度               │                      │
│  - 完成内容            │                      │
├──────────────────────┤                      │
│  今日行动区域          │                      │
│  - 推荐任务            │                      │
│  - 推荐原因/完成标准    │                      │
│  - 执行状态            │                      │
└──────────────────────┴──────────────────────┘
```

布局原则：

- 左列：状态信息区（用户状态 / 目标 / 项目 / 今日行动）
- 右列：AI 对话区（主交互）
- 左列信息实时反映到右列对话上下文，AI 回答基于左侧状态生成

---

## 6. MVP 边界

### 6.1 第一版重点

- 跑通核心闭环：目标创建 → AI 理解 → 项目拆解 → 下一步行动 → 执行 → 记录成长 → AI 更新理解
- 优先保证"下一步行动"建议的质量与可用性
- 优先保证数据能被持续记录，为后续复盘与分析打基础

### 6.2 避免事项

- 过度设计：不做超出核心闭环的复杂机制
- 无限扩展功能：P1/P2 功能不进 V1
- 为技术而技术：不引入当前阶段不需要的技术复杂度（如多 Agent、知识图谱）
- 完美主义：先交付可用的最小闭环，再迭代

### 6.3 完成标准

- 用户可创建目标并看到项目状态
- AI 对话可结合档案与项目状态给出下一步行动（含推荐原因与完成标准）
- 用户可记录成长，AI 在下一次对话中体现对状态的更新理解
- 整个闭环可被单人（杏珠）连续使用一周以上

---

*文档版本：V1.0　|　维护人：杏珠　|　对应文档：01_User_Profile.md、02_User_Scenarios.md*
