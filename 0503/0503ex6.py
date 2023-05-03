'''
2023-05-03
김나현
#문제 정의
    구구단 출력(중첩 반복)
#문제 분석
    변수 - i, j
#알고리즘
    논리(반복 - 중첩 반복(for))
        (조건) for i in range(2,10) :  #단 반복
                    제목 출력
                    for j in range(1,10) : #단 안에서 곱하는 수 반복
                        구구단 출력
'''

for i in range(2,10) :  #단 반복
    print("###",i,"단 ###") #제목 출력
    for j in range(1,10) : #단 안에서 곱하는 수 반복
        print(j,"*",i,"=",j*1)
