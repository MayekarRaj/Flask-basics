from flask import Flask, redirect, url_for, render_template, request, session
app = Flask(__name__)
app.secret_key = "qwerty9009"

'''
{%  %} conditional statements. for loops
{{  }} expression and variables
{#   } comments
'''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('results.html', result = "PASS", marks = score)

@app.route('/fail/<int:score>')
def fail(score):
    return render_template('results.html', result = "FAIL", marks = score)

@app.route('/results/<int:score>')
def results(score):
    all_marks = session.get('all_marks')
    res = ''
    if score < 50:
        res = 'FAIL'
    else: 
        res = 'PASS'
    return render_template('results.html', result = res, marks = score, all_marks = all_marks)

### VARIABLE URL
# @app.route('/results/<int:marks>')
# def results(marks):
#     result = ""
#     if marks < 50:
#         result = "fail"
#     else:
#         result = "success"
#     return redirect(url_for(result, score = marks))

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_marks = ''
    all_marks = {}
    if request.method == 'POST':
        science = int(request.form['science'])
        maths = int(request.form['maths'])
        english = int(request.form['english'])
        hindi = int(request.form['hindi'])
        total_marks = (science + maths + english + hindi)/4

        all_marks['science'] = science
        all_marks['maths'] = maths
        all_marks['english'] = english
        all_marks['hindi'] = hindi

        session['all_marks'] = all_marks

        # res = ''

        # if total_marks < 50:
        #     res = 'fail'
        # else:
        #     res = 'success'
        
        return redirect(url_for('results', score = total_marks))



if __name__ == "__main__":
    app.run(debug=True)
