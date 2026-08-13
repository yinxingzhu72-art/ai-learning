# AI Tutor 数据库设计（AI Tutor Database Design）V1.0

> 本文档定义 AI 导师 V1 的数据库设计：核心数据对象、关系、数据生命周期与记忆策略。
> 数据库是 AI Tutor 的长期记忆基础，目标是简单、清晰、可扩展，重点支持 AI Tutor MVP。
> 本文档为 03_MVP_Features.md 数据模型的实现细化，字段定义以本文档为准。

---

## 1. 数据库整体设计思想

数据库帮助 AI 按以下链路理解用户：

```
用户是谁（User / Profile）
    ↓
用户目标（Goal）
    ↓
用户项目（Project）
    ↓
用户任务（Task）
    ↓
AI 建议（AI Recommendation）
    ↓
成长反馈（Growth Log）
    ↓
长期记忆（Memory）
```

设计思想：

- 数据按"理解用户 → 推进项目 → 记录成长"组织
- 每一层数据都是上一层的细化：User → Goal → Project → Task
- 行动与对话数据（Conversation / AI Recommendation）沉淀后转化为成长数据（Growth Log）与长期记忆（Memory）

---

## 2. 核心数据对象（Entity Design）

### User 用户

- **作用**：表示系统使用者（登录身份）
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 用户唯一标识（主键） |
| name | string | 用户名称 |
| created_time | datetime | 创建时间 |

- **为什么需要 User**：所有数据以用户为中心组织；单用户系统仍需 User 作为数据归属的根节点，便于未来扩展多用户。

### Profile 用户档案

- **作用**：帮助 AI 理解用户
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| user_id | string | 关联 User.id（1:1） |
| identity | string | 用户身份 / 定位 |
| skills | list | 技能水平 |
| learning_style | list | 学习方式 |
| preferences | list | 决策偏好 |
| long_term_goal | string | 长期目标 |

- **Profile 与 User 的区别**：User 是身份（账号、登录），Profile 是画像（AI 决策输入）。User 解决"谁在用"，Profile 解决"这个用户是怎样的、如何给建议"。

### Goal 目标

- **作用**：记录用户想达到的方向
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 目标唯一标识（主键） |
| user_id | string | 关联 User.id |
| title | string | 目标标题 |
| description | string | 目标描述（含成功标准） |
| status | enum | active / paused / completed / archived |
| start_date | date | 开始日期 |
| target_date | date | 目标日期 |

### Project 项目

- **作用**：记录目标对应的实际项目
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 项目唯一标识（主键） |
| goal_id | string | 关联 Goal.id（1:1） |
| name | string | 项目名称 |
| current_stage | string | 当前阶段 |
| progress | number | 进度（0-100） |
| status | enum | active / blocked / done / archived |

### Task 任务

- **作用**：记录具体行动
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 任务唯一标识（主键） |
| project_id | string | 关联 Project.id |
| title | string | 任务标题 |
| priority | enum | high / medium / low |
| status | enum | todo / doing / done / cancelled |
| created_time | datetime | 创建时间 |
| completed_time | datetime | 完成时间（可空） |

### Conversation 对话记录

- **作用**：保存用户与 AI 的交流历史
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 消息唯一标识（主键） |
| user_id | string | 关联 User.id |
| message | string | 消息内容 |
| role | enum | user / assistant |
| time | datetime | 消息时间 |

- **聊天记录不等于长期记忆**：对话是原始过程数据，量大、含噪声，用于短期上下文；长期理解依赖提炼后的 Memory，而非全部聊天。

### Growth Log 成长记录

- **作用**：记录用户成长变化
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 记录唯一标识（主键） |
| user_id | string | 关联 User.id |
| achievement | string | 完成事项 |
| learning | string | 学习内容 |
| problem | string | 遇到问题 |
| reflection | string | 阶段总结 / 反思 |
| date | date | 记录日期 |

### Memory 长期记忆

- **作用**：保存 AI 需要长期理解的信息
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 记忆唯一标识（主键） |
| user_id | string | 关联 User.id |
| content | string | 记忆内容 |
| category | enum | goal / progress / preference / event |
| importance | number | 重要度（1-5） |
| created_time | datetime | 创建时间 |

- **不是所有聊天都会进入 Memory**：仅重要信息（偏好、目标变化、关键经验）由系统规则或复盘提炼后写入，避免噪声污染长期记忆。

### AI Recommendation AI 建议记录

- **作用**：保存 AI 提供的重要行动建议
- **字段**：

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 建议唯一标识（主键） |
| user_id | string | 关联 User.id |
| project_id | string | 关联 Project.id（可空） |
| task_id | string | 关联 Task.id（可空） |
| recommendation | string | 建议内容 |
| reason | string | 推荐原因 |
| status | enum | suggested / accepted / done / ignored |
| created_time | datetime | 创建时间 |

