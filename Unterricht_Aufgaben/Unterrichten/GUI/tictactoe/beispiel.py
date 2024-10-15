from Unterricht_Aufgaben.Unterrichten.GUI.tictactoe.cl_brett_ttt import TicTacToe


tic_tac_toe = TicTacToe()

result = tic_tac_toe.get()


while True:
    n = int(input("Geben Sie bitte die Feldnummer ein: "))

    try:
        tic_tac_toe.set(n)
    except Exception as ex:
        print(ex)

    for i, arr in enumerate(result):
        row = ''
        for elem in arr:
            row += elem + ' '
        print(row)


# tic_tac_toe.set(1)
