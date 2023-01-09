import requests
from bs4 import BeautifulSoup
from pprint import pprint



def brGame() :
    
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


    line_num = input('1호선 ~ 9호선 선택해주세요! : ')

    while True:

        turn = 1

        line_num = input('1호선 ~ 9호선 선택해주세요! : ')

        print(f'{line_num}호선~ {line_num}호선! {line_num}호선!! {line_num}호선!!!')

        if line_num == 1:
            last = 5
        elif line_num == 2:
            last = 6
        elif line_num == 3:
            last = 8
        elif line_num == 4:
            last = 8
        elif line_num == 5:
            last = 10
        elif line_num == 6:
            last = 11
        elif line_num == 7:
            last = 13
        elif line_num == 8:
            last = 14
        elif line_num == 9:
            last = 15
        
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
            else:
                print('첫번째 턴이 아니므로 컴퓨터가 술래')
                # 내가 술래가 아니고 컴퓨터부터 시작
                break
                

brGame()