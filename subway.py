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
    turn = 1

    while True:
        last = 0

        if turn == 1:
            line_num = int(input('1호선 ~ 4호선 선택해주세요! : '))
            print(f'{line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!! {line_num}호선!!!')
        else:
            line_num = random.randint(1,4)
            print('첫번째 턴이 아니므로 컴퓨터가 술래')
            print(f'이번엔~ 몇호선 ~?? {line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!! {line_num}호선!!!')


        if line_num == 1:
            last += 5
        elif line_num == 2:
            last += 6
        elif line_num == 3:
            last += 8
        elif line_num == 4:
            last += 9
        elif line_num == 5:
            last += 10
        elif line_num == 6:
            last += 11
        elif line_num == 7:
            last += 12
        elif line_num == 8:
            last += 14
        elif line_num == 9:
            last += 15
        else:
            print('1~9호선 중 선택하여 주십시오')


        
        response = requests.get(f'https://transit.navitime.com/ko/kr/line/0000000{last}')
        soup = BeautifulSoup(response.text, 'html.parser')

        metro_list = [word.get_text() for word in soup.select("body > div:nth-of-type(2) > div > div:nth-of-type(1) > ol > li > a > span.name")]




        if turn == 1:
            station = input(f'{line_num}호선에 해당하는 역을 입력해주세요: ')
            turn += 1
            if station in metro_list :
                print('맞았습니다!')
            else:
                print('틀렸습니다!!')
                break
        else:
            auto_answer = random.sample(metro_list, 4)
            print('다른 플레이어의 응답 : ',auto_answer)
            break
            # 내가 술래가 아니고 컴퓨터부터 시작

subway_game()