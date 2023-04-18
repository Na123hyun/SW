'''
2023-04-18
김나현
두 과목 모두 75이상 그리고 총점 180이다. "최우수"
총점 160이상 "우수", 150이상 "보통"
두 과목 모두 75미만이먄 "분발합시다."
#문제분석
    변수:점수1(score1),점수2(score2),합계(total)
    수식:total=score1+score2 #합계
#알고리즘
    1. 변수선언
    score1, score2에 점수 입력 받기
    2. 논리(선택-중첩if)
        if (score1)>=75 and (score2)>=75:
            if (total)>=180:
            "최우수"
            elif (toatal)>=160:
            "우수"
            else:
                "보통"
        else:
            "분발합시다."
'''

score1=int(input("성적1 입력:")) #점수 정수로 입력
score2=int(input("성적2 입력:")) #점수 정수로 입력
total=score1+score2 #합계

if (score1)>=75 and (score2)>=75: #조건1 
        if (total)>=180: #조건2-1
            print("최우수") #조건1,2-1 모두 참
        elif (total)>=160: #조건2-2
            print("우수") #조건1,2-2 모두 참
        else:
            print("보통") #조건1 참, 조건2-1,2-2 모두 거짓
else:
    print("분발합시다.") #조건1 거짓

