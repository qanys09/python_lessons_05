import json
# 01  Паспорт EventHub
# Требования
# 1. Создайте папку eventhub и файлы app.py, eventhub_db.json и README.md.
# 2. В JSON создайте корневой словарь с ключами next_event_id и events.
# 3. Добавьте два мероприятия по образцу: у каждого должны быть id, title, category, date, price, capacity и participants.
# 4. В app.py загрузите JSON и выведите количество мероприятий.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

# with open ("eventhub_db.json", "r", encoding="utf-8") as file:
#     data = json.load(file)

# print(f"Мероприяий : { len(data["events" ])}")







# 02  Надёжное хранилище
# Требования
# 1. Создайте функции load_db() и save_db(data).
# 2. Если файла нет или JSON повреждён, load_db должна вернуть пустую базу с правильными ключами.
# 3. Сохраняйте кириллицу читаемо и оформляйте JSON с отступом 4.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

FILE_NAME = "eventhub_db.json"
def load_db():
    try:
        with open(FILE_NAME,"r", encoding="utf-8") as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"next_event_id": 1, "events": []}

def save_db(data):
    with open(FILE_NAME, "w", encoding="utf_8") as file:
        json.dump(data, file, ensure_ascii=False, indent=3)









# 03  Тестовое мероприятие
# Требования
# 1. Создайте функцию add_event(data, title, category, date, price, capacity).
# 2. Используйте next_event_id как уникальный номер и создавайте пустой список participants.
# 3. Добавьте мероприятие в список, увеличьте next_event_id и сохраните базу.
# Повторение. Это задание восстанавливает навык прошлого урока и готовит основу общего проекта.

def add_event(data, title, category, date, price, capacity):
    event = {
        "id" :data["next_event_id"],
        "title" : title,
        "category" : category,
        "date": date,
        "price" : price,
        "capacity" : capacity,
        "participants" : []
    }

    data ["events"].append(event)
    data ["next_event_id"] += 1
    return event












# 04  Удобная афиша
# Требования
# 1. Создайте функцию show_events(events).
# 2. Для каждого события покажите ID, название, дату, категорию и количество свободных мест.
# 3. Если список пуст, выведите понятное сообщение.

def show_events(events):
    if not events:
        print ("Мироприятий пока нет")
        return 
    
    for event in events:
        free_places = event["capacity"] - len(event["participants"])
        print (f"{event["id"]} {event["title"]}")
        print (f"{event["date"]} {event["category"]}")
        print (f"{free_places}")












# 05  Поиск по номеру
# Требования
# 1. Создайте find_event(data, event_id).
# 2. Верните словарь мероприятия с нужным id.
# 3. Если совпадения нет, верните None.




def find_event(data,event_id):
    for event in data["events"]:
        if event["id"] == event_id:
            return event
        return None


















# 06  Тематическая подборка
# Требования
# 1. Создайте filter_by_category(data, category).
# 2. Соберите и верните новый список подходящих мероприятий.
# 3. Поиск не должен зависеть от регистра букв.


def filter_by_category(data, category):
    found_events= []
    for event in data["events"]:
        if event["category"].lower() == category.lower():
            found_events.append(event)
    return found_events











# 07  Афиша по датам
# Требования
# 1. Создайте sort_by_date(data).
# 2. Верните новый список, отсортированный по полю date с помощью sorted и lambda.
# 3. Исходный список в базе не изменяйте. Используйте формат даты ГГГГ-ММ-ДД.



def sort_by_date(data):
    return sorted (data["events"], key= lambda event : event["data"])








# 08  Бронирование места
# Требования
# 1. Создайте book_ticket(data, event_id, participant).
# 2. Запрещайте бронь, если мероприятия нет, имя уже записано или свободные места закончились.
# 3. При успехе добавьте имя в participants и верните результат с понятным сообщением.


def book_ticket(data, event_id, participant):
    event = find_event(data,event_id)

    if event is None:
        return False, "Меропряие не найдено"

    if participant in event["participant"]:
        return False, "Такое имя уже зареги-но"

    if  event["capacity"] <= event["participants"]:
        return False , "Свободных мест нет"

    event["participant"].append(participant)
    return True , "Бронь добавлено"





# 09  Отмена брони
# Требования
# 1. Создайте cancel_ticket(data, event_id, participant).
# 2. Удаляйте имя только из нужного мероприятия.
# 3. Верните True при успешной отмене и False, если событие или участник не найдены.


def cancel_ticket(data, event_id, participant):
    event = find_event(data, event_id)

    if event is None:
        return False

    if participant not in event["participants"]:
        return False

    event["participants"].remove(participant)
    return True

        
       








# 10  Редактор события
# Требования
# 1. Создайте edit_event(data, event_id, new_title, new_date, new_price).
# 2. Изменяйте только найденное мероприятие.
# 3. Верните логический результат, чтобы меню понимало, нужно ли сохранять файл.

