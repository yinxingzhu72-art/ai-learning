import json
import os
if os.path.exists("user_profile.json"):
    with open("user_profile.json", "r", encoding="utf-8") as file:
        user_profile = json.load(file)

    user_name = user_profile["name"]
    learning_goal = user_profile["goal"]
    level = user_profile["level"]
    print("欢迎回来，" + user_name + "！")
    print("你的当前学习方向：" + learning_goal)
    print("你的水平：" + level)


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


with open("user_profile.json", "w", encoding="utf-8") as file:
    json.dump(user_profile, file, ensure_ascii=False, indent=4)