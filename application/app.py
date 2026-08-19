from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS DevOps Project</title>
        </head>
        <body>
            <h1>Hello from AWS DevOps Project!</h1>
            <p>Application is running successfully.</p>
            <p>Environment: DEV</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
