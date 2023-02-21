from flask import Flask, render_template , url_for,redirect, flash , request, Blueprint
from Pack import app, db
from Pack.models import Student , Subject
from Pack.forms import RegisterUser, LoginUser, AddSubject
from flask_bcrypt import Bcrypt
from flask_login import login_user, current_user , logout_user , login_required

bcrypt = Bcrypt()
stds= Blueprint(
    'stds',
    __name__,
    url_prefix='/student'
)


@app.route('/')
def homepage():

    return render_template('homepage.html')

@stds.route('/register', methods=['GET','POST'])
def register():
    form = RegisterUser()
    if form.validate_on_submit():
        flash(f" Regestertion Completed {form.username.data}", "success")
        with app.app_context():
            hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf8')
            user = Student(username=form.username.data, email=form.email.data,password=hashed_password)
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/subject', methods=['GET','POST'])
def addSubjects():
    form = AddSubject()
    with app.app_context():
        students = Student.query.all()
        student_ids = [
                        student.id
                        for student in students
                       ]
        if form.validate_on_submit():
            with app.app_context():
                subj = Subject(title=form.title.data, student_id=request.form['student_id'])
                db.session.add(subj)
                db.session.commit()
            return redirect(url_for('homepage'))
    return render_template('subject.html', form=form, student_ids=student_ids)
#
@stds.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginUser()
    if form.validate_on_submit():
        std = Student.query.filter_by(username=form.username.data).first()
        if std and bcrypt.check_password_hash(std.password,form.password.data):
            login_user(std)
            flash(f" Login Successfully {form.username.data} ", "success")
            return redirect(url_for('homepage'))
        else:
            flash("try again", "warning")
            return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))
