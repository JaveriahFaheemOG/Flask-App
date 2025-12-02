from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class FirstApp(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"{self.sno} - {self.fname}"


@app.route('/')
def index():
    users = FirstApp.query.all()
    return render_template('index.html', users=users)


@app.route('/add', methods=['POST'])
def add_user():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    phone = request.form['phone']

    new_user = FirstApp(fname=fname, lname=lname, email=email, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update_user(sno):
    user = FirstApp.query.get_or_404(sno)
    if request.method == 'POST':
        user.fname = request.form['fname']
        user.lname = request.form['lname']
        user.email = request.form['email']
        user.phone = request.form['phone']

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', user=user)


@app.route('/delete/<int:sno>')
def delete_user(sno):
    user = FirstApp.query.get_or_404(sno)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
  