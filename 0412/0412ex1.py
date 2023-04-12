'''
2023-04-12
김나현
평점을 입력 받아서 평점 출력, 4.2이상이면 "해외 연수"
#문제 분석
    변수-평점(score)
알고리즘
    1.변수 선언
        score에 평점 실수로 입력 받기
    2.논리(선택)
        if score>=4.2:
'''
score=float(input("Enter you score : ")) #평점 실수로 입력
print("당신의 평점은 : ", score) #평점 출력
if score>=4.2: #조건
    print("해외 연수") #조건이 참일 때만 실행


