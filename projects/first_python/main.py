from profile import load_profile, save_profile
from learning import (
    analyze_stage,
    stage_advice,
    stage_reason,
    learning_report,
    generate_learning_plan
)
from progress import complete_task, calculate_progress
user_profile = load_profile()

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
learning_plan = generate_learning_plan(user_profile)

for i, step in enumerate(learning_plan, 1):
    print(str(i) + ". " + step)
completed = int(input("请输入已经完成的任务编号："))

result = complete_task(
    user_profile,
    learning_plan,
    completed
)

if result:
    print("任务完成记录成功！")
else:
    print("任务编号错误！")
progress = calculate_progress(
    user_profile,
    learning_plan
)

print("当前学习进度：")

completed_count = 0

for task in learning_plan:
    if task in user_profile["history"]:
        completed_count += 1

print(str(completed_count) + "/" + str(len(learning_plan)))

print("完成率：" + str(int(progress)) + "%")
learning_report(
    user_profile,
    stage,
    progress,
    learning_plan
)
save_profile(user_profile)