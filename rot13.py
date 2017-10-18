'''
requirements 
Python version - 3
flask

Rot13 converter
'''

from string import ascii_lowercase as low
from string import ascii_uppercase as upp
from flask import Flask,request,render_template
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('rot13.html',output="")

@app.route('/',methods=['POST'])
def rot13():
	s = request.form['q']
	rot13 = ''
	for i in s:
		if i.isupper():
			rot13 += upp[(upp.index(i) + 13) % 26]
		elif i.islower():
			rot13 += low[(low.index(i) + 13) % 26]
		else:
			rot13 += i
	#return rot13
	return render_template('rot13.html', output=rot13)

if __name__=='__main__':
	app.run(debug=True)
