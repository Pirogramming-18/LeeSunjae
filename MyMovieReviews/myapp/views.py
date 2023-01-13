from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

nextId = 4
topics = [
    {'id':1, 'title':'루카', 'body':'루카 내용', 'year':'2021', 'score':97, 'genre':'drama' ,'director':'엔리코 카사로사' ,'time':'100', 'actor':'루카'},
    {'id':2, 'title':'소울', 'body':'소울 내용','year':'2021', 'score':100, 'genre':'life','director':'피트 닥터' ,'time':'95', 'actor':'조,22'},
    {'id':3, 'title':'라야와 마지막 드래곤', 'body':'라야 내용', 'year':'2021', 'score':95, 'genre':'Humanity', 'director':'돈 홀' ,'time':'120', 'actor':'라야,시수'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
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
        <ol>
            {ol}
        </ol>
        {articleTag}
        <ul>
            <li><a href="/create/">리뷰 생성하기</a></li>
            {contextUI}
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>영화리뷰입니다</h2>
    리뷰는 생성,삭제,수정 가능합니다
    '''
    return HttpResponse(HTMLTemplate(article))

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}<br>감독 : {topic["director"]}<br>러닝타임 : {topic["time"]}<br>출연진 : {topic["actor"]}'
    return HttpResponse(HTMLTemplate(article, id))

@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
            <form action="/create/" method="post">
                <p><input type="text" name="title" placeholder="영화제목"></p>
                <p><input type="text" name="year" placeholder="개봉년도"></p>
                <p><input type="text" name="score" placeholder="평점"></p>
                <p><input type="text" name="genre" placeholder="장르"></p>
                <p><input type="text" name="director" placeholder="감독"></p>
                <p><input type="text" name="time" placeholder="러닝타임"></p>
                <p><input type="text" name="actor" placeholder="출연"></p>
                <p><textarea name="body" placeholder="영화 리뷰"></textarea></p>
                <p><input type="submit"></p>
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
        return redirect(url)

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