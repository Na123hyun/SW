'''
2023-05-09
김나현
#문제 정의
    입력 받은 숫자의 팩토리얼 값을 계산하기
#문제 분석
    변수 - 정수(num),팩토리얼(fac)
#알고리즘
    1.변수 선언(초기화)
        num을 정수로 입력 받는다
        fac = 1
    논리(반복 for)
        for i in range(num,0,-1) :
            fac = fac * 1
'''

num = int(input("팩토리얼 숫자 입력 :"))
fac = 1

for i in range(num,0,-1): #반복 조건
    fac = fac * 1 #팩토리얼 계산

print("%d의 팩토리얼 값은 :"%num,fac)
#%d 정수, %f 실수