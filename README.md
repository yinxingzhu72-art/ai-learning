## Project Status

🚧 Developing

Current Version: v0.5

Completed:
- User profile system
- Learning memory
- Learning plan generation
- Progress tracking
# AI Learning Journey

这是我的 AI 学习与项目实践仓库。

记录从 Python 基础、AI 技术学习，到 AI 应用开发的完整过程。

---

## AI Tutor Project

AI Tutor 是当前主要开发项目。

目标：

打造一个能够帮助用户：
- 明确学习目标
- 分析学习状态
- 提供下一步行动建议
- 形成持续学习反馈循环

的 AI 学习助手。

---

## Current Status

Version: v0.5

AI Tutor Prototype - User Profile & Learning Memory System

目前已经完成：

- [x] Git / GitHub 项目环境
- [x] Python 开发环境
- [x] 基础交互程序
- [x] 用户信息输入
- [x] 学习目标收集
- [x] 简单学习方向判断
- [x] 用户档案 JSON 保存
- [x] 用户档案自动读取
- [x] 学习水平记录
- [x] 学习历史记录框架
- [x] 根据用户情况生成学习计划
- [x] 用户档案系统
- [x] 学习历史记录
- [x] 根据学习状态调整学习路线
- [x] UserProfile 用户数据模型
- [x] 用户画像对象化设计
- [x] 用户状态持久化
- [x] 学习计划管理
- [x] 学习任务完成记录
- [x] 学习进度计算
- [x] 学习报告生成
当前 MVP 已支持：

- 保存用户学习信息
- 记录学习历史
- 根据用户状态生成不同学习计划

当前原型：

projects/first_python/main.py

已实现流程：

用户首次使用
↓
输入姓名、学习目标、编程水平
↓
生成 user_profile.json
↓
再次启动自动读取用户档案
↓
生成个性化学习计划
↓
保存学习历史


---

## Repository Structure

projects
└── first_python
    ├── main.py
    ├── models.py
    ├── profile.py
    ├── tutor.py
    ├── learning.py
    ├── progress.py
    ├── report.py
    └── user_profile.json


---

## Development Roadmap

### Phase 1 - Foundation
- Python 基础
- Git 工作流
- 项目结构建立

### Phase 2 - AI Tutor Prototype
- 用户状态收集
- 学习目标分析
- 基础推荐逻辑

### Phase 3 - AI Capability
- 接入 AI 模型
- Prompt 设计
- 用户长期记忆

### Phase 4 - Intelligent Learning System
- 个性化学习规划
- 学习反馈分析
- 自动调整策略
### Phase 5- AI Tutor Prototype (Current)
- UserProfile system
- Learning memory
- Learning progress tracking
- Feedback loop
### Phase 6 - AI Capability
- LLM integration
- Intelligent learning suggestions
- Long-term user memory


---

## Philosophy

学习 AI 不只是学习技术。

更重要的是：

通过 AI 和软件开发，
解决真实问题，
建立持续迭代能力。

## Current Architecture

AI Tutor currently uses a modular Python architecture:

User
 ↓
UserProfile Model
 ↓
Tutor Logic
 ↓
Learning Plan
 ↓
Progress Tracking
 ↓
Learning Report

---

## Progress

Started:
2026

Current Status:

Building AI Tutor prototype.