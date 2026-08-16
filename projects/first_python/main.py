import json
import os
def analyze_stage(history):

    completed_count = len(history)

    if completed_count < 3:
        return "入门阶段"

    elif completed_count < 6:
        return "基础阶段"

    else:
        return "进阶阶段"
def stage_advice(stage):
    if stage == "入门阶段":
        return "继续学习 Python 基础知识。"

    elif stage == "基础阶段":
        return "开始尝试独立完成小项目。"

    else:
        return "可以进入 AI 应用开发。"
def stage_reason(stage):
    if stage == "入门阶段":
        return "你还在建立基础知识，需要继续掌握 Python 核心概念。"

    elif stage == "基础阶段":
        return "你已经掌握基础语法，可以通过项目提升实际编程能力。"

    else:
        return "你已经具备基础能力，可以开始学习 AI 应用开发。"
def learning_report(user_profile, stage, progress, learning_plan):
    print("========== 学习报告 ==========")

    print("用户：" + user_profile["name"])
    print("学习方向：" + user_profile["goal"])
    print("当前阶段：" + stage)

    print("")
    print("已完成学习内容：")

    for task in learning_plan:
      if task in user_profile["history"]:
        print("√ " + task)
    print("")
    print("当前学习计划：")

    for task in learning_plan:
      if task in user_profile["history"]:
        print("✓ " + task)
      else:
        print("○ " + task)

    print("")
    print("当前完成率：" + str(int(progress)) + "%")

    print("==============================")
if os.path.exists("user_profile.json"):
    with open("user_profile.json", "r", encoding="utf-8") as file:
        user_profile = json.load(file)

    user_name = user_profile["name"]
    learning_goal = user_profile["goal"]
    level = user_profile["level"]
    print("欢迎回来，" + user_name + "！")
    print("你的当前学习方向：" + learning_goal)
    print("你的水平：" + level)
    stage = analyze_stage(user_profile["history"])

    print("你的当前学习阶段：" + stage)
    advice = stage_advice(stage)

    print("学习建议：" + advice)
    reason = stage_reason(stage)

    print("推荐原因：" + reason)


else:
 user_name = input("请输入你的名字：")

 print("你好，" + user_name + "! 欢迎来到 AI Tutor。")

 learning_goal = input("今天想学习什么？")

 level = input("你的编程基础是什么？（新手/有经验）：")
 user_profile = {
    "name": user_name,
    "goal": learning_goal,
    "level": level,
    "history": []
 }
 with open("user_profile.json", "w", encoding="utf-8") as file:
    json.dump(user_profile, file, ensure_ascii=False, indent=4)

learning_plan = []
stage = analyze_stage(user_profile["history"])
if "第一个小项目" in user_profile["history"]:
    print("你已经完成 Python 入门阶段，我们开始进阶学习。")

    learning_plan = [
        "函数深入学习",
        "文件处理",
        "AI项目开发"
    ]
elif learning_goal == "Python" and level == "新手":
    print("很好！Python 是编程入门的好选择。")

    learning_plan = [
        "Python基础语法",
        "变量和数据类型",
        "输入和输出",
        "第一个小项目"
    ]

elif learning_goal == "Python" and level == "有经验":
    print("很好，你已经有基础，我们直接进入项目训练。")

    learning_plan = [
        "Python项目结构",
        "数据处理",
        "AI应用开发"
    ]

else:
    print("好的，我们来学习 " + learning_goal + "!")

    learning_plan = [
        "了解基础概念",
        "完成练习",
        "制作小项目"
    ]

print("你的学习计划：")

for i, step in enumerate(learning_plan, 1):
    print(str(i) + ". " + step)
completed = input("请输入已经完成的任务编号：")
completed_index = int(completed) - 1

if completed_index < 0 or completed_index >= len(learning_plan):
    print("输入错误，请输入正确的任务编号。")
else:
    completed_task = learning_plan[completed_index]

    if completed_task not in user_profile["history"]:
        user_profile["history"].append(completed_task)

completed_count = 0

for task in learning_plan:
    if task in user_profile["history"]:
        completed_count += 1

total_count = len(learning_plan)

progress = completed_count / total_count * 100

print("当前学习进度：")
print(str(completed_count) + "/" + str(total_count))
print("完成率：" + str(int(progress)) + "%")
learning_report(
    user_profile,
    stage,
    progress,
    learning_plan
)
with open("user_profile.json", "w", encoding="utf-8") as file:
    json.dump(user_profile, file, ensure_ascii=False, indent=4)