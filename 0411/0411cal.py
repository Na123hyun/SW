'''
2023-04-11
김나현
숫자와 연산자를 정수로 입력 받아서 합계 구하기
num1(5),num(2),op(+,-,*,/)
'''

num1=int(input("첫 번째의 숫자를 입력하시오."))
num2=int(input("두 번째의 숫자를 입력하시오."))
op=(input("+,-,*,/ 중에서 고르시오."))

if op=="+":
    print('결과 값은',num1+num2)
elif op=="-":
    print('결과 값은',num1-num2)
elif op=="*":
    print('결과 값은',num1*num2)
elif op=="/":
    print('결과 값은',num1/num2)
else:
    print("해당 연산자는 없습니다.")
