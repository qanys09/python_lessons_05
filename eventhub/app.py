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

def save_bd(data):
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

        event = find_event(data,event_id)
        if event is None:
                return False
        
        if participant not in  event["participant"]:
                return False
        
        else   event["participant"].remove(participant):
                return True 
        
       








# 10  Редактор события
# Требования
# 1. Создайте edit_event(data, event_id, new_title, new_date, new_price).
# 2. Изменяйте только найденное мероприятие.
# 3. Верните логический результат, чтобы меню понимало, нужно ли сохранять файл.
