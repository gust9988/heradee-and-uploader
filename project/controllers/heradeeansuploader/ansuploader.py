from flask import Blueprint, render_template, request
from project.modules.imagePillow import pilimgs3, pilimg

bp = Blueprint('ansupload', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')

    elif request.method == 'POST':
        if request.form.get('action') == 'anssubmit':

            # SLIDE
            for i in range(1, 9):
                if not request.files['slide' + str(i)]:
                    pass
                else:
                    pilimgs3(request.files['slide' + str(i)],
                             pilimg(request.files['slide' + str(i)]).size[0],
                             pilimg(request.files['slide' + str(i)]).size[1],
                             f'ans/{request.form.get("ans_account")}/slide/',
                             f'{i}.jpg')

            # PROFILE
            if request.files['profile']:
                pilimgs3(request.files['profile'],
                         pilimg(request.files['profile']).size[0],
                         pilimg(request.files['profile']).size[1],
                         f'ans/{request.form.get("ans_account")}/profile/',
                         '1.jpg')

            if request.form.get('aboutme'):




            return render_template('upload.html')

