import requests
import random
from bs4 import BeautifulSoup as bs
from pprint import pprint

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

    while True:
        turn = 1
        last = 0
        line_num = int(input('1호선 ~ 9호선 선택해주세요! : '))
        print(f'{line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!! {line_num}호선!!!')

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

        print(f'{last}last')
        
        response = requests.get(f'https://transit.navitime.com/ko/kr/line/0000000{last}')
        soup = BeautifulSoup(response.text, 'html.parser')

        metro_list = [word.get_text() for word in soup.select("body > div:nth-of-type(2) > div > div:nth-of-type(1) > ol > li > a > span.name")]

        try:
            if turn == 1:
                station = input(f'{line_num}호선에 해당하는 역을 입력해주세요: ')
                turn += 1
                if station in metro_list :
                    print('#이후로 컴퓨터가 이어나감')
                    break
                break
            else:
                print('첫번째 턴이 아니므로 컴퓨터가 술래')
                # 내가 술래가 아니고 컴퓨터부터 시작
                break

        except:print('트라이문의except')

subway_game()