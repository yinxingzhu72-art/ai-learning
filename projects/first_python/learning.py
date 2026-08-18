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

def generate_learning_plan(user_profile):

    history = user_profile["history"]
    learning_goal = user_profile["goal"]
    level = user_profile["level"]

    if "第一个小项目" in history:
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

    return learning_plan