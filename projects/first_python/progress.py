def complete_task(user_profile, learning_plan, task_number):

    index = task_number - 1

    if index < 0 or index >= len(learning_plan):
        return False

    task = learning_plan[index]

    if task not in user_profile["history"]:
        user_profile["history"].append(task)

    return True


def calculate_progress(user_profile, learning_plan):

    completed_count = 0

    for task in learning_plan:
        if task in user_profile["history"]:
            completed_count += 1

    total_count = len(learning_plan)

    if total_count == 0:
        return 0

    return completed_count / total_count * 100