from project import db


class Ans(db.Model):
    __tablename__ = 'ans'

    ans_id = db.Column(db.Integer, primary_key=True)
    ans_user_id = db.Column(db.Integer)
    ans_account = db.Column(db.String(100))
    ans_user_type = db.Column(db.String(50))
    ans_dp_name = db.Column(db.String(50))
    ans_dp_introduce = db.Column(db.Text)
    ans_about_me_name = db.Column(db.String(50))
    ans_about_me_content = db.Column(db.Text)
    ans_artist_fb = db.Column(db.Text)
    ans_artist_ig = db.Column(db.Text)
    ans_artist_yt = db.Column(db.Text)
    ans_artist_tw = db.Column(db.Text)
    ans_artist_sp = db.Column(db.Text)
    ans_artist_sc = db.Column(db.Text)
    ans_artist_am = db.Column(db.Text)
    ans_artist_tt = db.Column(db.Text)
    ans_artist_contact = db.Column(db.Text)
    donate = db.Column(db.Text)

class Ansport(db.Model):
    __tablename__ = 'ansportfolio'

    port_id = db.Column(db.Integer, primary_key=True)
    port_account = db.Column(db.String(100), nullable=False)
    port_cont = db.Column(db.Text, nullable=False)
    port_cont_id = db.Column(db.Integer)
    port_url = db.Column(db.Text)