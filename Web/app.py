# file name : app.py
# pwd : /Web/app.py 
import os
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import module.DBTmodule as db
import module.DBTmodule2 as mdb
import module.DBTmodule3 as cdb


app = Flask(__name__)

# 로그인 전 게시판 메인 화면
@app.route('/')
def mainboard():
    data_list = db.selectDB()
    print(data_list)
    return render_template('mainboard.html', data_list=data_list)

# 로그인 후 게시판 메인 화면
@app.route('/after')
def aftermainboard(m_id):
    data_list = db.selectDB()
    return render_template('aftermainboard.html', data_list=data_list, m_id=m_id)

# 글쓰기
@app.route('/write', methods=['POST'])
def write():
    m_id=request.form.get('m_id')
    data=mdb.searchidMDB(m_id)
    m_name=data[0][0]
    return render_template("write.html", m_name=m_name)

@app.route('/write_action', methods=['POST'])
def write_action():
    title=request.form.get('title')
    content=request.form.get('content')

    file= request.files['uploadfile']
    path = 'static/file/' + secure_filename(file.filename)
    file.save(path)
    
    print(path)
    writer=request.form.get('writer')


    data=mdb.searchnameMDB(writer)
    m_id=data[0][0]
        
    db.insertDB(writer, title, content, path)

    return aftermainboard(m_id)
    

# 댓글 쓰기
@app.route('/cwrite_action', methods=['POST'])
def cwrite_action():
    title=request.form.get('title')
    writer=request.form.get('writer')
    content=request.form.get('content')
    idx=request.form.get('idx')
    m_id=request.form.get('m_id')

    cdb.insertDB(idx, writer, title, content)

    data1=db.searchidDB(idx)
    data2=mdb.searchidMDB(m_id)
    data_list=cdb.searchidDB(idx)
    
    if data1[0][2]==data2[0][0]:
        return render_template("read.html", data=data1, m_id=m_id, m_name=data2[0][0], data_list=data_list)
    else:
        return render_template("readonly.html", data=data1, m_id=m_id, m_name=data2[0][0], data_list=data_list)

# 글 읽기
@app.route('/read', methods=['POST'])
def read():
    title=request.form.get('title')
    data=db.searchtitleDB(title)
    m_id=request.form.get('m_id')
    idx=request.form.get('idx')
    if m_id is None:
        return render_template("login.html")
    else : 
        data2=mdb.searchidMDB(m_id)
        
        data_list=cdb.searchidDB(idx)
    
    path=data[0][5]
    fn=os.path.basename(path)
    print(fn)
    
    if data[0][2]==data2[0][0]:
        return render_template("read.html", data=data, m_id=m_id, m_name=data2[0][0], data_list=data_list, fn=fn)
    else:
        return render_template("readonly.html", data=data, m_id=m_id, m_name=data2[0][0], data_list=data_list, fn=fn)

# 게시글의 파일 다운로드
@app.route('/download_file', methods=['POST'])
def download_file():
    return send_file('./'+request.form['file'],as_attachment=True)
    

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
        content2=i[4]
        file2=i[5]
    title1=request.form.get('title')
    content1=request.form.get('content')
    file1=request.files['file']

    db.updatetitleDB(title1, title2)
    db.updatecontentDB(content1, content2)    
    db.updatefileDB(file1, file2)

    return mainboard()

# 글 삭제
@app.route('/delete', methods=['POST'])
def delete():
    id=request.form.get('id')
    db.deleteDB(id)

    return mainboard()

# 목록으로 돌아가기
@app.route('/back', methods=['POST'])
def back():
    m_id=request.form.get('m_id')
    return aftermainboard(m_id)

# 검색
@app.route('/search', methods=['POST'])
def search():
    search=request.form.get('search')
    choice=request.form.get('choice')
    
    if choice == 'title':
        datalist = db.searchtitleDB(search)
    elif choice == 'content':
        datalist = db.searchcontentDB(search)
    elif choice == 'all':
        data_dump = db.searchcontentDB(search)
        data_dump += db.searchnameDB(search)
        data_dump += db.searchtitleDB(search)
        datalist = list(set(data_dump))   
    else:
        data_dump = db.searchcontentDB(search)
        data_dump += db.searchnameDB(search)
        data_dump += db.searchtitleDB(search)
        datalist = list(set(data_dump))   
    

    return render_template('search.html', data_list=datalist)

