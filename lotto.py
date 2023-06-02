from random import shuffle, sample, choice

# constants
NORMAL_NUMBERS = list(range(1, 50))
SUPERNUMBER = list(range(0, 10))
DRAWINGS_PER_YEAR = 104
MAX_TICKETS = 14
COST_PER_TICKET = 1.20
WINNINGS = {
    "6+1": 9000000,
    "6": 575000,
    "5+1": 10000,
    "5": 3300,
    "4+1": 190,
    "4": 43,
    "3+1": 21,
    "3": 11,
    "2+1": 5,
}


# main game process with input validation
def play_lotto():
    shuffle(NORMAL_NUMBERS)
    shuffle(SUPERNUMBER)

    total_winnings = 0
    while True:
        my_tickets_amount = input_validation(
            input(
                "Willkommen zum Spiel 6 aus 49! Wie viele Lose (zwischen 1-14) wollen Sie kaufen: "
            ),
            MAX_TICKETS,
        )
        if not my_tickets_amount:
            continue
        else:
            break
    while True:
        drawings_to_play = input_validation(
            input(
                "An wie vielen Ziehungen (max 104 für ein Jahr) wollen Sie teilnehmen? "
            ),
            DRAWINGS_PER_YEAR,
        )
        if not drawings_to_play:
            continue
        else:
            break
    my_tickets = [
        drawing(NORMAL_NUMBERS, SUPERNUMBER) for ticket in range(my_tickets_amount)
    ]
    for i in range(drawings_to_play):
        won = calculate_winnings(my_tickets)
        total_winnings += won
        print(
            f"Ziehung {i + 1}, Kosten: {round(my_tickets_amount * COST_PER_TICKET, 2)} €, Gewinn: {won}€"
        )
    print(
        f"Kosten gesamt: {round((my_tickets_amount * COST_PER_TICKET) * drawings_to_play, 2)} €, Gewinn gesamt: {total_winnings}€"
    )


# drawing of players numbers and winning numbers
def drawing(NORMAL_NUMBERS, SUPERNUMBER):
    drawn_numbers = sample(NORMAL_NUMBERS, k=6)
    drawn_supernumber = choice(SUPERNUMBER)
    return drawn_numbers, drawn_supernumber


# calculate players winnings per drawing
def calculate_winnings(my_tickets):
    won = 0
    normal_nums, supernum = drawing(NORMAL_NUMBERS, SUPERNUMBER)
    for ticket in my_tickets:
        a = 0
        for drawn_num, my_num in zip(normal_nums, ticket[0]):
            if drawn_num == my_num:
                a += 1
        b = int(supernum == ticket[1])
        result = f"{a}+{b}"
        if result in WINNINGS:
            won += WINNINGS[result]
    return won


# validation for several inputs
def input_validation(txt, max_amount):
    if not txt.isdigit():
        print(
            f"Ungültige Eingabe. Bitte eine Zahl zwischen 1 und {max_amount} eingeben."
        )
        return False
    elif 1 > int(txt) or int(txt) > max_amount:
        print(
            f"Ungültige Anzahl. Bitte eine Zahl zwischen 1 und {max_amount} eingeben."
        )
        return False
    else:
        return int(txt)
