res = 0
games = {}
with open("2023/input_files/day02") as f:
    for data in f:
        data = data.rstrip()
        game_nb = int(data.split()[1][:-1])
        games[game_nb] = []

        data = ' '.join(data.split()[2:])
        reveals = data.split(';')
        for reveal in reveals:
            hands_list = []
            hands = reveal.split(',')
            for hand in hands:
                hand = hand.strip().split()
                hands_list.append((int(hand[0]), hand[1]))
            games[game_nb].append(hands_list)

for game in games:
    exceeded = False
    for reveal in games[game]:
        for hand in reveal:
            if (
                (hand[1] == 'red' and hand[0]>12)
                or (hand[1] == 'green' and hand[0]>13)
                or (hand[1] == 'blue' and hand[0]>14)):
                exceeded = True
                break
    if not exceeded:
        res += game

print(f"{res=}")