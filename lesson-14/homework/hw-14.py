# 1. Task: JSON Parsing
# Write a Python script that reads the students.jon JSON file and prints details of each student.
import os
import requests
import json

FILENAME = 'students.json'


def load_data():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return []
    with open(FILENAME, 'r') as f:
        return json.load(f)


def save_data(data):
    with open(FILENAME, 'w') as f:
        json.dump(data, f, indent=3)


def add_student():
    n = 1
    name = input("Ism: ")
    age = int(input("Yosh: "))
    course = int(input('Kurs: '))
    scores = []
    for i in range(3):
        score = int(input(f"{n}-bahoni kiriting: "))
        n += 1
        scores.append(score)
    students = load_data()
    students.append({'name': name, 'age': age, 'course': course, 'scores': scores})
    save_data(students)
    print("Talaba qo‘shildi!")


def get_students():
    students = load_data()
    for s in students:
        print(f"{s['name']} | Yoshi: {s['age']} | Kurs: {s['course']} | Ballari: {s['scores']}")


add_student()
get_students()

# 2. Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent)
# and print relevant information (temperature, humidity, etc.).

"""
# Misol uchun quyidagi openweathermap.org portalidagi mening API_KEY-im va shahrim:
# API_KEY = '82855aedd44183253e6730d128816870'
# CITY = "Tashkent"
"""


def get_weather(CITY, API_KEY):
    """url-ni funksiya ichida (local) qo'llash (global-ga qaraganda) requestni tezlashtiradi (IMHO)"""
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        data = response.json()
        print(f"Shahar: {data['name']}")
        print(f"Harorat: {data['main']['temp']}°C")
        print(f"Namlik: {data['main']['humidity']}%")
        print(f"Bosim: {data['main']['pressure']} hPa")
        print(f"Ob-havo: {data['weather'][0]['description']}")
    else:
        print(f"Serverdan {response.status_code} xatolik qaydi")
        print({response.text})


get_weather("Tashkent", '82855aedd44183253e6730d128816870')
print()
get_weather("Baku", '82855aedd44183253e6730d128816870')
print()
get_weather("Pekin", '82855aedd44183253e6730d128816870')
print()
get_weather("Amsterdam", '82855aedd44183253e6730d128816870')

# 3. Task: JSON Modification
# Write a program that allows users to add new books, update existing book information,
# and delete books from the books.json JSON file.
FILENAME = "books.json"


def load_data():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return []
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=3)


def add_book():
    books = load_data()
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = input("Yili: ")
    books.append({"title": title, "author": author, "year": year})
    save_data(books)
    print("Kitob qo‘shildi!")


def update_book():
    books = load_data()
    title = input("Yangilamoqchi bo‘lgan kitob nomini kiriting: ")
    for book in books:
        if book["title"].lower() == title.lower():
            print("Yangi ma'lumotlarni kiriting (bo‘sh qoldirilsa, eski qiymat saqlanadi):")
            new_title = input(f"Yangi nomi [{book['title']}]: ") or book["title"]
            new_author = input(f"Yangi muallif [{book['author']}]: ") or book["author"]
            new_year = input(f"Yangi yili [{book['year']}]: ") or book["year"]
            book.update({"title": new_title, "author": new_author, "year": new_year})
            save_data(books)
            print("Kitob yangilandi!")
            return
    print("Bunday nomdagi kitob topilmadi!")


def delete_book():
    books = load_data()
    title = input("O‘chirmoqchi bo‘lgan kitob nomini kiriting: ")
    new_books = [book for book in books if book["title"].lower() != title.lower()]
    if len(new_books) != len(books):
        save_data(new_books)
        print("Kitob o‘chirildi!")
    else:
        print("Bunday nomdagi kitob topilmadi!")


def show_books():
    books = load_data()
    if not books:
        print("Kitoblar ro‘yxati bo‘sh.")
        return
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book['title']} | {book['author']} | {book['year']}")


def main():
    while True:
        print("\n=== Kitoblar bazasi ===")
        print("1. Kitob qo‘shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o‘chirish")
        print("4. Barcha kitoblarni ko‘rish")
        print("5. Chiqish")

        choice = input("Tanlang (1-5): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            print("Dastur tugadi.")
            break
        else:
            print("Noto‘g‘ri tanlov! 1 dan 5 gacha son kiriting.")


if __name__ == "__main__":
    main()

# 4. Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.

import random

API_KEY = "8828b08e"  # OMDb API saytidan olingan api_key'im
URL = "http://www.omdbapi.com/"


def get_movies_by_genre(genre):
    # OMDb API bepul versiyada to‘g‘ridan-to‘g‘ri janr bo‘yicha qidirish imkoniyati cheklangan,
    # shuning uchun oldindan mashhur so‘zlar bilan qidiruv qilamiz
    sample_search_terms = ["love", "war", "life", "man", "woman", "dark", "light", "king", "city", "dream"]
    search_term = random.choice(sample_search_terms)
    params = {
        "apikey": API_KEY,
        "s": search_term,
        "type": "movie"
    }
    response = requests.get(URL, params=params)
    if response.status_code != 200:
        print("Xatolik yuz berdi!")
        return []
    data = response.json()
    if "Search" not in data:
        return []
    movies = []
    for item in data["Search"]:
        imdb_id = item["imdbID"]
        details = requests.get(URL, params={"apikey": API_KEY, "i": imdb_id}).json()
        if "Genre" in details and genre.lower() in details["Genre"].lower():
            movies.append(details)
    return movies


def recommend_movie():
    genre = input("Qaysi janrdagi filmni xohlaysiz (masalan: Action, Comedy, Drama): ").strip()
    movies = get_movies_by_genre(genre)
    if not movies:
        print("Bu janrda film topilmadi. Boshqa janr kiriting.")
        return
    movie = random.choice(movies)
    print("\nTavsiya etilgan film:")
    print(f"Nomi: {movie['Title']}")
    print(f"Yili: {movie['Year']}")
    print(f"Janr: {movie['Genre']}")
    print(f"IMDB reytingi: {movie.get('imdbRating', 'Noma’lum')}")
    print(f"Qisqacha mazmuni: {movie.get('Plot', 'Mavjud emas')}")


if __name__ == "__main__":
    recommend_movie()
