games_result = []
games_refined = ['1.e4', 'c6', '2.d4', 'd5', '3.Nc3', 'dxe4', '4.Nxe4', 'Nd7', '5.Ng5', 'Ngf6', '6.Bd3', 'e6', '7.N1f3', 'h6', '8.Nxe6', 'Qe7', '9.O-O', 'fxe6', '10.Bg6+', 'Kd8', '{Kasparov', 'schüttelt', 'kurz', 'den', 'Kopf}', '11.Bf4', 'b5', '12.a4', 'Bb7', '13.Re1', 'Nd5', '14.Bg3', 'Kc8', '15.axb5', 'cxb5', '16.Qd3', 'Bc6', '17.Bf5', 'exf5', '18.Rxe7', 'Bxe7', '19.c4']
for elem in games_refined:
    list = elem.split('.')
    if len(list) == 2:
        games_result.append(list[1])
        continue
    games_result.append(list[0])

print(games_result)