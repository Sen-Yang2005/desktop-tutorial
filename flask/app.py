from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def home_page():
    return render_template("home_page.html")

@app.route('/about')
def about_page():
    return render_template('about_page.html')

@app.route('/questionnaire')
def questionnaire_page():
    return render_template('questionnaire_page.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        # 获取表单数据
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        student_number = request.form['student_number']
        email = request.form['email']
        english_grades = request.form['english_grades']
        programming_theory_grades = request.form['programming_theory_grades']
        programming_practical_grades = request.form['programming_practical_grades']
        extended_project_grades = request.form['extended_project_grades']
        math_grades = request.form['math_grades']
        satisfaction = request.form['satisfaction']
        feedback_points = request.form['feedback_points']
        suggestions = request.form['suggestions']

        # 将数据存储到文本文件
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
            file.write('\n')  # 添加空行以分隔不同的表单提交

    return 'Form submitted successfully'


if __name__ == '__main__':
    app.run(debug=True)