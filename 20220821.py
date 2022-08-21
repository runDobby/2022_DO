# a = input('차량번호를 입력하세요>>>')
#
# print(f'서울{a}의 차량번호 4자리는",a[-4:])
#
#
#
#
# a = int(input('10~99 사이의 정수를 입력하세요>>>'))
#
# if a>99:
#     print('10~99 사이의 정수를 입력하세요')
# elif a<10:
#     print('10~99 사이의 정수를 입력하세요')
# else:
#     b=a//10
#     c=a%10
#     print('십의 자리:{}'.format(b))
#     print('일의 자리:{}'.format(c))
#
#
# 입력= int(input("초를 입력하세요>>>"))
#
# 시간 = 입력 //3600
# 분 = (입력%3600) // 60
# 초 = 입력 % 60
#
# print("변환 결과는 {}시간 {}분 {}초입니다.".format(시간,분,초))
#
#
# i=0
# while i<=100:
#     if i%7==0:
#         print(i)
#     i += 1
#
#
# a=int(input('자판기에 얼마를 넣을까요 >>>'))
# i=1
# while True:
#     print('커피 {}잔, 잔돈{}원'.format(i,a-(i*300)))
#     i += 1
#     if a<i*300:
#         break
#
#
# b=1
# while b<10:
#     a = 2
#     while a<10:
#         print('{}X{}={} '.format(a,b,a*b),end='\t')
#         a += 1
#     print('')
#     b+=1
#
#
# a=int(input('임의의 양수를 입력하세요 >>> '))
# b=0
# for i in range(1,a+1):
#     b=b+i
# print('1부터 {}사이 모든 정수의 합계는 {}입니다.'.format(a,b))
#
#
#
# for i in range(2,10):
#     for j in range(1, i+1):
#         if i%2==1:
#             print('{}X{}={}'.format(i,j,i*j))
#     if i % 2 == 1:
#         print('')
#
#
# for i in range(2,10):  # continue문은 반복문 즉시 복귀를 담당한다.
#     for j in range(1, i+1):
#         if i%2==0:
#             continue
#         print('{}X{}={}'.format(i,j,i*j))
#     if i % 2 == 1:
#         print('')