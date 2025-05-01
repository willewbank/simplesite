from flask import Flask, request, render_template_string, session
import random

app = Flask(__name__)

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
    colour = random.choice(colours)
    return render_template_string(COLOUR_TEMPLATE, colour=colour, name=name)

if __name__ == "__main__":
    app.run(debug=True)