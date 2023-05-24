'''
2023-05-24
김나현
#문제 정의
    난수를 발생시켜 num.txt 파일을 만들고 이 파일을 이용해서
    각 학생의 평균을 구한 다음 avg.txt파일에 저장하기
'''

import random #난수 모듈 추가
with open("C://data/num.txt", "w") as f : #파일 객체
    for i in range(5) : #줄 반복
        for j in range(5) : #랜덤 수 찍기 반복
            f.write(str(random.randint(1,100))) #랜덤 수 파일에 쓰기
            f.write(' ') #숫자 다음 공백 찍기
        f.write('\n') #줄 바꿈

with open("C://data/num.txt","r") as f1 : #읽기 파일 객체
    with open("C://data/avg.txt","w") as f2 : #쓰기 파일 객체
        j = 0
        while True : #무한 반복
            j = j + 1
            score = f1.readline() #num.txt 한 줄 읽어 오기
            if score == '' : #내용이 없으면
                break #반복 종료
            scorelist = score.split() #읽어 온 한 줄을 공백 기준 리스트로 반환

            sum = 0 #합계
            for i in range(5) : #한 학생당 5과목의 점수 더하기
                sum = sum + int(scorelist[i]) #리스트의 항목 더 하기
            print("%d번 학생의 평균 :"%j,sum/5,file = f2) #결과 파일에 저장