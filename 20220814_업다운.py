정답 = 18
while True:
    a = int(input("입력:"))
    if a < 정답:
        print('업')
    if a > 정답:
        print('다운')
    if a == 정답:
        print('정답')
        break