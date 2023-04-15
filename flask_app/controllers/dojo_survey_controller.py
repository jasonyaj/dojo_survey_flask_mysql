from flask import session, render_template, request, redirect
from flask_app import app
from flask_app.models.dojo_survey_model import Student

# landing page
@app.route('/')
def index():
    return render_template('index.html')

# page to collect and transfer survey answers
@app.route('/process', methods=['POST'])
def process_form():
    new_student_survey = {
        'name' : request.form['name'],
        'location' : request.form['dojo_location'],
        'language' : request.form['favorite_language'],
        'comment' : request.form['comments']
    }
    # "if" statement to check for required fields
    if Student.validate_survey(new_student_survey) == False:
        return redirect("/")
    else:
        student_id = Student.add_survey( new_student_survey )
        session["name"] = request.form["name"]
        session["comment"] = request.form["comments"]
        return redirect('/result')

# results displayed on a user card
@app.route('/result')
def show_submitted_form():
    data = {
        'name' : session["name"],
        'comment': session["comment"]
    }
    current_survey = Student.get_survey(data)
    return render_template('result.html', current_survey = current_survey)