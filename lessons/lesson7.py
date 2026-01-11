def show_menu():
    print("1. Добавить.")
    print("2. Показать.")
    print("3. Выход.")
show_menu()
tasks = []
def add_task(text):
    tasks.append({
        "text": text,
        "done": False
    })
add_task("Купить хлеб")
def is_done(task):
    return (task["done"])