from flask import Flask, redirect, url_for
app = Flask(__name__)
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number: %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo

@app.route('/name/<myname>')
def myname(myname):
    return 'My name is %s' % myname

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('myname',myname = name))
if __name__ == '__main__':
    app.run(debug = True)5