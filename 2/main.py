def is_prime_number(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False

    return True


def is_palindrome(text):
    return text[::-1] == text


def is_palindrome_and_prime(number):
    if not number.isnumeric():
        print("invalid input")
        return

    number = int(number) + 1

    while True:
        if is_palindrome(str(number)) and is_prime_number(number):
            print(number)
            break

        number += 1


user_input = input("Napis cislo: ")
is_palindrome_and_prime(user_input)
