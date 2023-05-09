def rps_game_winner(turns):
    if len(turns) != 2:
        raise Exception("WrongNumberOfPlayersError")
    elif turns[0][1] not in "RPS" or turns[1][1] not in "RPS":
        raise Exception("NoSuchStrategyError")
    p2win = ["SR", "PS", "RP"]
    if turns[0][1] + turns[1][1] in p2win:
        return " ".join(turns[1])
    else:
        return " ".join(turns[0])

