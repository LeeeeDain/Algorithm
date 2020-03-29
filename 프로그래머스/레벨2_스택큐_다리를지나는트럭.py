def solution(bridge_length, weight, truck_weights):
    time = 0
    arrival = 0
    total_weights = 0
    n = len(truck_weights)
    trucks = truck_weights
    now = []
    del_item = -1

    while arrival < n:
        for i in now:
            if i[1] == bridge_length:
                del_item = i
                arrival += 1
                total_weights -= i[0]
            else:
                i[1] += 1

        if del_item != -1:
            now.remove(del_item)
            del_item = -1

        if len(trucks) > 0:
            if trucks[0]+total_weights <= weight and len(now)+1 <= bridge_length:
                now.append([trucks[0],1])
                total_weights += trucks.pop(0)
        time += 1

    return time
