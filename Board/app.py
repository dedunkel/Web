# file name : app.py
# pwd : /Web/app.py 
 
from flask import Flask, render_template, request
import module.DBTmodule as db

app = Flask(__name__)

# 게시판 메인 화면
@app.route('/')
def mainboard():
    data_list = db.selectDB()
    return render_template('mainboard.html', data_list=data_list)

# 글쓰기
@app.route('/write')
def write():
    return render_template("write.html")

@app.route('/write_action', methods=['POST'])
def write_action():
    title=request.form.get('title')
    writer=request.form.get('writer')
    content=request.form.get('content')

    db.insertDB(writer, title, content)

    return mainboard()
    
# 글 읽기
@app.route('/read', methods=['POST'])
def read():
    title=request.form.get('title')
    data=db.searchtitleDB(title)

    return render_template("read.html", data=data)

# 글 수정
@app.route('/update', methods=['POST'])
def update():
    id=request.form.get('id')
    data=db.searchidDB(id)

    return render_template("update.html", data=data)

@app.route('/update_action', methods=['POST'])
def update_action():
    id=request.form.get('id')
    data=db.searchidDB(id)
    for i in data:
        title2=i[3]
        writer2=i[2]
        content2=i[4]
    title1=request.form.get('title')
    writer1=request.form.get('writer')
    content1=request.form.get('content')

    db.updatetitleDB(title1, title2)
    db.updatenameDB(writer1, writer2)
    db.updatecontentDB(content1, content2)    

    return mainboard()

# 글 삭제
@app.route('/delete', methods=['POST'])
def delete():
    id=request.form.get('id')
    db.deleteDB(id)

    return mainboard()

# 목록으로 돌아가기
@app.route('/back')
def back():
    return mainboard()

# 검색
@app.route('/search', methods=['POST'])
def search():
    search=request.form.get('search')
    choice=request.form.get('choice')
    
    if choice == 'title':
        data_list = db.searchtitleDB(search)
    elif choice == 'content':
        data_list = db.searchcontentDB(search)
    elif choice == 'all':
        data_dump = db.searchcontentDB(search)
        data_dump += db.searchnameDB(search)
        data_dump += db.searchtitleDB(search)
        data_list = list(set(data_dump))   
    
    return render_template('search.html', data_list=data_list)
    
if __name__ == '__main__':
    app.run()             
