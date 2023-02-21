from Pack import db, app
from Pack.models import Student , Subject
import sys
def create_db():
    with app.app_context():
        db.create_all()


def create_users():
    with app.app_context():
        user = Student(username='Omar', email='sssssss@gmail.com', password='123567')
        db.session.add(user)
        db.session.commit()

def create_use():
    with app.app_context():
        post = Subject(title='Physics', student_id=2)
        db.session.add(post)
        db.session.commit()


def read_users():
    with app.app_context():
        students = Student.query.all()
        student_ids = [
                       student.id
                       for student in students
                       ]
        print(student_ids)




if __name__ == '__main__':
    globals()[sys.argv[1]]()