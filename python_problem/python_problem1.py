import random

def brGame() :
    num = 0
    turn = 0

    while True:
        turn += 1

        if turn % 2 == 1:
            first = 'computer'
            second = 'player'
        else:
            first = 'player'
            second = 'computer'

        while True:


            try:
                if first == 'computer':
                    n = random.randint(1,3)
                else:
                    n = input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ')
                    n = int(n)
            except ValueError:
                print('정수를 입력하세요')
            else:
                if 1 <= n <= 3:
                    if 31 <= num+n:
                        for i in range(num,31):
                            print(f'{first} : {i+1}')
                        num += n
                    else:
                        for i in range(num,num+n):
                            print(f'{first} : {i+1}')
                        num += n
                    break
                else:
                    print('1,2,3 중 하나를 입력하세요')

        if 31 <= num:
            print(f'{second} Win!')
            break

# if __name__ == "__main__":
brGame()

    # while True:
    #     n = input('부를 숫자의 개수를 입력하세요(1,2,3만 입력 가능) : ')
    #     try:
    #         n = int(n)
    #     except ValueError:
    #         print('정수를 입력하세요')
    #     else:
    #         if 1 <= n <= 3:
    #             if 31 <= num+n:
    #                 for i in range(num,31):
    #                     print(f'player{first} : {i+1}')
    #                 num += n
    #             else:
    #                 for i in range(num,num + n):
    #                     print(f'player{first} : {i+1}')
    #                 num += n
    #             break
    #         else:
    #             print('1,2,3 중 하나를 입력하세요')

    # if 31 <= num:
    #     print(f'Player{second} win!')
    #     break