from flask import Flask

app = Flask(__name__)

def get_landing_page():
    return """
    <html>
      <head><title>Landing Page</title></head>
      <body style="font-family:Arial; text-align:center;">
        <h1 style="color:green;">WELCOME TO MY LANDING PAGE</h1>
        <nav style="margin:20px;">
          <a href="#">Home</a> | <a href="#">About</a> | <a href="#">Services</a> | <a href="#">Contact</a>
        </nav>
        <hr>
        <p>This is a basic Python landing page demo.<br>
        You can customize this text to showcase your project, portfolio, or business.</p>
        <hr>
        <div style="display:flex; justify-content:center; gap:20px;">
          <div style="border:1px solid #00cccc; padding:20px;">CONTENT</div>
          <div style="border:1px solid #00cccc; padding:20px;">CONTENT</div>
        </div>
        <hr>
        <footer style="margin-top:30px; color:blue;">
          Thank you for visiting!
        </footer>
      </body>
    </html>
    """

@app.route("/")
def landing():
    return get_landing_page()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
