from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
   dict = {'phy':40,'che':50,'maths':100}
   return render_template('result.html', result = dict)

if __name__ == '__main__':
   app.run(debug = True)