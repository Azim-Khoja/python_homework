# 1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import date, datetime

try:
    # Foydalanuvchidan tug‘ilgan sanani olish
    birth_date_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")

    # Stringni datetime formatiga o‘tkazamiz
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()

    # Bugungi sana
    today = date.today()

    # Farqni hisoblash
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Manfiy kun yoki oy chiqsa, to‘g‘rilash
    if days < 0:
        months -= 1
        prev_month = today.month - 1 if today.month > 1 else 12
        prev_year = today.year if today.month > 1 else today.year - 1
        # Oldingi oydagi kunlar sonini topamiz
        if prev_month == 12:
            days_in_prev_month = 31
        else:
            days_in_prev_month = (date(prev_year, prev_month + 1, 1) - date(prev_year, prev_month, 1)).days
        days += days_in_prev_month

    if months < 0:
        years -= 1
        months += 12

    # Natija
    print(f"Sizning yoshingiz: {years} da")

except ValueError:
    print("Iltimos, sanani to‘g‘ri formatda kiriting! (masalan: 2000-05-21)")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import date, datetime

try:
    # Foydalanuvchidan tug‘ilgan sanani olish
    birth_date_str = input("Tug‘ilgan sanangizni kiriting (YYYY-MM-DD): ")

    # Stringni datetime formatiga o‘tkazamiz
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
    today = date.today()

    # Keyingi tug‘ilgan kun sanasini aniqlaymiz
    next_birthday = date(today.year, birth_date.month, birth_date.day)

    # Agar bu yilgi tug‘ilgan kun o‘tgan bo‘lsa, keyingi yilni olamiz
    if next_birthday < today:
        next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

    # Farqni hisoblaymiz
    days_until_birthday = (next_birthday - today).days

    # Natija
    print(f"Sizning keyingi tug‘ilgan kuningizgacha {days_until_birthday} kun qoldi.")

except ValueError:
    print("Iltimos, sanani to‘g‘ri formatda kiriting! (masalan: 2000-05-21)")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 3.Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

try:
    # Joriy sana va vaqtni olish
    current_str = input("Joriy sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    current_datetime = datetime.strptime(current_str, "%Y-%m-%d %H:%M")

    # Uchrashuv davomiyligini olish
    hours = int(input("Uchrashuv davomiyligini kiriting (soatlarda): "))
    minutes = int(input("Qo‘shimcha daqiqalarni kiriting: "))

    # Tugash vaqtini hisoblash
    duration = timedelta(hours=hours, minutes=minutes)
    end_time = current_datetime + duration

    # Natijani chiqarish
    print(f"Uchrashuv tugash vaqti: {end_time.strftime('%Y-%m-%d %H:%M')}")

except ValueError:
    print("Iltimos, sanani va vaqtni to‘g‘ri formatda kiriting! (masalan: 2025-10-16 14:30)")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 4. Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.

from datetime import datetime
import pytz

try:
    # Foydalanuvchidan ma'lumotlarni olish
    date_str = input("Sana va vaqtni kiriting (YYYY-MM-DD HH:MM): ")
    from_tz_str = input("Joriy vaqt mintaqangizni kiriting (masalan: Asia/Tashkent): ")
    to_tz_str = input("Qaysi mintaqaga o‘tkazmoqchisiz? (masalan: Europe/London): ")

    # Kiritilgan sanani datetime obyektiga aylantirish
    naive_datetime = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    # Joriy va maqsadli vaqt zonalarini olish
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)

    # Sana va vaqtni joriy mintaqaga biriktirish
    local_datetime = from_tz.localize(naive_datetime)

    # Maqsadli mintaqaga o‘tkazish
    converted_datetime = local_datetime.astimezone(to_tz)

    # Natijani chiqarish
    print(f"{from_tz_str} vaqti bo‘yicha: {local_datetime.strftime('%Y-%m-%d %H:%M')}")
    print(f"{to_tz_str} vaqti bo‘yicha: {converted_datetime.strftime('%Y-%m-%d %H:%M')}")

except pytz.UnknownTimeZoneError:
    print("Kiritilgan vaqt mintaqasi noto‘g‘ri. Masalan: Asia/Tashkent yoki Europe/London deb kiriting.")

except ValueError:
    print("Iltimos, sanani va vaqtni to‘g‘ri formatda kiriting! (masalan: 2025-10-16 14:30)")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 5. Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).

from datetime import datetime
import time

