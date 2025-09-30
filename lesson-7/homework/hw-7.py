# 1. is_prime(n) funksiyasi
# is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

# Misollar:
# Kiritish:
# 4
# Natija:
# False
# (Izoh: 4 soni tub emas, chunki u 2 ga bo'linadi.)

# Kiritish:
# 7
# Natija:
# True
# (Izoh: 7 soni faqat 1 va o'ziga bo'linadi, ya'ni tub son.)

def is_prime(n):
    """
    n soni tub bo'lsa True, aks holda False qaytaradi.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # faqat toq bo'luvchilarni tekshiramiz
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Example:
print(is_prime(4))  # False
print(is_prime(7))  # True


# digit_sum(k) funksiyasi
# digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

# Misollar:
# Kiritish:
# 24
# Natija:
# 6
# (Izoh: 24 sonining raqamlari yig'indisi: 2 + 4 = 6.)

# Kiritish:
# 502
# Natija:
# 7
# (Izoh: 502 sonining raqamlari yig'indisi: 5 + 0 + 2 = 7.)

# case-1:
def digit_sum1(k):
    total = 0
    for x in str(k):
        total += int(x)

    return total


# case-2:
def digit_sum2(k):
    return sum(int(x) for x in str(k))


print("Kiritilgan sonlarning yiğindisi:", digit_sum1(123))
print("Kiritilgan sonlarning yiğindisi:", digit_sum2(456))


# 3. Ikki sonning darajalari
# Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni)
# chop etuvchi funksiyani yozing.

# Misol:
# Kiritish:
# 10
# Natija:
# 2 4 8
# (Izoh: 10 dan kichik yoki teng bo'lgan 2 ning darajalari: 2, 4, 8.)

def pow(n):
    k = 1
    while 2 ** k <= n:
        print(2 ** k, end=" ")
        k += 1
    return k


print(pow(10))
print(pow(100))