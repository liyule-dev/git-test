# 简易待办清单(Todo List)
# 题目：做一个命令行版待办工具，循环接收用户指令，支持4个功能：
# 1. 输入  add ：添加一条待办事项
# 2. 输入  list ：列出所有待办事项（带序号）
# 3. 输入  done ：输入序号，标记对应事项已完成
# 4. 输入  exit ：退出程序
# 考察点：while循环、列表操作、for循环、分支判断、用户交互逻辑
# 进阶挑战：已完成的事项单独归类显示，支持删除指定事项。

# 简易命令行待办清单
todo_list = []  # 存储所有待办事项
print("=== 简易待办工具 ===")
print("支持指令：add(添加)、list(列出)、done(标记完成)、exit(退出)")

# 循环接收用户指令
while True:
    command = input("\n请输入指令：").strip().lower()

    if command == "add":
        content = input("请输入待办事项：")
        todo_list.append(content)
        print("添加成功")

    elif command == "list":
        if not todo_list:
            print("暂无待办事项")
        else:
            print("当前待办列表：")
            for index in range(len(todo_list)):
                print(f"{index + 1}. {todo_list[index]}")

    elif command == "done":
        if not todo_list:
            print("没有可标记的待办事项")
        else:
            num = int(input("请输入要完成的序号："))
            if 1 <= num <= len(todo_list):
                finished = todo_list.pop(num - 1)
                print(f"已完成：{finished}")
            else:
                print("序号不存在")

    elif command == "exit":
        print("程序退出")
        break

    else:
        print("无效指令，请重新输入")
