def validate_row(items, i):
    if len(items) != 4:
        print("ERROR: " + str(len(items)) + " columns on line " + str(i + 1))
        return

    if items[0] == "":
        print("Missing title on line " + str(i + 1))

    if items[1] == "":
        print("Missing author on line " + str(i + 1))

    isbn = items[2]
    if not is_isbn_valid(isbn):
        print("Invalid ISBN on line " + str(i + 1))

    price = items[3]
    if not is_price_valid(price):
        print("Invalid price on line " + str(i + 1))


def is_price_valid(price):
    if len(price) == 0 or price[0] == "-":
        return False

    price = price.strip()
    price_split = price.split(" ")
    if len(price_split) == 1:
        if "€" in price_split[0] or "Kč" in price_split[0]:
            if "€" in price_split[0]:
                price_only = price_split[0][0:-1]
            else:
                price_only = price_split[0][0:-2]
        else:
            return False
    elif len(price_split) == 2:
        if "€" in price_split[1] or "Kč" in price_split[1]:
            price_only = price_split[0]
        else:
            return False
    else:
        return False

    return "." in price_only or "," in price_only


# https://compucademy.net/python-programming-challenge-validate-isbn-10-number/
def is_isbn_valid(isbn):
    if len(isbn) != 10:
        return False

    result = 0

    # Iterate through code_string
    for i in range(9):
        # for each character, multiply by a different decreasing number: 10 - x
        result = result + int(isbn[i]) * (10 - i)

    # Handle last character
    if isbn[9].lower() == "x":
        result += 10
    else:
        result += int(isbn[9])

    # Return whether the isbn is valid
    if result % 11 == 0:
        return True
    else:
        return False


with open('input.txt', encoding='UTF-8') as f:
    for i, line in enumerate(f):
        line = line.rstrip()
        row_items = line.split(';')
        validate_row(row_items, i)
