'''
2023-05-23
김나현
#문제 정의
    stu.txt 파일을 읽어서 각 학생의 평균 성적 계산해서 출력하기
#문제 분석
    변수 - 한 줄씩 읽어서 저장(score), 리스트 자료로 변환(scorelist)
            리스트에서 이름 항목 저장(name),합계(sum)
#알고리즘
    1. 파일 열기(읽기 모드)
    2. 파일 처리
        2.1 (반복) while True :
                        한 줄 읽어서 score  저장
                        (선택) if score == ' ' :
                                break
                        읽어온 내용을 리스트로 변환해서 scorelist 저장
                        scorelist에서 첫 번째 항목(이름)을 name 저장
                        (반복) for i in range(1,4) :
                                scorelist의 1,2,3 항목의 값을 sum에 더하기
    3. 파일 닫기
'''

f = open("C://data/stu.txt",'r') #읽기 모드 파일 객체 생성

while True : #무한 반복
    score = f.readline() #한 줄씩 읽어오기
    if score == '' : #더 이상 읽어 올 내용이 없다면
        break #반복 종료
    
    scorelist = score.split() #리스트 자료로 반환 
    name = scorelist[0] #리스트 첫 번째 항목은 이름

    sum = 0 #합계 저장
    for i in range (1,4) :
        sum = sum + int(scorelist[i]) #3과목 성적의 합계

    print(name+"의 평균 성적은  :%.1f"%(sum/3)) #소수점 자릿수 표현 형식 %.1f(소수점 자릿수) ~ %(변수) 괄호로 묶기
f.close() #파일 닫기