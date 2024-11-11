from flask import Flask, render_template, request, jsonify
from time import strftime
app = Flask(__name__)


class HalloApp:
    def __init__(self):
        self.time = self.get_time()

    def get_time(self):
        return strftime("%H:%M:%S")

    def greet(self, name):
        return f"Hallo {name}"


hallo_app = HalloApp()


@app.route('/', methods=['GET', 'POST'])
def index():

    current_time = hallo_app.get_time()
    if request.method == 'POST':
        name = request.form['name']
        greeting = hallo_app.greet(name)
        return render_template('result.html', greeting=greeting, current_time=current_time)
    return render_template('index.html', current_time=current_time)


@app.route('/time')
def get_time():
    current_time = hallo_app.get_time()
    return jsonify({'time': current_time})


if __name__ == "__main__":
    app.run(debug=True)
