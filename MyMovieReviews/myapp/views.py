from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

nextId = 4
topics = [
    {'id':1, 'title':'루카', 'body':'형제애와 우애를 느낄 수 있었습니다 픽사의 우정이야기', 'year':'2021', 'score':97, 'genre':'drama' ,'director':'엔리코 카사로사' ,'time':'100', 'actor':'루카'},
    {'id':2, 'title':'소울', 'body':'삶에서 진정 중요한 것이 무엇인지 느낄 수 있었던 이선재 인생 영화 2위','year':'2021', 'score':100, 'genre':'life','director':'피트 닥터' ,'time':'95', 'actor':'조,22'},
    {'id':3, 'title':'라야와 마지막 드래곤', 'body':'돌처럼 굳은 서로를 되돌릴 수 있는 것은 그보다 굳건한 진심', 'year':'2021', 'score':95, 'genre':'Humanity', 'director':'돈 홀' ,'time':'120', 'actor':'라야,시수'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = f'''
            <li><a href="/create/">리뷰 작성</a></li>
    '''
    if id != None:
        contextUI = f'''
            <li>
                <form action="/delete/" method="post">
                    <input type="hidden" name="id" value={id}>
                    <input type="submit" value="현재리뷰 삭제하기">
                </form>
            </li>
            <li><a href="/update/{id}">현재리뷰 수정하기</a></li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a><br>개봉 년도 : {topic["year"]}<br>평점 : {topic["score"]}<br>장르 : {topic["genre"]}</li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">MYMovieReviews</a></h1>
        {articleTag}
        <ul>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

def index(request):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a><br>개봉 년도 : {topic["year"]}<br>평점 : {topic["score"]}<br>장르 : {topic["genre"]}</li>'
    article = f'''
    <ol>
        {ol}
    </ol>
    <h2>영화리뷰 리스트페이지입니다</h2>
    리뷰는 해당 페이지를 통해 생성 가능합니다
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]} 디테일 페이지입니다<h2><h4>{topic["title"]}</h4>{topic["body"]}<br>감독 : {topic["director"]}<br>러닝타임 : {topic["time"]}<br>출연진 : {topic["actor"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <h2>리뷰 생성 페이지입니다<h2>
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="영화제목"></p>
                <p><input type="text" name="year" placeholder="개봉년도"></p>
                <p><input type="text" name="score" placeholder="평점"></p>
                <p><input type="text" name="genre" placeholder="장르"></p>
                <p><input type="text" name="director" placeholder="감독"></p>
                <p><input type="text" name="time" placeholder="러닝타임"></p>
                <p><input type="text" name="actor" placeholder="출연"></p>
                <p><textarea name="body" placeholder="영화 리뷰"></textarea></p>
                <p><input type="submit" value="저장"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        year = request.POST['year']
        score = request.POST['score']
        genre = request.POST['genre']
        director = request.POST['director']
        time = request.POST['time']
        actor = request.POST['actor']
        newTopic = {"id":nextId, "title":title, "body":body, 'year':year, 'score':score, 'genre':genre ,'director':director ,'time':time, 'actor':actor}
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        topics.append(newTopic)
        return redirect('/')

@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')

@csrf_exempt
def update(request,id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                selectedTopic = {
                    "title":topic['title'],
                    "body":topic['body'],
                    "year":topic['year'],
                    "score":topic['score'],
                    "genre":topic['genre'],
                    "director":topic['director'],
                    "time":topic['time'],
                    "actor":topic['actor']
                }
        article = f'''
        <h2>리뷰 수정 페이지입니다</h2>
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><input type="text" name="year" placeholder="year" value={selectedTopic["year"]}></p>
                <p><input type="text" name="score" placeholder="score" value={selectedTopic["score"]}></p>
                <p><input type="text" name="genre" placeholder="genre" value={selectedTopic["genre"]}></p>
                <p><input type="text" name="director" placeholder="director" value={selectedTopic["director"]}></p>
                <p><input type="text" name="time" placeholder="time" value={selectedTopic["time"]}></p>
                <p><input type="text" name="actor" placeholder="actor" value={selectedTopic["actor"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        year = request.POST['year']
        score = request.POST['score']
        genre = request.POST['genre']
        director = request.POST['director']
        time = request.POST['time']
        actor = request.POST['actor']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
                topic['year'] = year
                topic['score'] = score
                topic['genre'] = genre
                topic['director'] = director
                topic['time'] = time
                topic['actor'] = actor
        return redirect(f'/read/{id}')