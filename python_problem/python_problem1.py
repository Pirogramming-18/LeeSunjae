num = 0

while True:
    while True:
        n = input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ')
        try:
            n = int(n)
        except ValueError:
            print('정수를 입력하세요')
        else:
            if 1 <= n <= 3:
                if 31 <= num+n:
                    for i in range(num,31):
                        print(f'playerA : {i+1}')
                    num += n
                else:
                    for i in range(num,num+n):
                        print(f'playerA : {i+1}')
                    num += n
                break
            else:
                print('1,2,3 중 하나를 입력하세요')

    if 31 <= num:
        break

    while True:
        n_2 = input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ')
        try:
            n_2 = int(n_2)
        except ValueError:
            print('정수를 입력하세요')
        else:
            if 1 <= n_2 <= 3:
                if 31 <= num+n_2:
                    for i in range(num,31):
                        print(f'playerB : {i+1}')
                    num += n_2
                else:
                    for i in range(num,num + n_2):
                        print(f'playerB : {i+1}')
                    num += n_2
                break
            else:
                print('1,2,3 중 하나를 입력하세요')

    if 31 <= num:
        break