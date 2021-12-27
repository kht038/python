from flask import Flask, render_template, request, redirect, url_for
import pymysql

db = pymysql.connect(host="localhost",
                     user="root",
                     passwd="rhxogud@0804@",
                     db="flask",
                     charset="utf8")
cur = db.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    sql = "SELECT * from post"  # 실행할 쿼리 문
    cur.execute(sql)  # 실행
    data_list = cur.fetchall()  # 쿼리문으로 나온 결과 를 저장

    return render_template('index.html', data_list=data_list)  # 왼쪽이 html, 오른쪽이 파이썬에서 사용하는 변수명


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/test', methods=['GET', 'POST'])
def complete():
    if request.method == 'POST':
        title = request.form.get("title")
        author = request.form.get("author")
        contents = request.form.get("contents")

        insert = "INSERT INTO post VALUES('%s', '%s', '%s')" % (title, author, contents)
        cur.execute(insert)  # 메소드로 전달
        data = cur.fetchall()  # 실행한 결과의 데이터를 꺼냄

        if not data:
            db.commit()
            return redirect('/')

        else:
            db.rollback()
            return "실패"

    return render_template('index.html')

