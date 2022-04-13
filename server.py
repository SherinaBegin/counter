from flask import Flask, render_template, request, redirect, session 
app = Flask(__name__)
app.secret_key = 'averysecretkey'

@app.route('/')
def counter():
   if 'counter' not in session:
      session['counter'] = 0
   else:
      session['counter']+= 1
   return render_template('index.html')

@app.route('/plusTwo')
def plus_two():
   session['counter'] += 1
   return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
   session['counter'] += int(request.form['increment']) -1 #because redirect adds one we subtract one. 
   return redirect('/')


@app.route('/destroy_session')
def clear_session():
   session.pop('counter') #pop clears specific key name / clear clears ALL key names
   return redirect('/')

if __name__ == '__main__':
   app.run(debug=True)