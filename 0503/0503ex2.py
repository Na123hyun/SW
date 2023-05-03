'''
2023-05-03
김나현
1~10까지 합계 구하기
'''

#while 반복문
i=1 #반복 횟수 초기화
sum=0 #합계
while i<=10 : #반복 조건
    sum=sum+i #합계 저장
    i=i+1 #i는 1증가
print('1~10까지의 합계 :',sum)

print() #한 줄 띄우기 

#for 반복문
sum1=0 #합계
for j in range(1,11) : #반복 조건
    sum1=sum1+j #합계 구하기
    #j=j+1은 필요 없다 range가 더한다 초기화도 필요없다
print('1~10까지의 합계는 : ',sum1)

