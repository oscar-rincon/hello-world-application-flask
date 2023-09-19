from flask import Flask
app = Flask("My First Application")

@app.route("/")
def hello() :
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True)
