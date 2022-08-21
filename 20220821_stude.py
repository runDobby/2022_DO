# #교재로는 39p
#         #  0번째 index  1번째    2번쨰 index....
# a_tuple = ('안녕하세요', '저는', '박형준입니다') # () -> Tuple : 변경 X
#               [0]       [1]       [2]
#               [-3]      [-2]      [-1]
#
# a_list = ['안녕하세요', '저는', '박형준입니다']
#
# print
#
#
# """
# deep copy 깊은 복사
# shallow copy 얇은 복사 = 값 복사 = .copy()
#
# 메모리 공간
# .copy()
# a_list -> [ 1, 2, 3 ]
# b_list -> [ 1, 2, 3 ]
#
# b_list = a_list
# b_list -> [100, 2, 3]
# """
#
#
# while True # 무한반복문
#
# break #정지
#
#
#for i in range(1, 10)


# if a%2 == 0: #만약 a가 짝수라면


#today

# 튜플 딕셔너리 세트

# list_example = [1,2,3,4,5]
# tuple_example = (1,2,3,4,5)
# print(_type(list_example))
# print(_type(tuple_example)) #리스트랑 다르게 변경이안됨
# print(set_exaple) #리스트랑 다르게 순서가 없음 # 중복 제거용, 집합에 사용

# 캐스팅  바꾸고싶은 자료형(변수)
# s1 = {1,2,3}
# s2 = {3,4,5,4,5}
# print( s2 - s1) #
# print( s2 & s1) # 교집합
# print( set(s1) - set(s2) )


#c++  (바꾸고싶은 자료형)변수

# list_example ->
# typle(list_example)


# set_example = {5,3,'b','a',4} # 순서가 없으므로 계속 바뀜
# for i in set_example:
#     print(i)
#
#
# dict_example = {
#     '이름' : '박형준',
#     '나이' : 30,
#     '성별' : '남자'
# }
# dict_example['추가키'] = '추가값'
# dict_example.update(추가키 = '추가값')
# dict_example.pop('추가키')
# # json 딕셔너리는 key : value
# print(dict_example.keys())
# print(dict_example.values())
# print(dict_example['이름'])
#
#
# 반복횟수를 정확하게 알떄 => for 문
# for ___ in ____:
#     ...
#     ...
#
# 반복을 종료하는 조건을 알 떄 => while 문
# while [조건식이 참일때까지 루프]:
#     ...
#     ...
#
"""
# for for문지역변수 in iterable_object:
for 변수 in 반복가능객체:
    반복실행문
    한글자

# iterable 반복가능한 "안녕하세요", [1,2,3,4,5], (1,2,3,4,5), {1,2,3,4,5}, 등등
# iterable한 모든 것을 반복가능객체에 넣어도 된다.

for _ in range(5):
    print('안녕하세요')
"""
"""
토요일은 내장함수 및 외부 라이브러리 (Randon모듈)
        if, elif, else, pass, inNot in
        
일요일은 While Break Continue
"""