from Unterricht_Aufgaben.Unterrichten.GUI.tictactoe.cl_tic_tac_toe import TicTacToe


tic_tac_toe = TicTacToe()


result = tic_tac_toe.get()

def print_tic_tac_toe_feld(result):
    for arr in result:
        row = ''
        for elem in arr:
            row += elem + ' '
        print(row)


while True:
    print_tic_tac_toe_feld(result)
    n = int(input(f"Spieler: {tic_tac_toe.spieler_nummer} - geben Sie bitte die Feldnummer ein: "))

    try:
        tic_tac_toe.set(n)
    except Exception as ex:
        print(ex)
