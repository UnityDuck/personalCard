from flask import Flask, render_template
import random
import json
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

with open('templates/crew.json', 'r', encoding='utf-8') as f:
    crew_data = json.load(f)


@app.route('/member')
def member():
    random_member = random.choice(crew_data)

    sorted_specialties = sorted(random_member['specialties'])

    return render_template('member.html', member=random_member, specialties=sorted_specialties)


if __name__ == '__main__':
    app.run(debug=True)
