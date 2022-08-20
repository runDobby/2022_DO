# 교재로 39p

a1 = '안녕하세요'
a2 = '저는'
a3 = '박형준입니다'

a_list = ['안녕하세요', '저는', '박형준입니다'] # [] -> List
         # 0번째 index 1번째   2번째 index....
a_tuple = ('안녕하세요', '저는', '박형준입니다') # () -> Tuple

print(a1)
print(a2)
print(a3)

print(a_list[:5])

a = [1,2,3,4,5]

print(a[2:])
print(a[:3])
for i in range(0,5):
    print(a[i])

print(a[2:])
print(a[:4])
print(a[2:4])

a_list.append('추가')
print(a_list)

# 1부터 100까지 출력
# 1부터 100까지 더한값을 출력

for i in range(1,11):
    print(i)

a_list = ['앞에추가'] + a_list
print(a_list)
a_list.insert(1, '첫번')
print(a_list)
a_list.remove('첫번')
print(a_list)
a_list.pop()
print(a_list)

b_list = a_list.copy()
print(b_list)

b_list[0] = 100

print(b_list)