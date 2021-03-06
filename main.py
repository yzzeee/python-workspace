'''
변수명 정하기
 1) 영문과 숫자, _ 로 이루어진다.
 2) 대소문자를 구분한다.
 3) 문자나, _로 시작한다.
 4) 특수문자를 사용하면 안된다. (&, % 등)
 5) 키워드를 사용하면 안된다. (if, for 등)
'''

'''
a=1
print(a)
A=2
c=3
_b=4
# 2b=5
print(a, A, c, 4)
a, b, c=3, 2, 1
print(a, b, c)

# 값 교환
a, b=10, 20
print(a, b)
a, b=b,a
print(a, b)

# 변수 타입
a=12345
print(type(a))
a=12.123456789123456789
print(a, type(a)) # 실수형은 8바이트까지 차지가능
a='student'
print(a, type(a))

# 출력방식
print("number")
a, b, c=1, 2, 3
print(a, b, c)
print("number : ", a, b, c)
print(a, b, c, sep=', ')
print(a, b, c, sep=',')
print(a, b, c, sep='\n')
print(a, end=' ')
print(b, end=' ')
print(b, end=' ')
'''

'''
변수입력과 연산자
'''

'''
# a=input("숫자를 입력하시오 : ")
# print(a)
a, b=input("숫자를 입력하시오 : ").split()
print(a+b) # 문자형으로 나옴
a=int(a)
print(type(a))
a, b=map(int, input("숫자를 입력하세요 : ").split())
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) # 몫
print(a%b) # 나머지
print(a**b) # 거듭제곱
a=4.3
b=5
c=a+b
print(c, type(c))
'''

'''
조건문 if(분기, 중첩)
'''
'''
x=7
if x==7:
    print("Lucky")
    print("ㅋㅋ")
x=15
if x>=10:
    if x%2==1:
        print("10 이상의 홀수")
x=9
if x>0:
    if x<10:
        print("10보다 작은 자연수")
x=7
if x>0 and x<10:
    print("10보다 작은 자연수")
if 0<x<10:
    print("10보다 작은 자연수")
x=10
if x>0:
    print("양수")
else:
    print("음수")
x=80
if x>=90:
    print("A")
elif x>80:
    print("B")
elif x>70:
    print("C")
'''

'''
반복문(for, while)
'''
'''
a=range(10)
print(list(a))
for i in range(10):
    print("hello1", i)
    if i == 9:
        print("\n")
for i in range(1, 11):
    print("hello2", i)
    if i == 10:
        print("\n")
for i in range(10, 0, -2): # range의 마지막 인자는 간격
    print("hello3", i)
    if i == 2:
        print("\n")
i=1
while i<=10:
    print("hello4", i)
    if i == 10:
        print("\n")
    i=i+1
i=10
while i>=1:
    print("hello5", i)
    if i == 1:
        print("\n")
    i=i-1
i=1
while True:
    print("hello6", i)
    if i==10:
        print("\n")
        break
    i+=1
for i in range(1, 11):
    if i%2==0:
        continue
    print("hello7", i)
    if i==9:
        print("\n")
for i in range(1, 11):
    print("hello8", i)
    if i==5:
        break
else:
    print(11)
for i in range(1, 11):
    print("hello9", i)
    if i == 5:
        break
else: # for 문이 정상적으로 종료되었을 때
    print(11)
'''

'''
반복문을 이용한 문제풀이
 1) 1부터 N까지 홀수 출력하기
 2) 1부터 N까지 합 구하기
 3) N의 약수 출력하기
'''
'''
# 1부터 N까지 홀수 출력하기
N = int(input("숫자를 입력하시오 : "))
for i in range(N + 1):
    if i % 2 == 1:
        print(i, end=' ')
print("\n")
# 1부터 N까지 합 구하기
N = int(input("숫자를 입력하시오 : "))
acc = 0
for i in range(N + 1):
    acc += i
print(acc, end="\n\n")
# N의 약수 출력하기
N = int(input("숫자를 입력하시오 : "))
for i in range(1, N + 1):
    if N % i == 0:
        print(i, end=' ')
'''

'''
중첩 반복문(2중 for문)
'''
'''
for i in range(5):
    for j in range(5):
        print(j, end=' ')
    print()
for i in range(5):
    print('i:', sep='', end=' ')
    for j in range(5):
        print('j:', j, sep='', end=' ')
    print()
for i in range(5):
    for j in range(5):
        print('*', end=' ')
    print()
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    print()
'''

