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