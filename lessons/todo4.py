tasks = []
while True:
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("5. Выход")
    choice = input("Выберите пункт: ")
    if choice == "5":
        break
    if choice == "1":
        text = input("Введит задачу: ")
        tasks.append({
            "text": text,
            "done": False
        })
        print("Задача добавлена.")
    if choice == "2":
        if not tasks:
            print("Нет задач.")
        else:
            for task in tasks:
                if task["done"]:
                    print(f"[X] {task['text']}")
                else:
                    print(f"[ ] {task['text']}")
    if choice == "3":
        if not tasks:
            print("Нет задач.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['text']}")
            number = int(input("Введите номер задачи:"))
            tasks[number - 1]["done"] = True
    if choice == "4":
        if not tasks:
            print("Нет задач.")
        else:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['text']}")
            number = int(input("Введите номер:"))
            tasks.pop(number-1)
            print("Задача удалена.")

