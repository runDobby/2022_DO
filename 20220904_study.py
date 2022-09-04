list_var = ['박형준','호박','꿍디']
#
# i=1
# while True:
#     print("{}".format(list_var[i]),end='\t')
#     i+=1
#     print( '->'.join(list_var) )
#

# 1. 프로그래밍을 공부하고 싶다 -> 빌트인함수를 구현해보는연습
# 정답1. 내장함수를 쓰면 됩니다.
# print( '->'.join(list_var) )
#
# 문자("안녕하세요 저는 박형준입니다.")
#
# 문자.replace('박형준', '다른이름')
#
# print("{}".format(문자))


# 문제1: 두 수를 입력받아 더한값을 출력하는 Add함수를 만들어보세요.


# def add2(_lest, _right):
#     return _lest, _right


# 11장 사용자 함수 -> 코드 재사용성


# a=3
# b=5
#
# def add(a,b):
#     return a+b
# print(a+b)
#
# c=0
# for i in range(b):
#     c=c+a
# print(c)
#
# def mul(a,b):
#     return a * b
# print(mul(a,b))
#
# def mul(_left,_right):
#     합=0
#     for _ in range(_right):
#         합=add(합,_left)
#     return 합


# def my_factorial(n):
#     if(n > 1):
#         return n * my_factorial(n - 1)
#     else:
#         return 1
#
# a = int(input("팩토리얼을 구할 숫자를 입력하세요 : "))
# print(my_factorial(a))


def is_three_number(x):
    if x in ['3','6','9']:
        return True
    else:
        return False