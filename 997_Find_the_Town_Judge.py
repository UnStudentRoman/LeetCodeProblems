def findJudge(n, trust):
    #   Check if Judge trusts anybody. If so there is no Judge.
    trusting_people = set([item[0] for item in trust])
    possible_judges = list(set(range(1, n+1)) - trusting_people)
    if possible_judges is None or len(possible_judges) > 1:
        return -1
    #   Check if all other persons trust n.
    for possible_judge in possible_judges:
        trust_count = 0
        for person in trusting_people:
            if [person, possible_judge] in trust:
                trust_count += 1
        if trust_count == len(trusting_people):
            return possible_judge
    return -1


if __name__ == '__main__':
    n = 4
    trust = [[1,3],[1,4],[2,3]]
    print(findJudge(n, trust))
