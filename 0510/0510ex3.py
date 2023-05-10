'''
2023-05-10
김나현
#문제 정의
    입력 받은 숫자 만큼 줄 반복 하면서 별 찍기
#문제 분석
    변수 - 숫자(num)
#알고리즘
    1. 변수 선언(초기화)
        num을 정수에 입력 받기
    2. 논리(중첩 반복)
        (반복) for i in range(1,num+1) : #줄 반복
                (반복) for j in range(1,i+1) #별 찍기 반복
                        별 찍기
'''

num = int(input("숫자 입력 :")) #정수 입력

for i in range(1,num+1) : #줄 반복
    for j in range(1,i+1) : #별 찍기 반복
        print("*",end=" ")
    print() #줄 바꿈

#거꾸로 출력

print("\n거꾸로 출력")

num1 = int(input("숫자 입력 : "))

for i in range(1,num1+1) :
    for j in range(i,num1+1) :
        print("*",end=" ")
    print()