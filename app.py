from flask import Flask, render_template
from flask import send_file

# TODO : javascript functions 


app = Flask(__name__)

@app.route('/')
def indexflask():
    return render_template('flaskcommand.html')

@app.route('/1')
def indexter():
    return render_template('terminalcommand.html')

@app.route('/2')
def indexpy():
    return render_template('pyComands.html')

@app.route('/3')
def indexkivi():
    return render_template('kivies.html')

@app.route('/code.png')
def code_png():
    return send_file('code.png', mimetype='image/png')



if __name__ == '__main__':
    app.run()
