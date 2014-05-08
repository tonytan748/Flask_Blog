from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user={'nickname':'Miguel'}
	posts=[{'author':{'nickname':'John'},'body':'Beautiful day in China!'},{'author':{'nickname':'Tony'},'body':'The acerage moive was so warm!'}]
	return render_template('index.html',title='Home',user=user,posts=posts)
