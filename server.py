from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')

# @app.route('/ninjas')
# def ninjas():
#     return render_template('ninjas.html')


@app.route('/users', methods=['POST'])
def dojoData():
    name = request.form['name']
    email = request.form['email']
    print name,email
    return redirect('/')

app.run(debug=True)
