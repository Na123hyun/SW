'''
2023-04-18
김나현
두 정수를 입력 받아 두 정수의 연산 값이 출력되는 프로그램을 작성(단, 나눗셈 몫을 계산할 때 나누는 수 y는 0이 입력되면 안 됨.)
두 정수 입력 x>y->x//y, x<y->x+y,x==y->x*y
단, 나눗셈 몫 계산할 때 y는 0안 됨.
#문제 분석
    변수: su1(x), su2(y)
    수식: x//y, x+y, x*y
#알고리즘
    1.변수 선언
        su1,su2 정수로 입력
    2.논리(선택)
        if x>y:
            if y!=0:
                x//y
        elif x==y
            x+y
        else:
            x*y
'''

su1=int(input("x 입력:"))
su2=int(input("y 입력:"))

if su1>su2:
    if su2!=0:
        print(su1//su2)
elif su1<su2:
    print(su1+su2)
else:
    print(su1*su2)











