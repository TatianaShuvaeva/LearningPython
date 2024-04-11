import os

ordnerpfad = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
print('ordner: ' + ordnerpfad)

path_to_file = os.path.join(ordnerpfad, 'daten.txt')
print(path_to_file)

file_input = open(path_to_file)
metadaten = {}
line_number = 1
games = ''
for line in file_input:
    if line_number < 10:
        line_neu = line.strip('][\n')
        line_split = line_neu.split(' ', maxsplit=1)
        key = line_split[0]
        value = line_split[1].strip('"')
        metadaten[key] = value
    elif line_number > 10:
        print(line)
        games += line

    line_number += 1

# games = '1.e4 c6 2.d4 d5 3.Nc3 dxe4 4.Nxe4 Nd7 5.Ng5 Ngf6 6.Bd3 e6 7.N1f3 h6 8.Nxe6 Qe7 9.O-O fxe6 10.Bg6+ Kd8 {Kasparov schüttelt kurz den Kopf} 11.Bf4 b5 12.a4 Bb7 13.Re1 Nd5 14.Bg3 Kc8 15.axb5 cxb5 16.Qd3 Bc6 17.Bf5 exf5 18.Rxe7 Bxe7 19.c4 1-0'
# games_split = games.split(' ')
# games_split =   ['1.e4', 'c6', '2.d4', 'd5', '3.Nc3', 'dxe4', '4.Nxe4', 'Nd7', '5.Ng5', 'Ngf6', '6.Bd3', 'e6', '7.N1f3', 'h6', '8.Nxe6', 'Qe7', '9.O-O', 'fxe6', '10.Bg6+', 'Kd8', '{Kasparov', 'schüttelt', 'kurz', 'den', 'Kopf}', '11.Bf4', 'b5', '12.a4', 'Bb7', '13.Re1', 'Nd5', '14.Bg3', 'Kc8', '15.axb5', 'cxb5', '16.Qd3', 'Bc6', '17.Bf5', 'exf5', '18.Rxe7', 'Bxe7', '19.c4', '1-0']
# 'A'.isdigit()
# games_refined = ['1.e4', 'c6', '2.d4', 'd5', '3.Nc3', 'dxe4', '4.Nxe4', 'Nd7', '5.Ng5', 'Ngf6', '6.Bd3', 'e6', '7.N1f3', 'h6', '8.Nxe6', 'Qe7', '9.O-O', 'fxe6', '10.Bg6+', 'Kd8', '{Kasparov', 'schüttelt', 'kurz', 'den', 'Kopf}', '11.Bf4', 'b5', '12.a4', 'Bb7', '13.Re1', 'Nd5', '14.Bg3', 'Kc8', '15.axb5', 'cxb5', '16.Qd3', 'Bc6', '17.Bf5', 'exf5', '18.Rxe7', 'Bxe7', '19.c4']
# >>> '1.e4'.split('.')
# ['1', 'e4']
# >>> 'c6'.split('.')
# ['c6']
games_result = ['e4']
# print(metadaten)

