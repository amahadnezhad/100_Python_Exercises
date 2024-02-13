"""
Exercise 99
Question: Data Writer Web App

"""
# Answer
from flask import Flask, render_template_string, request
app = Flask(__name__)
html = """
        <div class="form">
            <form action="{{url_for('sent')}}" method="POST">
                <input title="Your Email Address Will Be Safe With Us." placeholder="Enter a Line" type="text" name="line" required> <br>
                <button class="go-button" type="submit"> Submit </button>
            </form>
        </div>
"""


@app.route("/")
def index():
    return render_template_string(html)


@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        line = request.form['line']
        with open('Files/user_input_flask.txt', 'a+') as file:
            file.write(line + '\n')
        return render_template_string(html)


if __name__ == "__main__":
    app.run(debug=True)
