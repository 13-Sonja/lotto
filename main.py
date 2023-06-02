from sys import exit
from silvester import play_silvester
from lotto import play_lotto


while True:
    game = input(
        "Willkommen in der Glücksspielzentrale! Wollen Sie Lose für die Silvestermillionen (1) oder Spiel 6 aus 49 (2) kaufen oder wieder gehen (0)? "
    )
    if game == "1":
        play_silvester()
    elif game == "2":
        play_lotto()
    elif game == "0":
        exit("Weise Entscheidung. Beim Glücksspiel kann man nur verlieren.")
    else:
        print("Ungültige Eingabe. Bitte 1, 2 oder 0 auswählen.")
        continue


if __name__ == "__main__":
    main()
