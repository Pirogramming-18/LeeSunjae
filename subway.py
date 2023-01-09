import requests
import random
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep

def subway_game() :


    print('''''')
    print('''＼지~하철 지하철~／＼지~하철 지하철~／
    ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ''')
    print('''   ■■┃■■■┃■■■┃■■■┃■■■┃■■■┃■■■■
    ┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻ 
    ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪''')
    print('''''')
    print('''＼몇호선! 몇호선!／＼몇호선! 몇호선!／
    ʕ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ•̫͡•ʕ•̫͡•ʔ•̫͡•ʔ''')
    print('''   ■■┃■■■┃■■■┃■■■┃■■■┃■■■┃■■■■
    ┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻┻ 
    ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪♬~♪ ♪~ ♬ ♪''')
    print('''''')
    print('''''')

    players = ['윤정', '준서', '홍구', '채원', '선재']
    players_re = []
    right_now = []
    right_now_final = {}
    players_amount = [2, 4, 6, 8, 10]
    players_amount_re = []
    player_dic = {}
    playersIndex = len(players)-1
    correct_line_num = [1,2,3,4]
    turn=1


    while True:
        last = 0

        if turn == 1:
            while True:
                line_num = int(input('1호선 ~ 4호선 선택해주세요! : '))
                if line_num in correct_line_num:
                    break
            print(f'{line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!! {line_num}호선!!!')
        else:
            line_num = random.randint(1,4)
            print('첫번째 턴이 아니므로 컴퓨터가 호선을 정함')
            print(f'이번엔~ 몇호선 ~?? {line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!! {line_num}호선!!!')


        if line_num == 1:
            last += 5
        elif line_num == 2:
            last += 6
        elif line_num == 3:
            last += 8
        elif line_num == 4:
            last += 9
        else:
            print('1~4호선 중 선택하여 주십시오')


        
        response = requests.get(f'https://transit.navitime.com/ko/kr/line/0000000{last}')
        soup = BeautifulSoup(response.text, 'html.parser')

        metro_list = [word.get_text() for word in soup.select("body > div:nth-of-type(2) > div > div:nth-of-type(1) > ol > li > a > span.name")]


        answer_list = []

        if turn == 1:
            while True:
                station = input(f'{line_num}호선에 해당하는 역을 입력해주세요: ')
                turn += 1
                if station in metro_list :
                    print('맞았습니다!')
                    answer_list.append(station)
                    auto_answer = random.sample(metro_list, 5)
                    random.shuffle(players)
                    print(f'{players[0]} : ',auto_answer[0])
                    if auto_answer[0] in answer_list:
                        print(f'이미 나왔습니다!! {players[0]} 패배')
                        print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                        return players[0]
                        break
                    else:
                        answer_list.append(auto_answer[0])
                    print(f'{players[1]} : ',auto_answer[1])
                    if auto_answer[1] in answer_list:
                        print(f'이미 나왔습니다!! {players[1]} 패배')
                        print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                        return players[1]
                        break
                    else:
                        answer_list.append(auto_answer[1])
                    print(f'{players[2]} : ',auto_answer[2])
                    if auto_answer[2] in answer_list:
                        print(f'이미 나왔습니다!! {players[2]} 패배')
                        print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                        return players[2]
                        break
                    else:
                        answer_list.append(auto_answer[2])
                    print(f'{players[3]} : ',auto_answer[3])
                    if auto_answer[3] in answer_list:
                        print(f'이미 나왔습니다!! {players[3]} 패배')
                        print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                        return players[3]
                        break
                    else:
                        answer_list.append(auto_answer[3])
                    print(f'{players[4]} : ',auto_answer[4])
                    if auto_answer[4] in answer_list:
                        print(f'이미 나왔습니다!! {players[4]} 패배')
                        print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                        return players[4]
                        break
                    else:
                        answer_list.append(auto_answer[4])
                    
                else:
                    print('틀렸습니다!! *플레이어 패배*')
                    print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                    answer_list.clear()
                    break
        else:
            while True:
                auto_answer = random.sample(metro_list, 5)
                random.shuffle(players)
                print(f'{players[0]} : ',auto_answer[0])
                print(f'{players[1]} : ',auto_answer[1])
                print(f'{players[2]} : ',auto_answer[2])
                print(f'{players[3]} : ',auto_answer[3])
                print(f'{players[4]} : ',auto_answer[4])
                station = input(f'{line_num}호선에 해당하는 역을 입력해주세요: ')
                if station in metro_list :
                    print('맞았습니다!')
                else:
                    print('틀렸습니다!! *플레이어 패배*')
                    print('아 누가 술을 마셔?! 너가 술을 마셔 원~~샷!!')
                    answer_list.clear()
                    break

subway_game()