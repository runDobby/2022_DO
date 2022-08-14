정답 = '123'
j=0
while True:
    a = int(input("입력:"))
    for i in range(0, 2):
        if(a[i])==(정답[i]):
            j = j+1
    print(f"{j} 스트라이크 {3-j} 아웃")
    j=0
    if a == 123:
        print('정답')
        break