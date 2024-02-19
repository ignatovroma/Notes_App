import json
import os
from datetime import datetime


def create_note():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    note_id = len(notes) + 1
    note_title = input("\nВведите заголовок заметки: ")
    note_body = input("\nВведите текст заметки: ")

    note = {
        "id": note_id,
        "title": note_title,
        "body": note_body,
        "timestamp": timestamp
    }

    notes.append(note)
    save_notes()
    print("\nЗаметка успешно создана!")


def read_specific_note():
    note_id = int(input("\nВведите ID заметки, которую необходимо прочитать: "))
    for note in notes:
        if note['id'] == note_id:
            print(f"\nID: {note['id']}\nЗаголовок: {note['title']}\n"
                  f"Текст: {note['body']}\nДата/Время: {note['timestamp']}")
            break
    else:
        print("\nЗаметка с указанным ID не найдена.")


def read_all_notes():
    if not notes:
        print("\n>>>>> ЗАМЕТОК НЕТ <<<<<\n")
        return
    for note in notes:
        print(f"\nID: {note['id']}\nЗаголовок: {note['title']}\n"
              f"Текст: {note['body']}\nДата/Время: {note['timestamp']}")


def search_note_by_date():
    date = input("\nВведите дату создания заметки (гггг-мм-дд): ")
    found = False
    for note in notes:
        if note['timestamp'].split()[0] == date:
            print(f"\nID: {note['id']}\nЗаголовок: {note['title']}\n"
                  f"Текст: {note['body']}\nДата/Время: {note['timestamp']}")
            found = True
    if not found:
        print("\n>>>>> Заметки с указанной датой не найдено <<<<<\n")


def edit_note():
    note_id = int(input("\nВведите ID заметки, которую необходимо отредактировать: "))
    note_index = -1

    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break

    if note_index != -1:
        new_note_title = input(f"\nВведите новый заголовок заметки: {notes[note_index]['title']} ")
        new_note_body = input(f"\nВведите новый текст заметки: {notes[note_index]['body']} ")

        notes[note_index]['title'] = new_note_title
        notes[note_index]['body'] = new_note_body
        notes[note_index]['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        save_notes()
        print("\nЗаметка успешно отредактирована!")
    else:
        print("\nЗаметка с указанным ID не найдена.")


def delete_note():
    note_id = int(input("\nВведите ID заметки, которую необходимо удалить: "))
    note_index = -1
    for index, note in enumerate(notes):
        if note['id'] == note_id:
            note_index = index
            break

    if note_index != -1:
        del notes[note_index]
        save_notes()
        print("\nЗаметка успешно удалена!")
    else:
        print("\nЗаметка с указанным ID не найдена.")


def save_notes():
    try:
        with open("notes.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Произошла ошибка при сохранении заметок: {e}")


def load_notes():
    try:
        if os.path.exists("notes.json"):
            with open("notes.json", "r", encoding="utf-8") as file:
                notes.extend(json.load(file))
    except Exception as e:
        print(f"Произошла ошибка при загрузке заметок: {e}")


notes = []

load_notes()


def main():
    while True:
        print("\nМеню:")
        print("1. Создать заметку")
        print("2. Просмотреть конкретную заметку")
        print("3. Просмотреть заметку по дате создания")
        print("4. Просмотреть все заметки")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выход\n")

        choice = input("Выберите действие: ")
        if choice == "1":
            create_note()
        elif choice == "2":
            read_specific_note()
        elif choice == "3":
            search_note_by_date()
        elif choice == "4":
            read_all_notes()
        elif choice == "5":
            edit_note()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            break
        else:
            print("\n>>>>> Некорректный выбор. Попробуйте снова <<<<<\n")


if __name__ == "__main__":
    main()
