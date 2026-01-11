task = {
    "text": "Купить хлеб",
    "done": False
}
print(task["text"])
print(task["done"])

tasks = [
    {"text": "Помыть посуду","done": True},
    {"text": "Помыть полы", "done": True}
]
for task in tasks:
    print(task["text"])
    print(task["done"])