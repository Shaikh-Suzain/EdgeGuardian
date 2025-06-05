from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is EdgeGuardian!"

@app.route('/about')
def about():
    return "This is the about page. Welcome to EdgeGuardian!"

@app.route('/contact')
def contact():
    return "Contact us at edgeguardian@example.com"

if __name__ == '__main__':
    app.run(debug=True)
