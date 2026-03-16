from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Yourpassword",
    database="course_db"
)

cursor = db.cursor()


# ---------------- HOME ----------------

@app.route('/')
def home():
    return render_template('index.html')


# ---------------- COURSES ----------------

@app.route('/courses')
def courses():

    cursor.execute("""
    SELECT 
    Course.course_id,
    Course.course_name,
    Course.credits,
    Course.semester,
    Program.program_name,
    Department.dept_name,
    Instructor.instructor_name

    FROM Course

    LEFT JOIN Program 
    ON Course.program_id = Program.program_id

    LEFT JOIN Department 
    ON Course.dept_id = Department.dept_id

    LEFT JOIN Instructor 
    ON Course.instructor_id = Instructor.instructor_id
    """)

    data = cursor.fetchall()

    return render_template('courses.html', courses=data)


@app.route('/add_course', methods=['GET','POST'])
def add_course():

    if request.method == 'POST':

        name = request.form['name']
        credits = request.form['credits']
        semester = request.form['semester']

        sql = """
        INSERT INTO Course(course_name,credits,semester)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,(name,credits,semester))
        db.commit()

        return redirect('/courses')

    return render_template('add_course.html')


# ---------------- PROGRAMS ----------------

@app.route('/programs')
def programs():

    cursor.execute("SELECT * FROM Program")

    data = cursor.fetchall()

    return render_template('programs.html', programs=data)


@app.route('/add_program', methods=['GET','POST'])
def add_program():

    if request.method == 'POST':

        name = request.form['name']
        duration = request.form['duration']
        degree = request.form['degree']

        sql = """
        INSERT INTO Program(program_name,duration,degree_type)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,(name,duration,degree))
        db.commit()

        return redirect('/programs')

    return render_template('add_program.html')


# ---------------- DEPARTMENTS ----------------

@app.route('/departments')
def departments():

    cursor.execute("SELECT * FROM Department")

    data = cursor.fetchall()

    return render_template('departments.html', departments=data)


@app.route('/add_department', methods=['GET','POST'])
def add_department():

    if request.method == 'POST':

        name = request.form['name']
        building = request.form['building']
        email = request.form['email']

        sql = """
        INSERT INTO Department(dept_name,building,contact_email)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,(name,building,email))
        db.commit()

        return redirect('/departments')

    return render_template('add_department.html')


# ---------------- INSTRUCTORS ----------------

@app.route('/instructors')
def instructors():

    cursor.execute("SELECT * FROM Instructor")

    data = cursor.fetchall()

    return render_template('instructors.html', instructors=data)


@app.route('/add_instructor', methods=['GET','POST'])
def add_instructor():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        designation = request.form['designation']

        sql = """
        INSERT INTO Instructor(instructor_name,email,designation)
        VALUES(%s,%s,%s)
        """

        cursor.execute(sql,(name,email,designation))
        db.commit()

        return redirect('/instructors')

    return render_template('add_instructor.html')


# ---------------- RUN SERVER ----------------

if __name__ == "__main__":
    app.run(debug=True)