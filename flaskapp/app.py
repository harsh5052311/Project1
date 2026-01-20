# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def landing_page():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Landing Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f4f9;
                margin: 0;
                padding: 0;
                text-align: center;
            }
            header {
                background: #4CAF50;
                color: white;
                padding: 20px;
            }
            nav {
                margin: 20px 0;
            }
            nav a {
                margin: 0 15px;
                text-decoration: none;
                color: #333;
                font-weight: bold;
            }
            section {
                padding: 40px;
            }
            footer {
                background: #333;
                color: white;
                padding: 10px;
                position: fixed;
                bottom: 0;
                width: 100%;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to My Landing Page</h1>
        </header>

        <nav>
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
        </nav>

        <section>
            <h2>Hello Jenkins!</h2>
            <p>This is a basic landing page served on a port.</p>
        </section>

        <footer>
            <p>&copy; 2026 My Landing Page</p>
        </footer>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Run on port 8080 (you can change this)
    app.run(host="0.0.0.0", port=3000)

