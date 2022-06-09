from operator import or_
from flask import Flask, render_template, request, url_for, redirect, flash
from models import * 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:yourpass@127.0.0.1:5432/web"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secret"
db.init_app(app)



@app.route("/")
def index():
    return render_template("index.html")



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if not request.form['ho_va_ten'] or not request.form['ngay_sinh'] or not request.form['so_dien_thoai'] or not request.form['email'] or not request.form['ten_dang_nhap'] or not request.form['mat_khau'] or not request.form['mat_khau2']:
            flash("Vui lòng nhập đầy đủ thông tin")
            return render_template("register.html")
        else:
            if request.form['ten_dang_nhap'] == User.query.filter_by(ten_dang_nhap=request.form['ten_dang_nhap']).first():
                flash("Tên đăng nhập đã tồn tại")
                return render_template("register.html")
            elif request.form['mat_khau'] != request.form['mat_khau2']:
                flash("Mật khẩu không khớp")
                return render_template("register.html")
            else:
                user = User(request.form['ho_va_ten'], request.form['ngay_sinh'], request.form['so_dien_thoai'], request.form['email'], request.form['ten_dang_nhap'], request.form['mat_khau'])
                db.session.add(user)
                db.session.commit()
                return redirect(url_for("login"))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if not request.form['ten_dang_nhap'] or not request.form['mat_khau']:
            flash("Vui lòng nhập đầy đủ thông tin")
            return render_template("login.html")
        else:
            user = User.query.filter_by(ten_dang_nhap=request.form['ten_dang_nhap']).first()
            if user is None:
                flash("Tên đăng nhập không tồn tại")
                return render_template("login.html")
            elif user.mat_khau != request.form['mat_khau']:
                flash("Mật khẩu không đúng")
                return render_template("login.html")
            else:
                return redirect(url_for("home"))
    return render_template("login.html")



@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html")



if __name__ == "__main__":
    app.run(debug=True)
