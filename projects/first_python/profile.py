from models import UserProfile
import os
import json

from config import USER_PROFILE_PATH


def load_profile():

    if os.path.exists(USER_PROFILE_PATH) and os.path.getsize(USER_PROFILE_PATH) > 0:

     with open(USER_PROFILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

     user_profile = UserProfile(
        data["name"],
        data["goal"],
        data["level"]
     )
     user_profile.history = data["history"]
     if "learning_plan" in data:
            user_profile.learning_plan = data["learning_plan"]
     else:
            user_profile.learning_plan = []

     return user_profile

    else:
        user_name = input("请输入你的名字：")

        print("你好，" + user_name + "! 欢迎来到 AI Tutor。")

        learning_goal = input("今天想学习什么？")

        level = input("你的编程基础是什么？（新手/有经验）：")

        user_profile = {
            "name": user_name,
            "goal": learning_goal,
            "level": level,
            "history": [],
            "learning_plan": [],
        }

        save_profile(user_profile)

        return user_profile


def save_profile(user_profile):

    data = {
        "name": user_profile.name,
        "goal": user_profile.goal,
        "level": user_profile.level,
        "history": user_profile.history,
        "learning_plan": user_profile.learning_plan
    }

    with open(USER_PROFILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def show_learning_memory(user_profile):
    print("")
    print("========== 学习记忆 ==========")

    history = user_profile.history

    if history:
        print("你之前学习过：")

        for item in history:
            print("✓ " + item)

    else:
        print("还没有学习记录")

    print("==============================")
