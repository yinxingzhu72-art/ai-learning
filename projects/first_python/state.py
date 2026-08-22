class UserState:

    def __init__(
        self,
        stage,
        completed_count,
        next_action
    ):
        self.stage = stage
        self.completed_count = completed_count
        self.next_action = next_action


    def to_dict(self):
        return {
            "stage": self.stage,
            "completed_count": self.completed_count,
            "next_action": self.next_action
        }
def analyze_user_state(user_profile):

    completed_count = len(user_profile.history)

    if completed_count < 3:
        stage = "入门阶段"
        next_action = "继续学习Python基础"

    elif completed_count < 6:
        stage = "基础阶段"
        next_action = "尝试完成第一个项目"

    else:
        stage = "进阶阶段"
        next_action = "学习AI应用开发"


    return UserState(
        stage,
        completed_count,
        next_action
    )