'''
문자열과 내장함수
'''
'''
msg="It is Time"
print(msg)
print(msg.upper())
print(msg.lower())
tmp=msg.upper()
print(tmp)
print(tmp.find('T'))
print(tmp.count('T'))
print(msg)
print(msg[:4]) # 시작:종료 인덱스 종료 인덱스 전까지 출력
print(msg[3:5]) # 3번 인덱스에서 4번 인덱스까지
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=' ')
print()
for x in msg:
    print(x)
print()
for x in msg:
    if x.isupper():
        print(x)
print()
for x in msg:
    if x.islower():
        print(x)
print()
for x in msg:
    if x.isalpha(): # 알파벳이냐?
        print(x)
print()
tmp='AZ'
for x in tmp:
    print(ord(x)) # 아스키넘버를 출력
print()
tmp='az'
for x in msg:
    print(ord(x))
print()
tmp=65
print(chr(tmp))
'''

'''
리스트와 내장함수(1)
'''

'''
import random as r

a = []
print(a)
b = list()
print(b)
a = [1, 2, 3, 4, 5]
print(a)
print(a[0])

b = list(range(1, 20))
print(b)

c = a + b
print(c)

print(a)
a.append(6)
print(a)
a.insert(3, 7)  # 첫 번째 인자로 들어온 인덱스에 두 번째 인자의 값 삽입
print(a)
a.pop()  # 리스트의 맨 뒤의 인덱스 값 추출
print(a)
a.pop(3)  # 해당 인덱스의 값 추출
print(a)
a.append(4)
print(a)
a.remove(4)  # 리스트에서 첫 번째로 찾게되는 해당 값 추출
print(a)
print(a.index(5))  # 인자의 값을 찾아서 해당 인덱스를 반환
a = list(range(1, 10))
print(a)
print(sum(a))  # 리스트 모든 값의 합
print(max(a))  # 인자로 들어온 값 중 최대값
print(min(a))  # 인자로 들어온 값 중 최소값
print(min(7, 3, 5))
r.shuffle(a)
print(a)  # 인자로 들어온 값을 직접 변경
a.sort()
print(a)
a.sort(reverse=True)  # 내림차순 정렬
print(a)
a.sort()
print(a)
a.clear()  # 리스트의 값을 모두 제거
print(a)
'''

'''
리스트와 내장함수(2)
'''

'''
a = [23, 12, 36, 53, 19]
print(a[:3])
print(a[1:4])
print(len(a))
for i in range(len(a)):
    print(a[i], end=' ')
print()
for x in a:
    print(x, end=' ')
print()
for x in a:
    if x % 2 == 1:
        print(x, end=' ')
print()
for x in enumerate(a):
    print(x)  # 튜플 출력
b = (1, 2, 3, 4, 5)
print(b[0])
# b[0] = 7  # 에러 발생, 튜플의 값은 변경이 불가
for x in enumerate(a):
    print(x[0], x[1])
print()
for i, v in enumerate(a):  # 가장 많이 사용하는 방법
    print(i, v)
print()
if all(60 > x for x in a):
    print('all true')
else:
    print('has false')
if any(60 < x for x in a):
    print('any true')
else:
    print('all false')
'''

'''
2차원 리스트 생성과 접근
'''

'''
a = [0] * 10
print(a)
a = [[0] * 3 for _ in range(3)]  # 2차원 리스트 선언
print(a)
a[0][1] = 1
print(a)
for x in a:  # 2차원 리스트 출력
    for y in x:
        print(y, end=' ')
    print()
'''

'''
함수 만들기
'''

'''
def add(a, b):
    c = a + b
    print(c)


add(3, 2)


def add(a, b):
    return a + b


print(add(3, 2))


def isPrime(x): # 소수만 출력하는 함수
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for y in a:
    if isPrime(y):
        print(y, end=' ')
'''

'''
람다 함수
'''


def plus_one(x):
    return x + 1


print(plus_one(1))

plus_two = lambda x: x + 2
print(plus_two(2))

a = [1, 2, 3]
print(list(map(plus_two, a)))
print(list(map(lambda x: x + 3, a)))
