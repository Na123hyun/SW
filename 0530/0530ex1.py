'''
2023-05-30
김나현
시퀀스 자료형 - 문자열 메소드 연습
'''

st = input("영어 문장 입력 : ")

print("입력된 문장의 길이 : ",len(st))
print("입력 받은 문장의 첫 문자만 대문자 : ",st.capitalize())
print("입력 받은 문장의 첫 각 단어의 첫 글자 대문자 : ",st.title())
print("모두 대문자로 : ",st.upper())
print("모두 소문자로 : ",st.lower())
print("문자열에서 a의 갯수를 구해라 : ",st.count('a'))
print("모두 문자열로 구성되었는가? : ",st.isalpha()) #공백 포함
print("스페이스의 갯수 : ",st.count(' '))
print("스페이스를 삭제한 문장 : ",st.replace(' ','')) #공백도 공백 아닌 것 