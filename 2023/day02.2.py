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
    max_red = 0
    max_green = 0
    max_blue = 0
    for reveal in games[game]:
        for hand in reveal:
            if hand[1] == 'red' and hand[0]>max_red:
                max_red = hand[0]
            elif hand[1] == 'green' and hand[0]>max_green:
                max_green = hand[0]
            elif hand[1] == 'blue' and hand[0]>max_blue:
                max_blue = hand[0]
    game_power = max_red * max_green * max_blue
    res += game_power

print(f"{res=}")