'''
2023-04-11
김나현
선택문-if~else
(1)입력받은 성적이 80이상이면 '합격' 출력
    그리고 성적과 상관없이 '수고했습니다.' 출력
(2)성적이 80이상이면 '합격' 출력
    성적이 80미만이면 '불합격' 출력
    성적과 관계없이 '수고했습니다.'
'''

#단순 if

score=int(input("점수 입력:")) #점수 정수로 입력

if score>=80: #선택 조건
    print("합격") #조건이 참일 때만 실행

print("수고하셨습니다.") #조건과 관계없이 항상 실행

#if~else
jumsu=int(input("점수 입력:")) #점수 정수로 입력
if jumsu>80: #선택 조건
    print("합격") #조건이 참일 때만 실행
else:
    print("불합격") #조건이 거짓일 때만 실행

print("수고했습니다.") #조건과 관계없이 항상 실행
