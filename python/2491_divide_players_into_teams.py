def dividePlayers(skill):
    team_pool = sorted(skill)
    team_skill = 2*sum(skill)/len(skill)
    teams = []
    
    while team_pool:
        member1 = team_pool[0]
        required_skill = team_skill - member1
        team_pool.remove(member1)
        if required_skill not in team_pool: return -1
        member2_index = team_pool.index(required_skill)
        member2 = team_pool[member2_index]
        team_pool.remove(member2)
        teams.append((member1,member2))
    
    return sum(k[0]*k[1] for k in teams)



#print(dividePlayers([3,2,5,1,3,4]))
print(dividePlayers([3,4]))