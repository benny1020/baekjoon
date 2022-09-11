from collections import deque
def solution(cacheSize, cities):
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
    city = deque()
    totalTime = 0
    
    if cacheSize == 0:
        return len(cities)*5
    
    
    for c in cities:
        if c in city:
            city.remove(c)
            city.append(c)
            totalTime += 1
        else:
            if len(city) >= cacheSize:
                city.popleft()
                city.append(c)
            else:
                city.append(c)
            totalTime += 5
    
    return totalTime
                    