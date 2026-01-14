habits = []
def show_menu():
    print("\nТрекер привычек")
    print("1. Показать привычки")
    print("2. Добавить привычку")
    print("3. Отметить привычку выполненной")
    print("4. Выход")
def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            show_habits()
        elif choice == "2":
            add_habit()
        elif choice == "3":
            mark_habit_done()
        elif choice == "4":
            print("Выход из программы")
            break
        else:
            print("Неверный пункт меню")
def add_habit():
    name = input("Введите название привычки:")
    habits.append({
        "name": name,
        "done": False
    })
    print("Привычка добавлена")
def show_habits():
    if not habits:
        print("Пока привычек нет.")
        return
    else:
        for index, habit in enumerate(habits, start=1):
            name = habit["name"]
            done = habit["done"]
            status = "✓" if done else "✗"
            print(f"{index}. {name} [{status}]")
def mark_habit_done():
    if not habits:
        print("Нет привычек для отметки.")
        return
    
    show_habits()
    number = input("Введите номер привычки: ")
    number = int(number)
    index = number - 1

    habits[index]["done"] = True
    print("Привычка отмечена как выполненная.")
main()
