'''
2023-05-03
김나현
#문제정의
    입력 받은 구구단 출력하기
#문제 분석
    변수-단(dan),반복횟수(i)
#알고리즘
    1. 변수 선언
        dan을 정수로 입력
        i=1
    2. 논리(반복 - while)
        (조건) while i<=9 : 
                구구단 출력
'''

dan = int(input("단 입력 : ")) #정수로 입력
i=1 #초기화

print("###",dan,"단 ###") #제목 출력

while i<=9 : #반복 조건
    print(dan,"*",i,"=",dan*1)
    i=i+1 #i는 1증가