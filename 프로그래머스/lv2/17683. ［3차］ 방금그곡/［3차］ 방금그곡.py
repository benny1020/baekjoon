
def getDiff(start, end):
    start_hours, start_minutes = map(int,start.split(':'))
    end_hours, end_minutes = map(int,end.split(':'))
    
    start_minutes += start_hours*60
    end_minutes += end_hours*60
    
    return end_minutes - start_minutes

def getRecord(melody, minutes):
    record = []
    for i in range(minutes):
        record.append(melody[i%len(melody)])
    return record

def getMelody(music):
    melody = []
    tmp = ""
    for i in range(len(music)):
        if music[i] =='#':
            melody.append(tmp + '#')
            tmp = ""
        else:
            if tmp != "":
                melody.append(tmp)
            tmp = music[i]
                
    if tmp != "":
        melody.append(tmp)
    return melody
        
    
        

def solution(m, musicinfos):  
 #'

    ans = ["",0]
    m = getMelody(m)
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(',')
        diff = getDiff(start, end)
        melody = getMelody(music)
        record = getRecord(melody, diff)
        for i in range(len(record)-len(m)+1):
            if record[i:i+len(m)] == m:
                if ans[1] < diff:
                    ans[0] = title
                    ans[1] = diff
                    break
    if ans[0] == "":
        return "(None)"
    else:
        return ans[0]
        

        