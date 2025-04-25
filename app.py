from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Background Color Changer</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body style="background-color: {{ color }};">
    <h1>Choose a background color</h1>
    <form method="post">
        <input type="text" name="color" placeholder="Enter a color (e.g., red, yellow, green)" required>
        <button type="submit">Change Color</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    color = request.form.get("color", "clear")
    return render_template_string(HTML_TEMPLATE, color=color)

if __name__ == "__main__":
    app.run(debug=True)