from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>YellowRoam</title>
        <link rel="manifest" href="/manifest.json">
        <script src="/service-worker.js"></script>
    </head>
    <body>
        <h1>Welcome to YellowRoam</h1>
        <p>Roam like a local.</p>
    </body>
    </html>
    '''