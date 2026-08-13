user_name = input("请输入你的名字：")

print("你好，" + user_name + "！欢迎来到 AI Tutor。")
learning_goal = input("今天想学习什么？")
if learning_goal == "Python":
    print("很好！Python 是编程入门的好选择，我们先学习变量和输入输出。")
else:
    print("好的，我们来学习 " + learning_goal + "！")