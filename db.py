from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "Welcome to home page"

# route to add students
@app.route('/add_student', methods=['POST'])
def add_student():
    if request.method == 'POST':
        data = request.get_json()

        name = data.get('name')
        email = data.get('email')

        new_student = Student(name=name, email=email)

        db.session.add(new_student)
        db.session.commit()

        return jsonify({'message': 'Student added successfully'})
    

# route to see all the students in the table 
@app.route('/get_students', methods=['GET'])
def get_students():
    students = Student.query.all()
    student_list = []

    for student in students:
        student_info = {
            'id': student.id,
            'name': student.name,
            'email': student.email
        }
        student_list.append(student_info)

    return jsonify(student_list)

# Route to access students by their id 
@app.route('/get_student/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    if student:
        return {
            'name': student.name,
            'email': student.email
        }
    else:
        return {'message': 'Student not found'}

if __name__ == '__main__':
    app.run(debug=True)
