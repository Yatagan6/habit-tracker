habits = []
while True:
    print("\nТрекер ривычек")
    print("1.Показать привычку.")
    print("2.Добавить привычку.")
    print("3.Выход.")
    choice = input("Выберите действие: ")
    if choice == "1":
        if not habits:
            print("Привычек пока нет.")
        else:
            for index, habit in enumerate(habits, start=1):
                status = "✓" if habit["done"] else "✗"
                print(f"{index}. {habit['name']} [{status}]")
    elif choice == "2":
        name = input("Введите название привычки.")
        habits.append({
            "name": name,
            "done": False
        })
        print("Привычка добавлена.")
    elif choise == "3":
        print("Выход из приложения.")
        break
    else:
        print("Неверный выбор.")