try:
    # Foydalanuvchidan kelajakdagi sana va vaqtni olish
    target_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")
    target_time = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

    print("Taymer boshlandi...\n")

    while True:
        now = datetime.now()
        remaining = target_time - now

        if remaining.total_seconds() <= 0:
            print("Vaqt tugadi!")
            break

        # Qolgan vaqtni soat, daqiqa, soniya ko‘rinishida ajratish
        days = remaining.days
        hours, remainder = divmod(remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Qolgan vaqt: {days} kun, {hours:02d}:{minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

except ValueError:
    print("Iltimos, sanani to‘g‘ri formatda kiriting! (masalan: 2025-10-16 18:00:00)")

except KeyboardInterrupt:
    print("\nTaymer to‘xtatildi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

try:
    # Foydalanuvchidan email manzilini olish
    email = input("Email manzilingizni kiriting: ")

    # Email formatini tekshirish uchun regex andoza
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Tekshirish
    if re.match(pattern, email):
        print("Email manzil to‘g‘ri formatda kiritilgan.")
    else:
        print("Email manzil noto‘g‘ri formatda. Iltimos, qaytadan tekshirib kiriting.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 7.Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

import re

try:
    # Foydalanuvchidan raqamni olish
    phone = input("Telefon raqamingizni kiriting (faqat raqamlar, masalan: 998123456789): ")
    # phone = '998335447040'
    # Faqat raqamlarni ajratib olish
    digits = re.sub(r"\D", "", phone)

    # Tekshirish — 10 ta raqam bo‘lishi kerak
    if (len(digits) == 12) and (digits.startswith('998')):
        formatted = f"(+{digits[0:3]})-{digits[3:5]}-{digits[5:8]}-{digits[8:10]}-{digits[10:]}"
        print(f"Formatlangan raqam: {formatted}")
        # else:
        # print("Xato: 998 bilan boshlanishi kerak!")
    else:
        print("Xato: Telefon raqam 12 ta raqamdan iborat bo‘lishi va 998 bilan boshlanishi kerak kerak.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 8. Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).

import re

try:
    # Foydalanuvchidan parolni olish
    password = input("Parolingizni kiriting: ")

    # Mezonga moslikni tekshirish
    length_ok = len(password) >= 8
    upper_ok = re.search(r"[A-Z]", password) is not None
    lower_ok = re.search(r"[a-z]", password) is not None
    digit_ok = re.search(r"\d", password) is not None
    special_ok = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    # Natijani baholash
    if all([length_ok, upper_ok, lower_ok, digit_ok, special_ok]):
        print("Parol mustahkam (Strong).")
    else:
        print("Parol zaif. Quyidagilarni tekshiring:")
        if not length_ok:
            print("- Kamida 8 ta belgidan iborat bo‘lishi kerak.")
        if not upper_ok:
            print("- Kamida bitta katta harf bo‘lishi kerak.")
        if not lower_ok:
            print("- Kamida bitta kichik harf bo‘lishi kerak.")
        if not digit_ok:
            print("- Kamida bitta raqam bo‘lishi kerak.")
        if not special_ok:
            print("- Kamida bitta maxsus belgi (!@#$%^&*) bo‘lishi kerak.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

try:
    # Namunaviy matn
    text = """Python kuchli dasturlash tillaridan biri.
    Ko'p dasturchilar Pythonni sevishadi, chunki bu til o'qish va o'rganish uchun oson."""

    # Foydalanuvchidan so‘z kiritish
    word = input("Qaysi so‘zni izlamoqchisiz? ")

    # So‘zni qidirish (case-insensitive)
    matches = [m.start() for m in re.finditer(rf"\b{re.escape(word)}\b", text, re.IGNORECASE)]

    if matches:
        print(f"'{word}' so‘zi {len(matches)} marta topildi.")
        print("Topilgan joylari (indekslar):", matches)
    else:
        print(f"'{word}' so‘zi matnda topilmadi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")

# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

print("Matnda sanalar bor/yo'qligini tekshirish")
try:
    # Foydalanuvchidan matn olish
    text = input("Matnni kiriting: ")

    # Turli sana formatlarini aniqlash uchun regex andozalar
    date_patterns = [
        r"\b\d{4}-\d{2}-\d{2}\b",  # YYYY-MM-DD
        r"\b\d{2}/\d{2}/\d{4}\b",  # DD/MM/YYYY
        r"\b\d{2}-\d{2}-\d{4}\b",  # DD-MM-YYYY
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{1,2},\s*\d{4}\b"  # Month DD, YYYY
    ]

    # Barcha mosliklarni topish
    dates = []
    for pattern in date_patterns:
        matches = re.findall(pattern, text)
        dates.extend(matches)

    # Natijani chiqarish
    if dates:
        print("Matnda topilgan sanalar:")
        for d in dates:
            print("-", d)
    else:
        print("Matnda hech qanday sana topilmadi.")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")