def edit_event(data, event_id, new_title, new_date, new_price):
    event = find_event(data, event_id)   #ищем мероприятие по ID
    if event is None:  # проверяет найдено ли оно
        return False

# изменяет название
    event["title"] = new_title  
    event["date"] = new_date
    event["price"] = new_price

    return True








11
def delete_event(data , event_id):
    event = find_event(data , event_id)   #ищем мероприятие по ID

    if event is None:    # если мероприятие не найдено, возвращает False
        return False
    data["event"].remove(event)  # удаляем найденное мероприятие из списка.
    return True   # означает, что удаление прошло успешно



12

def sort_by_popularity(data):
    return sorted(data["events"], key=lambda event: len(event["participants"]), reverse=True)




13

def get_statistics(data):
    total_bookings = 0   #начальное количество бронирований
    total_income = 0  # начальный доход
    popular_event = None  # пока популярное мероприятие не определено

    for event in data["events"]:
        bookings = len(event["participants"]) #количество участников текущего мероприятия
        total_bookings += bookings   #добавляем это количество к общему числу бронирований
        total_income += bookings * event["price"]   # умножаем количество броней на цену билета и прибавляем к общему доходу

        if popular_event is None or bookings > len(popular_event["participants"]):
            popular_event = event

    popular_title = "Нет мероприятий"

    if popular_event is not None:
        popular_title = popular_event["title"]

    return {
        "events": len(data["events"]),
        "bookings": total_bookings,
        "income": total_income,
        "popular": popular_title
    }







14

def export_report(data):
    statistics = get_statistics(data)

    with open("eventhub_report.txt", "w", encoding="utf-8") as file: # режим записи
       # записывает текст в файл
       
        file.write("ОТЧЁТ EVENTHUB\n")     
        file.write(f'Мероприятий: {statistics["events"]}\n')
        file.write(f'Бронирований: {statistics["bookings"]}\n')
        file.write(f'Доход: {statistics["income"]} тг\n')
        file.write(f'Самое популярное: {statistics["popular"]}\n')




15




def read_number(message):
    try:
        return int(input(message))
    except ValueError:
        print("Введите целое число")
        return None


def main():
    data = load_db()

    while True:
        print("\n===== EVENTHUB =====")
        print("1. Показать мероприятия")
        print("2. Добавить мероприятие")
        print("3. Найти по категории")
        print("4. Отсортировать по дате")
        print("5. Забронировать место")
        print("6. Отменить бронь")
        print("7. Изменить мероприятие")
        print("8. Удалить мероприятие")
        print("9. Статистика")
        print("10. Создать отчёт")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_events(data["events"])

        elif choice == "2":
            title = input("Название: ")
            category = input("Категория: ")
            date = input("Дата ГГГГ-ММ-ДД: ")
            price = read_number("Цена: ")
            capacity = read_number("Количество мест: ")

            if price is not None and capacity is not None and capacity > 0:
                add_event(data, title, category, date, price, capacity)
                save_db(data)
                print("Мероприятие добавлено")
            else:
                print("Неверная цена или количество мест")

        elif choice == "3":
            category = input("Категория: ")
            show_events(filter_by_category(data, category))

        elif choice == "4":
            show_events(sort_by_date(data))

        elif choice == "5":
            event_id = read_number("ID мероприятия: ")
            participant = input("Имя участника: ")

            if event_id is not None:
                success, message = book_ticket(
                    data, event_id, participant
                )
                print(message)

                if success:
                    save_db(data)

        elif choice == "6":
            event_id = read_number("ID мероприятия: ")
            participant = input("Имя участника: ")

            if event_id is not None and cancel_ticket(
                data, event_id, participant
            ):
                save_db(data)
                print("Бронь отменена")
            else:
                print("Бронь не найдена")

        elif choice == "7":
            event_id = read_number("ID мероприятия: ")

            if event_id is not None:
                new_title = input("Новое название: ")
                new_date = input("Новая дата ГГГГ-ММ-ДД: ")
                new_price = read_number("Новая цена: ")

                if new_price is not None and edit_event(
                    data, event_id, new_title, new_date, new_price
                ):
                    save_db(data)
                    print("Мероприятие изменено")
                else:
                    print("Не удалось изменить мероприятие")

        elif choice == "8":
            event_id = read_number("ID мероприятия: ")

            if event_id is not None and delete_event(data, event_id):
                save_db(data)
                print("Мероприятие удалено")
            else:
                print("Мероприятие не найдено")

        elif choice == "9":
            statistics = get_statistics(data)
            print(statistics)

        elif choice == "10":
            export_report(data)
            print("Отчёт создан")

        elif choice == "0":
            print("До встречи!")
            break

        else:
            print("Такого пункта нет")


if __name__ == "__main__":
    main()









