def minimumCardPickup(cards):
    cases = []
    numbers = []
    if len(cards)==len(set(cards)): return -1
    for i in range(len(cards)):
        focused_list = cards[:i]+cards[i+1:]
        if cards[i] in focused_list:
            if cards[i] in numbers: continue
            else:
                cases.append(len(cards[i:focused_list.index(cards[i])+2]))
                numbers.append(cards[i])
    if cases: return min([i for i in cases if i!=0])
    else: return -1