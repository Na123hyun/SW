'''
2023-04-12
김나현
두 정수를 입력 후
모두 짝수이면 두 수를 더한 결과를 출력
둘 중 하나가 홀수이면 몇 번째 입력한 수를 짝수로 입력하라고 출력
#문제 분석
    변수 - 정수1(num1),정수2(num2),op(+)
    수식
        num1%2==0 and num2%2==0 (모두 짝수,)
        num1 op num2
        num1%2==0 and num2%1!=0 (num1은 짝수, num2는 홀수,num2를 짝수로 입력하시오.)
        num1%1!=0 and num2%1!=0 (모두 홀수, num1과 num2를 짝수로 입력하시오.)
#알고리즘
    1.변수 선언
        num1,num2를 정수로 입력
    2.논리(선택 if~elif~else)
        if num1%2==0 and num2%2==0:
            (참)"모두 짝수"
            num1 op num2
        elif num1%2==0 and num2%1!=0:
            (거짓)"num2를 짝수로 입력하시오.
        else num1%1!=0 and num2%1!=0:
            (거짓)"num1과 num2를 짝수로 입력하시오."
'''

num1=int(input("첫 번째 숫자:"))
num2=int(input("두 번째 숫자:"))

if num1%2==0 and num2%2==0:
    print("num1+num2",num1+num2)
elif num1%2==1 and num2%2==0:
    print("첫 번째 숫자를 짝수로 입력하시오.")
elif num1%2==0 and num2%2==1:
    print("두 번째 숫자를 짝수로 입력하시오.")
else :
    print("첫 번째 숫자와 두 번째 숫자를 짝수로 입력하시오.")
