class UserProfile:

    def __init__(self, name, goal, level):
        self.name = name
        self.goal = goal
        self.level = level
        self.history = []
        self.learning_plan = []


    def add_history(self, task):
        self.history.append(task)

    def set_learning_plan(self, plan):
        self.learning_plan = plan
    def to_dict(self):
        return {
            "name": self.name,
            "goal": self.goal,
            "level": self.level,
            "history": self.history,
            "learning_plan": self.learning_plan
        }
user = UserProfile(
    "杏珠",
    "Python",
    "新手"
)


user.add_history("Python基础语法")


user.set_learning_plan(
    [
        "Python基础",
        "第一个项目",
        "AI应用开发"
    ]
)


print(user.to_dict())