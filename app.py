from flask import Flask, request, render_template_string, session, redirect
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
<form action="/colour" method="post">
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
<p>Did I get that right? Hit try again if I got it wrong.</p>
<form action="/colour">
    <input type="submit" value="Try Again">
</form>
<p>Do you want to sign up to coding club?</p>
<form action="/signup">
    <input type="submit" value="Sign up">
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
    name = request.form.get("name", "Guest")
    colour = random.choice(colours)
    return render_template_string(COLOUR_TEMPLATE, colour=colour, name=name)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    return redirect("https://forms.cloud.microsoft/pages/responsepage.aspx?id=PKjhf7v5f0auHigHBSUJQdiq9VVxg5BFnGDGMD0e-41UNEpHN1FDVTZPTUtQQ1RCNFg5SVlaUzVSRy4u&route=shorturl")

if __name__ == "__main__":
    app.run(debug=True)
