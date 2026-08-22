def complete_task(user_profile, learning_plan, task_number):

    index = task_number - 1

    if index < 0 or index >= len(learning_plan):
        return False

    task = learning_plan[task_number - 1]


    matched = False

    for history_task in user_profile.history:
        if task in history_task or history_task in task:
            matched = True
            break

    if matched:
        return False

    user_profile.history.append(task)

    return True


def calculate_progress(user_profile, learning_plan):

    completed_count = 0

    for task in learning_plan:
        if task in user_profile.history:
            completed_count += 1

    total_count = len(learning_plan)

    if total_count == 0:
        return 0

    return completed_count / total_count * 100


def get_progress_detail(user_profile, learning_plan):

    completed_count = 0

    for task in learning_plan:
        if task in user_profile.history:
            completed_count += 1

    total_count = len(learning_plan)

    return completed_count, total_count
