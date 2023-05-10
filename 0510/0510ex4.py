'''
2023-05-10
김나현
#문제 정의
    3의 배수의 총합이 입력된 숫자를 넘었을 때의 n 값과 총합계,
    n 값이 몇 번째인지를 while 반복문을 사용한 프로그램
#문제 분석
    변수 - num, sum, cnt
#알고리즘
    1. 변수 선언(초기화)
        num을 정수에 입력 받기
        sum = 0
        cnt = 0
    2. 논리(반복 안에 선택문 포함)
        (반복 조건) while True : #무한 반복
                        i = i + 3
                        sum = sum + i
                        cnt = cnt + 1
            (선택 조건) if sum > num :
                                break
'''

num = int(input("사용자 입력 : ")) #정수 입력
sum = 0 #합계
cnt = 0 #3의 배수의 갯수
i = 0

while True :
    i = i + 3
    sum = sum + i
    cnt = cnt + 1
    if sum > num :
        break

print("{}을 넘었을 때 숫자 : {}".format(num,i))
print("{}을 넘었을 때까지의 합계 : {}".format(num,sum))
print("{}을 넘었을 때까지 몇 번째 3의 배수인가 : {}".format(num,cnt))
