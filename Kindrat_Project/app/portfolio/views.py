from flask import render_template, request
from . import portfolio
from datetime import datetime
import os

my_skills = [
    'Python',
    'JavaScript',
    'HTML',
    'CSS',
    'Flask',
    'SQL',
]

@portfolio.route('/')
def home():
    os_type = os.name
    user_agent = request.headers.get('User-Agent')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('portfolio.html', os_type=os_type, user_agent=user_agent, current_time=current_time)

@portfolio.route('/resume')
def resume():
    return render_template('resume.html')

@portfolio.route('/skills')
@portfolio.route('/skills/<int:id>')
def skill(id=None):
    if id is None:
        return render_template('skills.html', skills=my_skills)
    elif id >= 0 and id < len(my_skills):
        return f"Skill {id}: {my_skills[id]}"
    else:
        return "Skill not found"