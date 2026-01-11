tasks = [
    {"text": "Купить хлеб", "done": False},
    {"text": "Купить колбасы", "done": True}
]
for task in tasks:
    if task["done"]:
        print(f"[X] {task['text']}")
    else:
        print(f"[ ] {task['text']}")
