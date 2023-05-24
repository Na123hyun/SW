'''
2023-05-24
김나현
#문제 정의
    score1.txt 파일을 읽어와서 각 학생의 등급을 결정하고
    결과를 repot1.txt 파일에 저장하기
'''
score = [] #빈 리스트 변수 생성
f = open("C://data/score1.txt","r") #읽기 객체 생성

for i in range(10) :
    score.append(f.readline().split()) #한 줄씩 읽어서 공백의 기준으로 나누고 score 리스트에 추가 

for j in range(10) : #10명의 점수에 대한 등급 계산 반복
    score[j][1] = float(score[j][1]) #문자열을 실수로 반환

    if score[j][1] >= 90 :
        score[j].append("A") #점수가 90 이상이면
    elif score[j][1] >= 80 :
        score[j].append("B") #점수가 80 ~ 89이면
    elif score[j][1] >= 70 : 
        score[j].append("C") #점수가 70 ~ 79이면
    else : #점수가 70 미만
        score[j].append("D") 
    
for i in range(10) : #10명 등급 화면 클릭
    print("{:<5}{:>5}".format(score[i][0],score[i][2]))

f.close() #파일 닫기
