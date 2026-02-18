from flask import Flask

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define the route (the URL path)
@app.route("/")
def hello_world():
    # 3. Return the HTML content to the browser
    return "<p>Hello, World!</p><p>My name is </p>"

# 4. Start the server
if __name__ == "__main__":
    # debug=True allows the server to auto-reload when you change code
    app.run(debug=True)