- **为什么需要单独保存 AI Recommendation**：
  - AI 建议是核心产出，需要可追溯（当时推荐了什么、为什么）
  - 用于复盘：哪些建议被采纳、执行效果如何，形成反馈循环
  - 用于改进：积累建议数据，评估 AI 判断质量

---

## 3. 数据关系设计

```
User
 ├── 1:1 ──> Profile
 ├── 1:N ──> Goal
 │              └── 1:1 ──> Project
 │                              └── 1:N ──> Task
 ├── 1:N ──> Conversation
 ├── 1:N ──> Growth Log
 ├── 1:N ──> Memory
 └── 1:N ──> AI Recommendation
                    │
                    ├── N:1 ──> Project（可空）
                    └── N:1 ──> Task（可空）
```

各对象关系说明：

| 关系 | 类型 | 说明 |
| --- | --- | --- |
| User → Profile | 1:1 | 一个用户一份档案 |
| User → Goal | 1:N | 一个用户可有多个目标（可并行/归档） |
| Goal → Project | 1:1 | V1 简化：一个目标对应一个项目 |
| Project → Task | 1:N | 一个项目包含多个任务 |
| User → Conversation | 1:N | 对话挂在用户下 |
| User → Growth Log | 1:N | 成长记录挂在用户下 |
| User → Memory | 1:N | 长期记忆挂在用户下 |
| User → AI Recommendation | 1:N | 建议挂在用户下 |
| AI Recommendation → Project / Task | N:1（可空） | 建议可关联到具体项目或任务，也可能不关联（如方向建议） |

---

## 4. 数据生命周期

示例：用户提问"我今天应该做什么？"

```
1. 读取用户状态（User / Profile）
    ↓
2. 读取项目状态（Goal / Project / Task）
    ↓
3. AI 生成建议
    ↓
4. 保存 AI Recommendation
    ↓
5. 用户执行任务
    ↓
6. 更新 Task（status → done, completed_time）
    ↓
7. 生成 Growth Log（achievement / learning / reflection）
    ↓
8. 更新 Memory（重要经验写入）
```

| 步骤 | 动作 | 涉及数据 |
| --- | --- | --- |
| 1 | 读取用户是谁、当前状态 | User / Profile |
| 2 | 读取当前目标与项目进展 | Goal / Project / Task |
| 3 | AI 结合上下文生成建议 | —（AI Layer） |
| 4 | 持久化建议与原因 | AI Recommendation |
| 5 | 用户按建议执行 | —（用户操作） |
| 6 | 任务状态更新 | Task |
| 7 | 沉淀完成事项与反思 | Growth Log |
| 8 | 提炼重要信息入长期记忆 | Memory |

循环反馈：第 8 步更新的 Memory 会成为下一次第 1、2 步读取的上下文，形成闭环。

---

## 5. AI 记忆策略

V1 采用简单记忆方案，不引入向量库 / RAG。

### 临时记忆

| 内容 | 存储 | 说明 |
| --- | --- | --- |
| 当前对话 | Conversation（近期） | 本次会话上下文 |
| 当前任务上下文 | Task（进行中） | 正在推进的任务状态 |

### 长期记忆

| 内容 | 存储 | 说明 |
| --- | --- | --- |
| 用户偏好 | Profile / Memory | 学习方式、决策偏好 |
| 长期目标 | Goal | 目标与状态 |
| 重要经验 | Memory | 提炼后的关键经验 |

### 明确边界

- 不保存 AI 内部推理过程（CoT 细节不入库）
- 只保存结论性建议（AI Recommendation）与提炼后记忆（Memory）
- 临时记忆到长期记忆的转化：由复盘流程或重要事件触发，而非自动全量写入

---

## 6. 数据库设计原则

### 简单优先

- V1 避免复杂设计（无分区、无复杂索引优化、无中间表）
- 单表结构清晰直白，优先可读性

### 服务产品目标

- 数据设计必须服务三件事：

| 目标 | 对应数据 |
| --- | --- |
| 理解用户 | User / Profile / Memory |
| 推进项目 | Goal / Project / Task |
| 记录成长 | Growth Log / Conversation / AI Recommendation |

### 可扩展

- 未来可平滑增加：更高级 Memory（向量化）、知识库、多 Agent
- 预留方式：保持数据对象边界清晰、外键关系规范，扩展时新增表即可，不改动现有结构

---

## 7. V1 数据库范围

明确支持以下能力：

1. 用户创建账号
2. 建立用户档案
3. 创建目标
4. 管理项目
5. 管理任务
6. 保存 AI 建议
7. 保存聊天记录
8. 保存成长记录
9. 保存长期记忆

对应表：User、Profile、Goal、Project、Task、AI Recommendation、Conversation、Growth Log、Memory，共 9 张表，全部在本文档定义范围内。

---

*文档版本：V1.0　|　维护人：杏珠　|　对应文档：03_MVP_Features.md（数据模型）、05_Tech_Architecture.md（技术架构）*
