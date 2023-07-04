
tasks = []
def add_task(task):
    tasks.append(task)
def show_tasks():
    if not tasks:
        print("Die Liste ist leer.")
    else:
        for task in tasks:
            print(task)
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Aufgabe entfernt.")
    else:
        print("Aufgabe nicht gefunden.")

def mark_task_done(task):
    if task in tasks:
        index = tasks.index(task)
        tasks[index] = f"[ERLEDIGT] {task}"
        print("Aufgabe als erledigt markiert.")
    else:
        print("Aufgabe nicht gefunden.")


def main_menu():
    while True:
        print("ToDo-Liste")
        print("1. Aufgabe hinzufügen")
        print("2. Aufgaben anzeigen")
        print("3. Aufgabe entfernen")
        print("4. Aufgabe als erledigt markieren")
        print("5. Beenden")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            task = input("Gib den Namen der Aufgabe ein: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            task = input("Gib den Namen der Aufgabe ein, die du entfernen möchtest: ")
            remove_task(task)
        elif choice == "4":
            task = input("Gib den Namen der Aufgabe ein, die du als erledigt markieren möchtest: ")
            mark_task_done(task)
        elif choice == "5":
            break
        else:
            print("Ungültige Option. Versuche es erneut.")
main_menu()
