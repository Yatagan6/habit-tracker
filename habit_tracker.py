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
        if choice == "4":
            print("Выход из программы")
            break
        elif choice == "2":
            add_habit()
        else:
            print("Неверный пункт меню")
def add_habit():
    name = input("Введите название привычки: ")
    habits.append({
        "name": name,
        "done": False
    })
    print("Привычка добавлена")
def show_habits():
    pass

main()