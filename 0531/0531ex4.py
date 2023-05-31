'''
2023-05-31
김나현
#문제 정의
    튜플 안에 있는 숫자들의 종류와 반복 갯수 분석하기기
#문제 분석
    변수 - num, 빈 리스트(num_list)
#알고리즘
    1. 튜플 정의
    2. 빈 리스트 생성
    3. 반복
        for i in range(len(num))
            리스트에 없는 경우
            리스트에 추가
    4. 결과 출력
'''

num = (1, 4, 6, 5, 4, 3, 2, 0, 1, 2, 4, 6, 7, 9, 4, 0)
num_list = [] #빈 리스트

print("생성된 튜플",num)

for i in range(len(num)) : #튜플 길기 만큼 반복
    if num[i] not in num_list : #리스트에 없는 경우
        num_list.append(num[i]) #리스트에 추가

        print(num[i],"개수 : ",num.count(num[i])) #갯수 출력