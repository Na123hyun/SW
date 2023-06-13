'''
2023-06-13
김나현
#문제 정의
    3개의 매개변수르 전달 받아서 가장 큰 값을 리턴하는
    findmax(a,b,c)함수 구현
#문제 분석
#알고리즘
    1. findmax(a,b,s) 함수 선언
        1-1. a,b,c 중 가장 큰 값 찾기
    2. num1, num2, num3 정수 입력 받기
    3. findmax(num1, num2, num3) 호출
    4. 리턴 받은 가장 큰 값 출력
'''

def findmax(a,b,c) : #함수 선언
    if a > b : #가장 큰 수를 구하는 기능을 정의
        biggest = a
    else :
        biggest = b

    if biggest < c :
        biggest = c

    return biggest #가장 큰 값을 반환

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))
num3 = int(input("num3 : "))

biggist_number = findmax(num1,num2,num3) #함수 호출하고 return문에 의해 반환되는 값을 변수에 저장
print("가장 큰 숫자는 : ",biggist_number)