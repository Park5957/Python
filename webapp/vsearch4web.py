# chap5_2 Head First pythin 의 내용에 대한 실습
# HTML

from contextlib import redirect_stderr
from unittest import result
from flask import Flask, render_template, request,redirect #서버 동작에 필요한 flask 모듈 읽어오기
from vsearch import search4letters #파일 vsearch를 제작해 해당 def를 돌린다.

app = Flask(__name__)      # Flask 객체 생성하여 app 변수명으로 할당.
                           # 객체 생성시 생성자에 __name__ 파이썬 인터프린터가
                           # 제공하는 기본값이다.
                           # 현재 활성 모듈의 이름을 가진다.
                           # 즉, Flask 의 기본 시작을 설정했다는 의미로 볼 수 있다.

@app.route("/")            # 사이트 접근주소(주소를 할당한다는 의미)
#@app.route("/entry")      # 해당 구문의 위치를 조정하면 스타트 위치를 효율적으로 조정할 수 있다.
                           # @는 decorator 이다.(장식자)
def hello() -> "302":      # 위 주소로 접근을 하면 이 함수가 실행된다.
    return redirect('/entry')   #entry 함수로 바로 이동


@app.route("/search4", methods = ["POST"])

def do_search() ->"html" :
    phrase = request.form['phrase']     #templates 의  entry 폴더 안의 phrase를 지정한 것이다.
    letters = request.form['letters']   #templates 의  entry 폴더 안의 letters 지정한 것이다.
    title = '찾은 결과입니다. :'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                            the_title=title,
                            the_phrase=phrase,
                            the_letters=letters,
                            the_results=results,)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='글자 찾기 사이트 방문을 환영합니다. by 박현용')

if __name__ == "__main__" : #웹사이트에서 실행제한을 걸기위한 용도
    app.run(debug=True)

# 로컬에서 테스트와 개발을 할 때는 app.run(debug=True)이 실행이 되어야 하지만
# 웹상에서 배포할 때는 실행되면 안된다.
# if __name__ == "__main__" :
# 을 넣으면 웹상에서 실행을 막게된다.
# 계속 지금처럼 로컬에서 웹앱을 개발할 수 있도록 한다.

# app.run()                # 웹 실행 요청
# app.run(debug=True)      # 자동으로 웹 실행을 갱신
