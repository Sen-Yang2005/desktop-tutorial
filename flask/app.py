from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)