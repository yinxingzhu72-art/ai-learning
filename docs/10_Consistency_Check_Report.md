# AI Tutor 文档一致性检查报告（AI Tutor Documentation Consistency Report）

> 检查对象：README.md + docs/01-09 共 10 份文档
> 检查方法：逐份对照数据模型、API、Prompt 上下文、技术架构、MVP 范围、开发阶段、产品定位
> 检查日期：设计阶段收尾后

---

## 1. 总体检查结果

| 结果 | 数量 |
| --- | --- |
| ✅ 一致项 | 24 |
| ⚠️ 需要关注项 | 5 |
| ❌ 冲突项 | 4 |

**结论**：整体架构、技术选型、核心流程、产品定位一致，设计主体可进入开发；存在 4 处字段级冲突，均集中在 03 与 06 的数据模型定义，建议进入开发前统一。

---

## 2. 数据模型检查表

检查范围：03_MVP_Features.md（逻辑模型）vs 06_Database_Design.md（物理细化）vs 07_API_Design.md（接口字段）vs 08_Prompt_Design.md（上下文来源）

| 检查项 | 结果 | 说明 |
| --- | --- | --- |
| User | ✅ | 03 与 06 字段完全一致（id / name / created_time） |
| User Profile / Profile | ❌ | 实体名不一致（03"User Profile" vs 06"Profile"）；字段集不一致：03 有 `current_stage`、`updated_time`、`decision_preferences`，06 为 `preferences` 且无前两者 |
| Goal | ✅ | 03 与 06 字段一致（id / user_id / title / description / status / start_date / target_date） |
| Project | ✅ | 03 与 06 字段一致（id / goal_id / name / current_stage / progress / status） |
| Task | ✅ | 03 与 06 字段一致（id / project_id / title / priority / status / created_time / completed_time） |
| Conversation | ❌ | 消息类型字段名冲突：03 用 `type`，06 用 `role`（取值均为 user / assistant） |
| Growth Log | ❌ | 时间字段名冲突：03 用 `log_time`，06 用 `date` |
| Memory | ✅ | 03 与 06 字段一致（id / user_id / content / category / importance / created_time） |
| AI Recommendation | ❌ | 06 新增实体，03 数据模型与关系图中缺失（06 已声明"字段以本文档为准"，但 03 未同步） |
| 数据关系 | ⚠️ | 03 关系图无 AI Recommendation；06 有（含到 Project/Task 的可空关联）。其余关系（User→Profile 1:1、Goal→Project 1:1、Project→Task 1:N）一致 |
| 07 API 返回字段 | ⚠️ | `/api/profile/{user_id}` 返回 `preferences`（与 06 一致），与 03 的 `decision_preferences` 不一致 |

---

## 3. API 检查表

检查范围：07_API_Design.md 与 05_Tech_Architecture.md、06_Database_Design.md、README.md

| 接口 | 相关文档 | 状态 |
| --- | --- | --- |
| GET /api/users/{id} | 06 User 表 | ✅ 对应一致 |
| GET /api/profile/{user_id} | 06 Profile 表 / 03 档案 | ⚠️ 字段与 06 一致，与 03 冲突（见数据模型检查） |
| POST /api/goals | 06 Goal 表 / 03 目标管理 | ✅ 一致 |
| GET /api/goals | 06 Goal 表 | ✅ 一致 |
| PUT /api/goals/{id} | 06 Goal 表 | ✅ 一致 |
| POST /api/projects | 06 Project 表 / 03 项目管理 | ✅ 一致 |
| GET /api/projects/{id} | 06 Project 表 | ✅ 一致 |
| PUT /api/projects/{id} | 06 Project 表 | ✅ 一致 |
| POST /api/tasks | 06 Task 表 / 03 任务管理 | ✅ 一致 |
| GET /api/tasks | 06 Task 表 | ✅ 一致 |
| PUT /api/tasks/{id} | 06 Task 表 | ✅ 一致 |
| POST /api/ai/recommend | 05 AI 流程 / README §5 | ✅ 流程一致（读取上下文→Prompt→调用→保存→返回） |
| POST /api/chat | 05 AI 流程 | ✅ 流程一致 |
| 模块关系 | 05 §3 模块 vs 03 P0 模块 | ✅ Backend 五模块（用户/目标/项目/任务/AI 调用）对应一致 |
| Memory 数据访问 | 06 Memory 表 | ⚠️ 07 无 Memory 独立读写接口，仅 recommend 流程内部读取，写入途径未在 API 层明确 |

---

## 4. Prompt 上下文检查

检查范围：08_Prompt_Design.md 的 Context 来源 vs 06 数据库 vs 07 API

| Context 来源 | 数据库（06） | API（07） | Prompt（08） | 状态 |
| --- | --- | --- | --- | --- |
| User Profile | Profile 表 | /api/profile/{user_id} | Context Prompt 包含 | ✅ 一致 |
| Goal | Goal 表 | /api/goals | Context Prompt 包含 | ✅ 一致 |
| Project State | Project 表 | /api/projects/{id} | Context Prompt 包含 | ✅ 一致 |
| Task | Task 表 | /api/tasks | Context Prompt 包含 | ✅ 一致 |
| History | Conversation / Growth Log | /api/chat | Context Prompt 包含 | ✅ 一致 |
| Memory | Memory 表 | 无独立接口（recommend 内部读取） | Context Prompt 包含 | ⚠️ 来源一致，但 API 层无显式存取途径 |

---

## 5. 架构一致性检查

