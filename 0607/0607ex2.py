'''
2023-06-07
김나현
#문제 정의
    1 ~ 45 사이의 난수 6개를 오름차순 정렬한 로또 번호 생성하기
#문제 분석
    변수 -  lotto, cnt
#알고리즘
    1. 랜덤 모듈 추가
    2. lotto(set변수) 생성
    3. 반복(무한 반복)
        while True :
            lotto = 랜덤 수 6개 추가
            if len(lotto) == 6 :
                break
    4. 생성된 로또번호 출력
    5. 중복된 수 출력
'''

import random #랜덤 모듈 추가

lotto = set() #set변수 생성

cnt = 0 #랜덤 수가 발생할 때마다 1씩 증가

while True : #무한 반복
    lotto.add(random.randint(1,45))
    cnt = cnt + 1

    if len(lotto) == 6 :
        break #반복 종료

print("이번주 로또 번호 : ",sorted(lotto)) #오름차순 정렬
print("중복된 난수의 발생 횟수 : ",cnt - 6) #중복 횟수 출력

