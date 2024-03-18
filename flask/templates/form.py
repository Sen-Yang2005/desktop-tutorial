from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class QuestionnaireForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    student_number = StringField('Student Number', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    english_grades = StringField('English for Academic Purposes', validators=[InputRequired()])
    programming_theory_grades = StringField('Programming Theory', validators=[InputRequired()])
    programming_practical_grades = StringField('Programming Practical Applications', validators=[InputRequired()])
    extended_project_grades = StringField('Extended Project', validators=[InputRequired()])
    math_grades = StringField('Intermediate Mathematics', validators=[InputRequired()])
    satisfaction = SelectField('Overall satisfaction with the academic experience',
                               choices=[('Very satisfied', 'Very satisfied'),
                                        ('Generally satisfied', 'Generally satisfied'),
                                        ('Relatively dissatisfied', 'Relatively dissatisfied'),
                                        ('Very dissatisfied', 'Very dissatisfied')],
                               validators=[InputRequired()])
    feedback_points = TextAreaField('Which points you think you have done well', validators=[InputRequired()])
    suggestions = TextAreaField('Suggestions for improvement', validators=[InputRequired()])
    submit = SubmitField('Submit')