检查范围：05_Tech_Architecture.md 与 README.md、09_MVP_Development_Plan.md

| 模块 | 文档位置 | 状态 |
| --- | --- | --- |
| Frontend（Next.js） | 05 §8 / README §6 / 09 学习路线 | ✅ 技术选型统一 |
| Backend（FastAPI） | 05 §8 / README §6 / 09 学习路线 | ✅ 统一 |
| Database（PostgreSQL） | 05 §8 / README §6 / 09 学习路线 | ✅ 统一 |
| AI Layer（LLM API） | 05 §8 / README §6 / 09 学习路线 | ✅ 统一 |
| 四层结构 | 05 §1 / README §4 | ✅ 结构一致 |
| AI 工作流程 | 05 §7 / 07 §12 / README §5 | ⚠️ 主流程一致；README 末步简写为"保存成长记录"，07 为"保存 AI Recommendation + Conversation" |
| MVP 功能范围 | 03 P0/P1 vs README §3 | ✅ 用户档案/目标/项目/任务/AI建议/成长记录均有；README 的"长期记忆"对应 06 Memory，非 03 独立模块（口径差异，低风险） |
| 开发阶段 Phase 0-6 | 09 §3 vs README §9 | ✅ 名称、顺序、内容一致（README 为简表） |
| 使用场景覆盖 | 02 vs 03/04 | ⚠️ 02 场景五"长期成长分析"对应 03 P1 复盘模块的"阶段成长分析"，术语略异但语义一致 |

---

## 6. 发现的问题

### 问题 1（❌）：Profile 实体名与字段集不统一

- **问题**：03 为"User Profile"（含 current_stage / updated_time / decision_preferences），06 为"Profile"（preferences，无前两者）
- **影响**：开发建表时无法确定字段依据；AI 上下文组装（07/08）以 06 为准，但 03 文档描述与其不符，造成理解混乱
- **建议修改方式**：以 06 为准统一。修改 03：实体名改为 Profile，字段同步为 identity / skills / learning_style / preferences / long_term_goal；`current_stage` 如需保留，明确其归属（如放 Profile 或并入 Project.current_stage，避免重复定义）

### 问题 2（❌）：Conversation 消息类型字段名冲突

- **问题**：03 用 `type`，06 用 `role`（07/08 未直接引用该字段，未扩散）
- **影响**：建表与序列化字段名不一致
- **建议修改方式**：统一为 `role`（06 已用，且语义更明确：user / assistant）

### 问题 3（❌）：Growth Log 时间字段名冲突

- **问题**：03 用 `log_time`（datetime），06 用 `date`（date）
- **影响**：字段名与类型双重不一致
- **建议修改方式**：统一为 `date`（06 已用），或统一为 `log_time` 并同步类型；任选其一，两文档同步

### 问题 4（❌）：AI Recommendation 实体在 03 缺失

- **问题**：06 新增 AI Recommendation（含 project_id / task_id / status 等），03 数据模型与关系图未包含
- **影响**：03 作为功能需求文档缺少"保存 AI 建议"的数据支撑；开发以 06 为准可规避，但文档体系不完整
- **建议修改方式**：在 03 数据模型与关系图补入 AI Recommendation，并注明其与 Project/Task 的可空关联

### 问题 5（⚠️）：Memory 无独立 API 途径

- **问题**：06 定义 Memory 表，08 要求 AI 参考 Memory，但 07 未提供 Memory 的读写接口
- **影响**：开发时 Memory 的写入（由谁在何时写）缺乏接口依据
- **建议修改方式**：在 07 补充说明 Memory 的写入途径（如由 recommend / chat 流程内部完成，不单独暴露接口），或在 V1 增加只读接口 GET /api/memory

### 问题 6（⚠️）：README 与 07 的流程末步表述简化

- **问题**：README §5 末步"保存成长记录"，07 §7/§12 为"保存 AI Recommendation + Conversation"
- **影响**：无功能冲突，仅表述粒度不同
- **建议修改方式**：README 末步改为"保存 AI 建议与对话记录"（保持简表风格）

### 问题 7（⚠️）：02 与 03 的场景/功能术语对应

- **问题**：02 场景五"长期成长分析"在 03 中对应 P1 复盘模块的"阶段成长分析"，非精确同名
- **影响**：无功能冲突，术语不统一
- **建议修改方式**：03 P1 复盘模块说明中注明"含长期成长分析（见 02 场景五）"

---

## 7. 最终建议

### 是否可以进入开发阶段

**可以，建议先完成 4 处字段级统一（问题 1-4）后进入。** 架构、技术选型、流程、Phase 规划均一致，不阻塞开发启动；冲突集中在数据模型字段命名，属低成本修正。

### 是否需要修改设计

需要**小范围修改**，不涉及架构调整：

- 必须：03 与 06 的数据模型同步（Profile / Conversation / Growth Log / AI Recommendation，4 处）
- 建议：07 明确 Memory 存取途径；README 流程末步表述对齐

### 下一步建议

1. 指定 06_Database_Design.md 为数据模型**唯一权威文档**，03 同步更新（或反向，二选一）
2. 按问题清单完成修订后，更新 03 的版本号并标注变更
3. 修订完成后进入 Phase 0（环境准备）开发
4. 开发过程中以 06 表结构为建表依据、07 接口为前后端契约，遇到文档未覆盖细节回填本文档体系

---

*审查报告版本：V1.0　|　检查对象：README.md + docs/01-09　|　审查员：AI 文档审查流程*
