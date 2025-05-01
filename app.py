from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

INDEX_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Colour guesser</title>
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
</head>
<body style="background-color: {{ colour }};">
<h1>Your favorite colour is {{colour}}</h1>
<p>Is that right?</p>
<form action="/colour">
  <input type="radio" id="yes" name="correct" value="Yes" checked="checked">
  <label for="html">Yes</label><br>
  <input type="radio" id="no" name="correct" value="No">
  <label for="css">No</label><br>
  <input type="submit" value="Submit">
</form>
</body>
</html>
"""

colours = ['red', 'yellow', 'green', 'blue', 'orange']

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template_string(INDEX_TEMPLATE)

@app.route("/colour", methods=["GET", "POST"])
def colour():
    colour = random.choice(colours)
    return render_template_string(COLOUR_TEMPLATE, colour=colour)

if __name__ == "__main__":
    app.run(debug=True)