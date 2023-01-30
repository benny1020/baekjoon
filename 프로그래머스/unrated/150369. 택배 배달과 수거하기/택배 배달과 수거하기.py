def solution(cap, n, deliveries, pickups):
    targetDeliver = n - 1
    targetPickup = n - 1
    distance = 0

    while pickups[targetPickup] == 0:
        targetPickup -= 1
        if targetPickup == -1:
            break

    while deliveries[targetDeliver] == 0:
        targetDeliver -= 1
        if targetDeliver == -1:
            break
    # 1 0 3 1 2    0 3 0 4 0
    # 1 0 2 0 0    0 3 0 0 0 10
    # 0 0 0 0 0
    # 1 0 2 0, 0 3 0 4  10
    # 0 0 0 0, 0 3 0 0

    while not (targetDeliver == -1 and targetPickup == -1):
        # deliver 처리
        curDeliverCap = cap
        distance += (max(targetDeliver, targetPickup)+1)* 2

        # 뒤에서부터 찾고
        for i in reversed(range(targetDeliver + 1)):
            if deliveries[i] < curDeliverCap:
                curDeliverCap -= deliveries[i]
                deliveries[i] = 0
                if i == 0:
                    targetDeliver= -1
            else:
                deliveries[i] -= curDeliverCap
                curDeliverCap = 0
                while deliveries[i] == 0:
                    i -= 1
                    if i == -1:
                        break
                targetDeliver = i
                break

        # pickup 처리
        curPickupCap = cap

        # 뒤에서부터 찾고
        for i in reversed(range(targetPickup + 1)):

            if pickups[i] < curPickupCap:
                curPickupCap -= pickups[i]
                pickups[i] = 0
                if i == 0:
                    targetPickup = -1

            else: #pickups[i] >= curPickupCap
                pickups[i] -= curPickupCap
                curPickupCap = 0
                while pickups[i] == 0:
                    i -= 1
                    if i == -1:
                        break
                targetPickup = i
                break
        #print(curDeliverCap, curPickupCap)
    return distance