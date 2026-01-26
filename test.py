habits = []
def show_menu():
    print("Трекер привычек")
    print("1. Добавить привычку.")
    print("2. Показать привычки.")
    print("3. Отметить привычку выполненной.")
    print("4. Выйти.")
def main():
    while True:
        show_menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            add_habit()
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню.")
def add_habit():
    name = int("Введите привычку:")
    habits.append({
        "name": name,
        "done": False
    })
    print("Привычка добавлена.")
main()
