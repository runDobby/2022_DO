"""
2단원 : 변수와 자료형
"""


# int_var = 1
# float_var = 1.5
# str_var = '안녕하세요' #문자 != 문자열 except 파이썬은 이 두개를 동일취급
# list)var = [1,2,3,4,5]
# set_var + (1,2,3,4,5)
# dict_var = { "K" : "V" }
# bool_var = True # or False False = 0, True != 0이 아닌 모든 수
# Mutable , Immutable
# 변수가 저장되는 로직(메모리주소값, Alias)
# 함수가 메모리를 Call할떄의 방식 (c by reference, value, pointer)


# 3단원
# print("안녕하세요 {}저는 {} '박형준'입니다".format('"','"'))
# print("안녕하세요 /저는/ '박형준'입니다")
# end='\n' 줄바꾸기, end='\t' 띄어쓰기

#변수는 숫자가 이닌 문자로, 기호도 사용하지 않기

# inputIntAge = 10 # 요즘 유행하는 변수명
# age_int = 13

#string format


# last_day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
#                 # 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12
#
# 달 =input("1~12 사이의 월을 입력하세요 >>>")
#
# print("{}월은 {}일까지 있습니다".format(달, last_day_list[int(달)-1]))


# 4단원 연산자

# 1 ~ 100까지 합을 구하는 프로그램
# 합 = 0
# for i in range(1,101):
#     합=합+i
# print(합)

# # 변수 += 1

# 변수=20
# print(변수 > 10) # !=, <=, 등등

# 변수 = 20
# print(0 < 변수 and 변수 < 30)  # and자리에 or을 넣을 수도 있다.


# 5단원 조건문

"""
비교연산이 기본 + Boolean(True, False)

if (조건식이 들어감):
    이 코드가 실행되는 조건은
    위의 조건식이 True일때
    else
    elif
"""

# list_var = [1,2,3,4,5]
#
# for i in range(1,101):
#     if i % 10:
#         print(i)


# 6단원 반복문

# while True:
#     블라블라
#     break


# 7단원 for문

for _______ in _______:
      변수        범위


# 8단원 기타제어문

# 9단원 내장함수