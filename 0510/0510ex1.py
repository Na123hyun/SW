'''
2023-05-10
김나현
#문제 정의
    입력 받은 숫자가 소수인지 아닌지 판별하는 프로그램
#문제 분석
    변수 - 숫자(num)
#알고리즘
    1. 변수 선언(초기화)
        num에 정수 입력
    2. 논리(반복문 안에 선택포함)
        (반복) for i in range(2,num + 1) :
                (선택)if num%i==0 :
                        break
        (선택) if num==i :
                    소수
                else :
                    소수 아님
'''

num = int(input("소수 검증 숫자 입력 :"))

for i in range(2,num+1) :
    if num%i==0 : #선택 조건
        break #반복 종료
if num==i :
    print("{}는 소수이다.".format(num))
else :
    print("{}는 소수가 아니다.".format(num))