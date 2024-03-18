from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form import QuestionnaireForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set your secret key for CSRF protection
csrf = CSRFProtect(app)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/about')
def about_page():
    return render_template('about_page.html')

@app.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire_page():
    form = QuestionnaireForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Get form data
            first_name = form.first_name.data
            last_name = form.last_name.data
            student_number = form.student_number.data
            email = form.email.data
            english_grades = form.english_grades.data
            programming_theory_grades = form.programming_theory_grades.data
            programming_practical_grades = form.programming_practical_grades.data
            extended_project_grades = form.extended_project_grades.data
            math_grades = form.math_grades.data
            satisfaction = form.satisfaction.data
            feedback_points = form.feedback_points.data
            suggestions = form.suggestions.data

            # Store data in a text file
            with open('data.txt', 'a') as file:
                file.write(f'First Name: {first_name}\n')
                file.write(f'Last Name: {last_name}\n')
                file.write(f'Student Number: {student_number}\n')
                file.write(f'Email: {email}\n')
                file.write(f'English Grades: {english_grades}\n')
                file.write(f'Programming Theory Grades: {programming_theory_grades}\n')
                file.write(f'Programming Practical Grades: {programming_practical_grades}\n')
                file.write(f'Extended Project Grades: {extended_project_grades}\n')
                file.write(f'Math Grades: {math_grades}\n')
                file.write(f'Satisfaction: {satisfaction}\n')
                file.write(f'Feedback Points: {feedback_points}\n')
                file.write(f'Suggestions: {suggestions}\n')
                file.write('\n')  # Add a blank line to separate different form submissions

            return 'Form submitted successfully'
    return render_template('questionnaire.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
