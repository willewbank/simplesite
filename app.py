from flask import Flask, request, render_template_string, session
import random

app = Flask(__name__)

app.secret_key = "session"

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Colour guesser</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
<h1>Your favorite colour guesser</h1>
<p>Enter your name and your favorite colour will show.</p>
<form action="/colour">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name"><br><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
"""

COLOUR_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Colour guesser</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body style="background-color: {{ colour }};">
<h1>{{name}}'s favorite colour is {{colour}}</h1>
<p>Is that right?</p>
<form action="/colour">
    <div style="display: flex; gap: 10px;">
        <div>
            <input type="radio" id="yes" name="correct" value="Yes" checked="checked">
            <label for="yes">Yes</label><br>
        </div>
        <div>
            <input type="radio" id="no" name="correct" value="No">
            <label for="no">No</label><br>
        </div>
  <input type="submit" value="Submit">
</form>
</body>
</html>
"""

colours = ['red', 'yellow', 'green', 'blue', 'orange', 'pink', 'purple']

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template_string(INDEX_TEMPLATE)

@app.route("/colour", methods=["GET", "POST"])
def colour():
    name = request.args.get("name", "Guest")
    if request.method == "POST":
        user_choice = request.form.get("correct")
        if user_choice == "No":
            session["colour"] = random.choice(colours)
    if "colour" not in session:
        session["colour"] = random.choice(colours)
    return render_template_string(COLOUR_TEMPLATE, colour=session["colour"], name=name)

if __name__ == "__main__":
    app.run(debug=True)