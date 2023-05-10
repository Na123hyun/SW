'''
2023-05-10
김나현
#문제 정의
    입력 받은 숫자의 합이 1000이상이면 합계와 평균 출력
#문제 분석
    변수 - 합계(sum), 입력 횟수(cnt), 평균(avg), 정수(num)
#알고리즘
    1. 변수 선언(초기화)
        num은 정수 입력 받기
        sum = 0, cnt = 0, avg = 0
    2. 논리(반복 안에 선택 포함)
        (반복) while True : #무한 반복
                num
                cnt 1증가
                sum에 더하기
                (선택) if sum >= 1000 :
                        break
    3. 합계, 평균 출력
'''

sum = 0; cnt = 0; avg = 0

while True : #무한 반복
    num = int(input("숫자 입력 :")) #정수 입력
    cnt = cnt + 1 #cnt 1 증가
    sum = sum + num #합계
    if sum >= 1000 :
        break #반복 종료

avg = sum / cnt #평균 계산

print("1000을 넘은 수 : %d"%sum, end=" ")
print("평균:%.2f"%avg)
