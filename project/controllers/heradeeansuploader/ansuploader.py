from flask import Blueprint, render_template, request
from project import db
from project.models.model import Ans, Ansport
from project.modules.imagePillow import pilimgs3, pilimg

bp = Blueprint('ansupload', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    elif request.method == 'POST':
        if request.form.get('action') == 'anssubmit':

            # SLIDE PICS
            for i in range(1, 9):
                if not request.files['slide' + str(i)]:
                    pass
                else:
                    pilimgs3(request.files['slide' + str(i)],
                             pilimg(request.files['slide' + str(i)]).size[0],
                             pilimg(request.files['slide' + str(i)]).size[1],
                             f'ans/{request.form.get("ans_account")}/slide/',
                             f'{i}.jpg')

            # PROFILE PICS
            if request.files['profile']:
                pilimgs3(request.files['profile'],
                         pilimg(request.files['profile']).size[0],
                         pilimg(request.files['profile']).size[1],
                         f'ans/{request.form.get("ans_account")}/profile/',
                         '1.jpg')

            # ABOUT CONTENT
            if request.form.get('aboutme'):
                ansuser = Ans.query.filter(Ans.ans_account == request.form.get("ans_account")).first()
                ansuser.ans_about_me_content = request.form.get('aboutme')

            # PORTFOLIO
            if request.files['portfolio'] and request.form.get('portcont'):
                ansport = Ansport()
                ansport.port_account = request.form.get('ans_account')
                ansport.port_cont_id = request.form.get('portnum')
                ansport.port_cont = request.form.get('portcont')
                pilimgs3(request.files['portfolio'],
                         pilimg(request.files['portfolio']).size[0],
                         pilimg(request.files['portfolio']).size[1],
                         f'ans/{request.form.get("ans_account")}/portfolio/',
                         f'{request.form.get("portnum")}.jpg')
                db.session.add(ansport)

            db.session.commit()
            return render_template('upload.html')

