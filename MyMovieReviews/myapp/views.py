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
                <p><textarea name="body" placeholder="영화 리뷰"></textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
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
                    "body":topic['body']
                }
        article = f'''
            <form action="/update/{id}/" method="post">
                <p><input type="text" name="title" placeholder="title" value={selectedTopic["title"]}></p>
                <p><textarea name="body" placeholder="body">{selectedTopic['body']}</textarea></p>
                <p><input type="submit"></p>
            </form>
        '''
        return HttpResponse(HTMLTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}')