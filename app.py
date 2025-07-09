from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1 style='color:#7E22CE;'>Your Name</h1>
        <blockquote style='color:#FF5C8A;'>Engineering builds on nature, inspired by it, driven by human purpose, and bound by nature's law.</blockquote>
        <p>I am passionate about innovation, optimization, and complex precision backed with clarity and creativity.</p>
    """

@app.route("/about")
def about():
    return """
        <h2>About Me</h2>
        <p>Here you can write your detailed professional journey about AI, engineering, and projects.</p>
    """

@app.route("/projects")
def projects():
    return """
        <h2>Projects</h2>
        <p>List of projects coming soon. You will update this later with your resume projects.</p>
    """

@app.route("/contact")
def contact():
    return """
        <h2>Contact</h2>
        <p>Email: yourname@example.com</p>
        <p>LinkedIn: your-linkedin-url</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
