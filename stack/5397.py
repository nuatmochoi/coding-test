"""
창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 
며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.

키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.

강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.
"""

for _ in range(int(input())):
    l_stack = []
    r_stack = []
    data= input()
    for i in data:
        if i == '-':
            if l_stack:
                l_stack.pop()
        elif i == '<':
            if l_stack:
                r_stack.append(l_stack.pop())
        elif i == '>':
            if r_stack:
                l_stack.append(r_stack.pop())
        else:
            l_stack.append(i)
    l_stack.extend(reversed(r_stack))
    print(''.join(l_stack))