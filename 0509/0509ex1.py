'''
2023-05-09
김나현
#문제 정의
두개의 숫자를 입력 받아서 두 수 사이의 합계 구하기
#문제 분석
    변수 - 정수1(num1),정수2(num2),합계(sum),임시변수(temp),반복(i)
#알고리즘
    1. 변수 선언(변수 초기화)
        num1,num2는 정수를 입력 받는다.
        sum = 0,temp = 0
    2. 논리(선택,반복)
        2-1. (선택 조건) - 항상 num1<=num2
            if num1>num2 :
                num1, num2의 값을 바꾼다.
        2-2. (반복) - num1 ~ num2까지 1씩 증가하면서 더하기
            i = num1
            while i <= num2 :
                sum = sum + i
                i = i + 1
'''

num1 = int(input("첫 번째 숫자 :"))
num2 = int(input("두 번째 숫자 :"))

sum = 0
temp = 0

if num1>num2 : #선택 조건
    temp = num1 #num1 값을 temp에 저장
    num1 = num2 #num2 값을 num1에 저장
    num2 = temp #temp 값을 num2에 저장

i = num1 #i는 num1로 초기화

while i <= num2 : #반복 조건
    sum = sum + i #합계 구하기
    i = i + 1 #i는 1증가

print("{} ~ {}까지의 합계는 {}이다.".format(num1,num2,sum))