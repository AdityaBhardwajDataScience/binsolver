from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return 'index.html'
    # return render_template('index.html')

@app.route('/solve',methods='POST')
def solve():
    equation = request.form['eq']
    return 'hello'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
