import json

def find_player(player_id):  # Создаём функцию поиска
    with open("players.json", "r", encoding="utf-8") as file: # Открываем файл для чтения
        players = json.load(file) # Превращаем JSON в список Python

    for player in players: # Перебираем игроков
        if player["id"] == player_id: # Сравниваем ID игрока с искомым
            return player # Возвращаем найденный словарь

    return None  # Возвращает None если игрок не найден



print (find_player(2))
print (find_player(7))












9.

def level_up(player_id):
    with open ("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for player in players:
        if player["id"] == player_id:
            player["level"] +=1

            with open("players.json", "w", encoding="utf-8") as file:   # Мы записываем данные внутри цикла for потому что хотим сохранить изменения сразу как нашли нужного игрока.
                json.dump(players, file, ensure_ascii=False, indent=3)
                return True 

            return False


print(level_up(2))
print(level_up(9))




















10.

def deactivate_player(player_id):
    with open ("players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    for player in players:
        if player["id"] == player_id:
            player["active"] = False


            with open("players.json", "w", encoding= "utf-8") as file:
                json.dump(players, file, ensure_ascii=False, indent=3)

            return True
    return False

print(deactivate_player(2))
print(deactivate_player(6))