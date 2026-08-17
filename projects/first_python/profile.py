import json
import os


def load_profile():

    if os.path.exists("user_profile.json"):

        with open("user_profile.json", "r", encoding="utf-8") as file:
            user_profile = json.load(file)

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
            "history": []
        }

        save_profile(user_profile)

        return user_profile



def save_profile(user_profile):

    with open("user_profile.json", "w", encoding="utf-8") as file:

        json.dump(
            user_profile,
            file,
            ensure_ascii=False,
            indent=4
        )