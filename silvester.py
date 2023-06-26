from random import shuffle, sample

# constants
TICKETS = list(range(1, 1750001))
PRICE = 10
WINNINGS = {"class_1": 1000000, "class_2": 100000, "class_3": 1000, "class_4": 10}


# main game process with input validation
def play_silvester():
    shuffle(TICKETS)
    while True:
        my_tickets_amount = input_validation(
            input("Wieviele Lose für die Silvestermillionen wollen Sie kaufen: ")
        )
        if my_tickets_amount:
            break
    my_tickets = sample(TICKETS, my_tickets_amount)
    won = calculate_winnings(drawing(TICKETS), my_tickets)
    print(
        f"Sie haben {my_tickets_amount} Lose für insgesamt",
        my_tickets_amount * PRICE,
        "Euro gekauft.",
    )
    print(f"Sie haben {won} Euro gewonnen.")


# randomly drawing the winning tickets, avoiding duplicates
def drawing(TICKETS):
    class_1 = sample(TICKETS, 7)
    remaining_tickets = [item for item in TICKETS if item not in class_1]
    class_2 = sample(remaining_tickets, 7)
    remaining_tickets = [item for item in remaining_tickets if item not in class_2]
    class_3 = sample(remaining_tickets, 1750)
    class_4 = sample(range(1, 100), 6)
    return [class_1, class_2, class_3, class_4]


# calculate winnings of players tickets
def calculate_winnings(draws, my_tickets):
    won = 0
    for ticket in my_tickets:
        if ticket in draws[0]:
            won += WINNINGS["class_1"]
        elif ticket in draws[1]:
            won += WINNINGS["class_2"]
        elif ticket in draws[2]:
            won += WINNINGS["class_3"]
        if int(str(ticket)[-2:]) in draws[3]:
            won += WINNINGS["class_4"]
    return won


def input_validation(my_tickets_amount):
    if not my_tickets_amount.isdigit():
        print(
            f"Ungültige Eingabe. Bitte eine Zahl zwischen 1 und {max(TICKETS)} eingeben."
        )
        return False
    elif min(TICKETS) > int(my_tickets_amount) or int(my_tickets_amount) > max(TICKETS):
        print(
            f"Ungültige Anzahl. Bitte eine Zahl zwischen 1 und {max(TICKETS)} eingeben."
        )
        return False
    else:
        return int(my_tickets_amount)
