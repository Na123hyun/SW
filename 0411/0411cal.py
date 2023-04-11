'''
2023-04-11
김나현
숫자와 연산자를 정수로 입력 받아서 합계 구하기
numder1(5),numder(2),op(+,-,*,/)
'''

numder1=int(input("첫번째 정수를 입력하시오."))
numder2=int(input("2"))
op=(input("+,-,*,/"))

if op=="+":
    print('결과값은',numder1+numder2)

