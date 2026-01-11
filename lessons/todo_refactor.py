def show_menu():
    print("1. Добавить задачу.")
    print("2. Показать задачи.")
    print("3. Отметить задачу выполненной.")
    print("4. Удалить задачу.")
    print("5. Выход.")

def add_task(tasks):
    text = input("Введите задачу: ")
    tasks.append({
        "text": text,
        "done": False
    })
    print("Задача добавлена.")


def show_tasks(tasks):
    if not tasks:
        print("Нет задач")
    else:
        for task in tasks:
            if task["done"]:
                print(f"[X] {task['text']}")
            else:
                print(f"[ ] {task['text']}")

def mark_task_done(tasks):
    if not tasks:
        print("Нет задач.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['text']}")
        number = int(input("Введите номер задачи:"))
        tasks[number - 1]["done"] = True
        print("Задача отмечена выполненой.")

def remove_task(tasks):
    if not tasks:
        print("Нет задач")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['text']}")
        number = int(input("Введите номер задачи:"))
        tasks.pop(number-1)
        print("Задача удалена.")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Выберите пункт: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Выход.")
            break
        else:
            print("Неверный пункт.")


main()
