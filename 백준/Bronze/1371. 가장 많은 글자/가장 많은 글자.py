import sys



max = 0
max_idx=0


arr = [0 for i in range(26)]



for str in sys.stdin.read():
    if 97 <= ord(str):
        if ord(str) <= 122 : # i가 97~122 즉 a~z인경우 , a는 아스키코드로 97 , z는 122
            arr[ord(str)-97]+=1 # 갯수 하나 더해줌


for i in range(26):
    if max <= arr[i]:
        max_idx = i
        max = arr[i]
for i in range(26):
    if arr[i]==max:
        print(chr(i+97),end='')