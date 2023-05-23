'''
2023-05-23
김나현
#문제 정의
    키보드로 입력 받은 내용을 리스트에 저장하고 파일(out.txt)에 출력하기
#문제 분석
    변수 - 입력값 저장할 리스트(enter), 키보드 입력 받은 내용 저장(text)
#알고리즘
    1. 변수 선언(초기화)
        enter = []
    2. 파일열기 객체 생성(쓰기 모드)
    3. 파일 처리
        3.1 (반복) while True :
                    text = 문장 입력
                    (선택) if text == ' ' :
                                break
                    text를 enter(리스트 변수)추가
        3.2 파일에 결과 출력
            writelines()
    4. 파일 닫기
'''

enter = [] #리스트 변수 생성

f = open("C://data/out.txt","w") #파일 쓰기 객체

while True :  #무한 반복
    text = input("문장 입력(끝 : 엔터키) :") #문자열 입력
    if text == '' : #입력 내용이 없으면
        break #반복 종료
    enter.append(text+"\n") #입력 내용 리스트에 추가

f.writelines(enter) #리스트 자료형을 파일에 출력

f.close() #파일 닫기

print("입력될 리스트 :",enter)
print("out.txt 파일이 생성되었습니다.")