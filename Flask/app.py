from flask import Flask, render_template,request,redirect,url_for

app=Flask(__name__)

@app.route("/")
def welcome():
  return "Welcome to this Flask course. This is best course"

@app.route("/index")
def index():
  return render_template('index.html')

@app.route("/form", methods=['GET','POST'])
def form():
  if request.method=='POST':
    name=request.form['name']
    return f'Hello {name}!!!'
  return render_template('form.html')

'''
##variable rule - it is happening by jinja 2 template engine ( It read data source from backend to html page) 

{{ }} to print output in html
{% %} conditions, for loops
{# #} this is for comments
'''

@app.route('/sucess/<int:score>')
def success(score):
  res=""
  if score>=50:
    res="Pass"

  else:
    res="Fail"

  return render_template('result.html',results=res)


@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data = float(request.form['data'])

        total_score = (science + maths + c + data) / 4
        return redirect(url_for('success', score=total_score))

    return render_template('submit.html')


if __name__ =="__main__":
  app.run(debug=True)