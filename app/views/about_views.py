from flask import Blueprint, render_template

# 우리가 부를 이름, flask 프레임워크가 찾을 이름, 라우팅주소
fisa = Blueprint('about', __name__, url_prefix='/fisa')

@fisa.route('/')
def aboutme():
    return render_template('about_me.html')