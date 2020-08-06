from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def aboutme():
    return render_template('aboutme.html')


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


@app.route('/socialnetworks')
def socialnetworks():
    return render_template('socialnetworks.html')


if __name__ == '__main__':
    app.run()
