from flask import Blueprint, render_template
from app.models import Question
from app.models import Answer

# 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
fisa = Blueprint('basic', __name__, url_prefix='/fisa')

@fisa.route('/post')
def post_list():
    question_list = Question.query.all()
    return render_template('question/question_list.html', question_list=question_list)

@fisa.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get(question_id)
    return render_template('question/question_detail.html', question=question)

@fisa.route('/loop')
def loop():
    test = [1,2,3,4,5]
    return render_template('test.html', list=test)


@fisa.route('/')
def index():
    return render_template('index.html')