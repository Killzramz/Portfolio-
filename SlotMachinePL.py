import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def spin_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("Ile chcesz wpłacić? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Kwota wpłacenia musi byc wieksza niż 0.")
        else:
            print("Prosze podac kwote w cyfrach kurwa i tylko!.")

    return amount


def number_of_lines():
    while True:
        lines = input(
            "Na ile lini chcesz obstawić : (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Podaj dostępną liczbe lini.")
        else:
            print("Prosze podac numer! (cyfra).")

    return lines


def get_bet():
    while True:
        amount = input("Ile chcesz postawić na każdą z lini? 1 - 100$: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Kwota musi sie miescić w przedziale: ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Prosze podac liczbę!.")

    return amount


def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"Masz za mało mamonki! Twój balans wynosi!: ${balance}")
        else:
            break

    print(
        f"Postawiłeś ${bet} na {lines} linie. Całkowity bet to: ${total_bet}")

    slots = spin_machine(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    if winnings > 0:
        print(f"Wygrałeś! ${winnings}.")
        print(f"Szczęśliwe linie:", *winning_lines)
    else:
        print('PUDŁO!')

    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Aktualny stan konta ${balance}")
        answer = input("Naciśnij ENTER aby kontynuować (q aby wyjść).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"Wychodzisz z ${balance}")

main()



