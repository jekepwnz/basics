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




#
#rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #=> WrongNumberOfPlayersError
#rps_game_winner([['player1', 'P'], ['player2', 'A']]) #=> NoSuchStrategyError
# rps_game_winner([['player1', 'P'], ['player2', 'S']]) #=> 'player2 S'
# print(rps_game_winner([['player1', 'P'], ['player2', 'S']])) #=> 'player2 S'
# rps_game_winner([['player1', 'P'], ['player2', 'P']]) #=> 'player1 P'
# print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'