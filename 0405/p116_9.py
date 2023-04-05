'''
2023.04.05
김나현
본봉과 수당을 정수로 입력 받아서 이번 달 월급 수령액 구하기
(세금은 총액의 20%)(p116-9번)
'''

sal=int(input("본봉:")) #본봉 입력
allo=int(input("수당:")) #수당 입력

tax=(sal+allo)*0.2 #세금 계산
totel_sal=sal+allo+tax #수령액 계산

print("본봉이 {}이고, 수당이 {}일 때 실수령액은 {}이다.".format(sal,allo,totel_sal))