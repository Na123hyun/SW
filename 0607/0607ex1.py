'''
2023-06-07
김나현
#문제 정의
    랜덤으로 2개의 set 만든 후 합집합, 교집합, 차집합 구하기
#문제 분석
    변수 - num1, num2
#알고리즘
    1. 랜덤 모듈 추가
    2. 비어있는 세트 변수 생성
    3. 반복(무한 반복)
        while True :
            if len(num1) < 10 :
                num1 = 랜덤 수 추가
            if len(num2) < 10 :
                num2 = 랜덤 수 추가
    4. 합집합, 교집합, 차집합
'''

import random

num1 = set() #비어있는 세트
num2 = set() #비어있는 세트

while True : #무한 반복
    if len(num1) < 10 :
        num1.add(random.randint(1,100)) #1~100 사이의 랜덤 수 추가
    if len(num2) < 10 :
        num2.add(random.randint(1,100))
    if len(num1) == 10 and len(num2) == 10 :
        break

print("발생한 10개의 난수 num1 : ",num1)
print("발생한 10개의 난수 num2 : ",num2)

print("합집합 : ",num1 | num2)
print("교집합 : ",num1 & num2)
print("차집합 : ",num1 - num2)