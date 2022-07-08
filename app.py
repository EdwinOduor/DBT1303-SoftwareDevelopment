from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask (__name__)
app.secret_key = "12233ados"

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:password12@localhost/school'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    student_no = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    address = db.Column(db.String(100))
    program = db.Column(db.String(100))
    course = db.Column(db.String(100))
    document = db.Column(db.String(100))

    def __init__(self, name, student_no, phone, address, program, course, document):
        self.name = name
        self.student_no = student_no
        self.phone = phone
        self.address = address
        self.program =program
        self.course = course
        self.document = document

@app.route('/')
def index():
    all_data = Students.query.all()

    return render_template("index.html", students = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        student_no = request.form['student']
        phone = request.form['phone']
        address = request.form['address']
        program = request.form['program']
        course = request.form['course']
        document = request.form['document']

        my_data = Students(name,student_no,phone,address,program,course,document)
        db.session.add(my_data)
        db.session.commit()

        flash("Student added successfully")

        return redirect(url_for('index'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = Students.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.student_no = request.form['student']
        my_data.phone = request.form['phone']
        my_data.address = request.form['address']
        my_data.program = request.form['program']
        my_data.course = request.form['course']
        my_data.document = request.form['document']

        db.session.commit()
        flash("Student updated successfully")

        return redirect(url_for('index'))


@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Students.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Student deleted successfully")

    return redirect(url_for('index'))




if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)