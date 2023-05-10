class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass


def errors_check(turns):
    if len(turns) != 2:
        raise WrongNumberOfPlayersError()
    elif turns[0][1] not in "RPS" or turns[1][1] not in "RPS":
        raise NoSuchStrategyError()

def rps_game_winner(turns):
    try:
        errors_check(turns)
    except WrongNumberOfPlayersError:
        return "WrongNumberOfPlayersError"
    except NoSuchStrategyError:
        return "NoSuchStrategyError"

    else:
        p2win = ["SR", "PS", "RP"]
        if turns[0][1] + turns[1][1] in p2win:
            return " ".join(turns[1])
        else:
            return " ".join(turns[0])