# 회원가입
@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signup_action', methods=['POST'])
def signup_action():
    m_id=request.form.get('id')
    m_pwd=request.form.get('pwd')
    m_name=request.form.get('name')
    m_email=request.form.get('email')
    m_school=request.form.get('school')
    m_file= request.files['file']
    path = 'static/profile/' + secure_filename(m_file.filename)
    m_file.save(path)

    mdb.insertMDB(m_name, m_id, m_pwd, path, m_email, m_school)
    return mainboard()

#로그인
@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login_action', methods=['POST'])
def login_action():
    m_id=request.form.get('id')
    m_pwd=request.form.get('pwd')
        
    data1=mdb.searchidMDB(m_id)
    data2=mdb.searchpwdMDB(m_pwd)

    if data1==data2:
        return aftermainboard(m_id=m_id)
    else:
        return '로그인 실패'
        
# 로그아웃
@app.route('/logout')
def logout():
    return mainboard()

# 아이디 찾기
@app.route('/findid')
def findid():
    return render_template("findid.html")

@app.route('/findid_action', methods=['POST'])
def findid_action():
    m_name=request.form.get('name')
    m_email=request.form.get('email')
    m_shcool=request.form.get('school')
    
    data1=mdb.searchnameMDB(m_name)
    data2=mdb.searchemailMDB(m_email)
    data3=mdb.searchschoolMDB(m_shcool)
    
    if data1==data2:
        if data2==data3:
            return '아이디는 '+data1[0][1]+'입니다'

    return '가입된 정보가 없습니다.'

# 비밀번호 찾기
@app.route('/findpwd')
def findpwd():
    return render_template("findpwd.html")

@app.route('/findpwd_action', methods=['POST'])
def findpwd_action():
    m_id=request.form.get('id')
    m_name=request.form.get('name')
    m_email=request.form.get('email')
    m_shcool=request.form.get('school')
    
    data1=mdb.searchidMDB(m_id)
    data2=mdb.searchnameMDB(m_name)
    data3=mdb.searchemailMDB(m_email)
    data4=mdb.searchschoolMDB(m_shcool)
    
    if data1==data2:
        if data2==data3:
            if data3==data4:
                return '비밀번호는 '+data1[0][2]+'입니다'

    return '가입된 정보가 없습니다.'


# 내 프로필
@app.route('/myprofile', methods=['POST'])
def myprofile():
    m_id=request.form.get('m_id')
    data=mdb.searchidMDB(m_id)
    return render_template("myprofile.html", data=data)
    
# 프로필 수정
@app.route('/updateprofile', methods=['POST'])
def updateprofile():
    m_name=request.form.get('m_name')
    data=mdb.searchnameMDB(m_name)
    return render_template("updateprofile.html", data=data)

@app.route('/updateprofile_action', methods=['POST'])
def updateprofile_action():
    m_id=request.form.get('id')
    data=mdb.searchidMDB(m_id)

    for i in data:
        name=i[0]
        pwd=i[2]
        path=i[3]
        email=i[4]
        school=i[5]
    m_pwd=request.form.get('pwd')
    m_name=request.form.get('name')
    m_email=request.form.get('email')
    m_school=request.form.get('school')
    m_file= request.files['file']
    m_path = 'static/profile/' + secure_filename(m_file.filename)
    m_file.save(m_path)

    mdb.updatenameMDB(m_name, name)
    mdb.updatepwdMDB(m_pwd, pwd)
    mdb.updateemailMDB(m_email, email)
    mdb.updateschoolMDB(m_school, school)
    mdb.updateimgMDB(m_path, path)
    
    return aftermainboard(m_id=m_id)
    
# 회원탈퇴
@app.route('/deletemember', methods=['POST'])
def deletemember():
    m_id=request.form.get('id')
    mdb.deleteMDB(m_id)
    return mainboard()

# 다른 사람 프로필
@app.route('/profile', methods=['POST'])
def profile():
    name=request.form.get('m_name')
    data=mdb.searchnameMDB(name)
    return render_template("profile.html", data=data)

if __name__ == '__main__':
    app.run()             
