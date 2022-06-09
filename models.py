from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    ho_va_ten = db.Column(db.String(50), primary_key=True)
    ngay_sinh = db.Column(db.Date, nullable=False)
    so_dien_thoai = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ten_dang_nhap = db.Column(db.String(80), nullable=False)
    mat_khau = db.Column(db.String(80), nullable=False)

    
def __init__(self, ho_va_ten, ngay_sinh, so_dien_thoai, email, ten_dang_nhap, mat_khau):
    self.ho_va_ten = ho_va_ten
    self.ngay_sinh = ngay_sinh
    self.so_dien_thoai = so_dien_thoai
    self.email = email
    self.ten_dang_nhap = ten_dang_nhap
    self.mat_khau = mat_khau



class Mon_hoc(db.Model):
    __tablename__ = 'mon_hoc'
    ma_mon_hoc = db.Column(db.Integer, primary_key=True)
    ten_mon_hoc = db.Column(db.String(80), nullable=False)
    nhom = db.Column(db.Integer, nullable=False)
    so_tin_chi = db.Column(db.Integer, nullable=False)
    giang_vien = db.Column(db.String(80), nullable=False)
    lop = db.Column(db.String(30), db.ForeignKey("hssv.lop"), nullable=False)



class Diem(db.Model):
    __tablename__ = 'diem'
    stt = db.Column(db.Integer, primary_key=True)
    ma_mon_hoc = db.Column(db.Integer, db.ForeignKey("mon_hoc.ma_mon_hoc"), nullable=False)
    ten_mon_hoc = db.Column(db.String(80), nullable=False)
    diem_c = db.Column(db.Float, nullable=False)
    diem_b = db.Column(db.Float, nullable=False)
    diem_a = db.Column(db.Float, nullable=False)
    diem_tong_ket = db.Column(db.Float, nullable=False)
    


class HSSV(db.Model):
    __tablename__ = 'hssv'
    lop = db.Column(db.String(30), primary_key=True)
    ma_sinh_vien = db.Column(db.Integer, nullable=False)
    ho_va_ten = db.Column(db.String(50), db.ForeignKey("users.ho_va_ten"), nullable=False)
    ngay_sinh = db.Column(db.Date, nullable=False)
    gioi_tinh = db.Column(db.String(10), nullable=False)
    dia_chi = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    so_dien_thoai = db.Column(db.Integer, nullable=False)