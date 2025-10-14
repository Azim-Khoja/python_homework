# Exercise 1: Threaded Prime Number Checker

# Write a Python program that checks whether a given range of numbers contains prime numbers.
# Divide the range among multiple threads to parallelize the prime checking process.
# Each thread should be responsible for checking a subset of the range, and the main program should print the list of prime numbers found.

import threading

# --- Prime check function ---
def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# --- Thread worker function ---
def check_primes_in_range(start, end, result_list):
    """Check primes in the given range and append to shared result_list."""
    for num in range(start, end):
        if is_prime(num):
            result_list.append(num)


# --- Main Program ---
def threaded_prime_checker(start, end, num_threads=4):
    """Divide the range and use multiple threads to find primes."""
    threads = []
    result = []

    # Step size per thread
    step = (end - start) // num_threads

    for i in range(num_threads):
        range_start = start + i * step
        # last thread takes the remainder range
        range_end = end if i == num_threads - 1 else range_start + step

        thread = threading.Thread(target=check_primes_in_range, args=(range_start, range_end, result))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    # Sort result before returning (since threads work in parallel)
    result.sort()
    return result


# --- Run the program ---
if __name__ == "__main__":
    start_range = 1
    end_range = 100

    primes = threaded_prime_checker(start_range, end_range, num_threads=4)

    print(f"Prime numbers between {start_range} and {end_range}:")
    print(primes)

# Exercise 2: Threaded File Processing

# Write a program that reads a large text file containing lines of text.
# Implement a threaded solution to count the occurrence of each word in the file.
# Each thread should process a portion of the file, and the main program should display a summary of word occurrences across all threads.

import threading
from collections import Counter

# --- Thread function ---
def count_words(lines, result_list):
    """Count word occurrences in given lines and append result to shared list."""
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result_list.append(word_count)


# --- Main threaded file processor ---
def threaded_word_count(file_path, num_threads=4):
    """Count words in a file using multiple threads."""
    # Fayldan barcha satrlarni o‘qish
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads

    threads = []
    results = []

    # Har bir thread uchun satrlar oralig‘ini bo‘lish
    for i in range(num_threads):
        start = i * step
        end = total_lines if i == num_threads - 1 else start + step
        thread = threading.Thread(target=count_words, args=(lines[start:end], results))
        threads.append(thread)
        thread.start()

    # Barcha thread’larni kutish
    for t in threads:
        t.join()

    # Natijalarni birlashtirish
    final_count = Counter()
    for partial_result in results:
        final_count.update(partial_result)

    return final_count


# --- Run the program ---
if __name__ == "__main__":
    file_name = "large_text.txt"  # Fayl nomi (katta fayl bo‘lishi mumkin)

    result = threaded_word_count(file_name, num_threads=4)

    print("\nTop 10 most common words:")
    for word, count in result.most_common(10):
        print(f"{word}: {count}")