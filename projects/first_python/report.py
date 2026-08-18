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