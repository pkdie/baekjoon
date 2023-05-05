def solution(players, callings):
    rank_dic = dict()
    for i, p in enumerate(players):
        rank_dic[p] = i
    for i in callings:
        passed, passing = rank_dic[i] - 1, rank_dic[i]
        rank_dic[players[passing]] = passed
        rank_dic[players[passed]] = passing
        players[passed], players[passing] = players[passing], players[passed]
        
    return players