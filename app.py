from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
import socket

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'
    id     = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name   = db.Column(db.String(100), nullable=False)
    email  = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(100), default='General')
    def to_dict(self):
        return {'id': self.id, 'name': self.name,
                'email': self.email, 'course': self.course}

# FIXED: runs at module level — works with gunicorn
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return jsonify({'message': 'Student Registration API is running!',
                    'server': socket.gethostname()})

@app.route('/students', methods=['GET'])
def get_all_students():
    return jsonify([s.to_dict() for s in Student.query.all()])

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({'error': 'name and email are required'}), 400
    if Student.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'A student with this email already exists'}), 409
    s = Student(name=data['name'], email=data['email'],
                course=data.get('course', 'General'))
    db.session.add(s)
    db.session.commit()
    return jsonify({'message': 'Student added!', 'student': s.to_dict()}), 201

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    s = db.session.get(Student, student_id)
    return jsonify(s.to_dict()) if s else (jsonify({'error': 'Not found'}), 404)

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    s = db.session.get(Student, student_id)
    if not s: return jsonify({'error': 'Not found'}), 404
    data = request.get_json()
    if data.get('name'):   s.name   = data['name']
    if data.get('course'): s.course = data['course']
    db.session.commit()
    return jsonify({'message': 'Student updated!', 'student': s.to_dict()})

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    s = db.session.get(Student, student_id)
    if not s: return jsonify({'error': 'Not found'}), 404
    db.session.delete(s)
    db.session.commit()
    return jsonify({'message': f'Student {student_id} deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
