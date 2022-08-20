# 조건문은
"""
python : if, elif, else
C++ : if, [elseif], else

if [조건식]:
   ...
   ...
   ...
(elif [조건식]:)
   ...
   ...
(else:)
"""

# 나이 = 15
#
# if 나이 >= 80:
#     print('노인입니다')
# if 나이 >= 20:
#     print('성인입니다')
# else:
#     print('어려요')

# 99p 1번문제, 4번문제 ~ 14:00까지

# a = int(input('점수를 입력하세요 >>>'))
#
# if a >= 90:
#     print('점수는 %d점이고, 학점은 A학점입니다.' %a)
# elif a >= 80:
#     print('점수는 %d점이고, 학점은 B학점입니다.' %a)
# elif a >= 70:
#     print('점수는 %d점이고, 학점은 C학점입니다.' %a)
# elif a >= 60:
#     print('점수는 %d점이고, 학점은 D학점입니다.' %a)
# else:
#     print('점수는 %d점이고, 학점은 F학점입니다.' %a)
# # "'{}'.format()" 사용 가능

# a = (input('차량번호를 입력하세요 >>>'))
# b = int(a[-1])
# if b%2==0:
#     print(f"차량번호'{a}'는 오늘 주행가능입니다.")
# else:
#     print(f"차량번호'{a}'는 오늘 주행불가능입니다.")


# 전체합 = 0
# 짝수합 = 0
# 홀수합 = 0
# for i in range(1,101):
#     전체합 = 전체합+i
#     if i%2 == 1:
#         홀수합 = 홀수합+i
#     else:
#         짝수합 = 짝수합+i
# print(전체합)
# print(짝수합)
# print(홀수합)


# 99p 2, 3 문제

# a = (int(input('정수를 입력하세요 >>> ')))
# if a % 3 == 0:
#     print(f'{a}는 3의 배수입니다.')
# else:
#     print(f'{a}는 3의 배수가 아닙니다.')


a = (int(input('정수1 입력 >>> ')))
b = (int(input('정수2 입력 >>> ')))
c = (int(input('정수3 입력 >>> ')))

if a>=b:
    print(f'가장 큰 수는 {a}입니다.')
elif b>=c:
    print(f'가장 큰 수는 {b}입니다.')
else:
    print(f'가장 큰 수는 {c}입니다.')
    