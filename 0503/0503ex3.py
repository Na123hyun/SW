'''
2023-03-05
김나현
#문제 정의
1~ 입력 받은 숫자까지의 합계 구하기
#for 반복문
    #문제 분석
        변수 num,sum
        수식 
            sum=sum+1
    #알고리즘
        #변수 선언
            num에 정수 입력
            total=0
        #논리(반복)
            total=0
            for i in range(1,num + 1) :
            total=total+i
            print('1~{}까지의 합계는 {}'.format(num,total))
'''

#for 반복문
num = int(input("합계를 구할 숫자 입력 : ")) #정수로 입력
total=0 #합계

for i in range(1,num + 1) :
    total=total+i
print('1~{}까지의 합계는 {}'.format(num,total))

print() #한 줄 띄우기

