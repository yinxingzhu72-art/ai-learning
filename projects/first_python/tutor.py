from profile import save_profile

from learning import analyze_stage, stage_advice, stage_reason, generate_learning_plan

from progress import complete_task, calculate_progress, get_progress_detail

from report import learning_report
from state import analyze_user_state


def run_tutor(user_profile):
    state = analyze_user_state(user_profile)
    user_profile.state = state.to_dict()

    stage = state.stage
    print("学习状态：")
    print(state.to_dict())
    print("下一步建议：" + state.next_action)
    print("你的当前学习阶段：" + stage)

    advice = state.next_action

    print("学习建议：" + advice)

    reason = stage_reason(stage)

    print("推荐原因：" + reason)
    if user_profile.learning_plan:
        learning_plan = user_profile.learning_plan

    else:
        learning_plan = generate_learning_plan(user_profile)
    user_profile.learning_plan = learning_plan

    print("你的学习计划：")

    for i, step in enumerate(learning_plan, 1):
        print(str(i) + ". " + step)
    completed = int(input("请输入已经完成的任务编号："))

    result = complete_task(user_profile, learning_plan, completed)

    if result:
        print("任务完成记录成功！")
        print(user_profile.history)
    else:
        print("任务已经完成或者编号错误！")
    progress = calculate_progress(user_profile, learning_plan)

    print("当前完成率：" + str(int(progress)) + "%")
    learning_report(user_profile, stage, progress, learning_plan)
    save_profile(user_profile)
