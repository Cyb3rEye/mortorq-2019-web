from flask import Flask, render_template
app = Flask(__name__, template_folder="pages")
app._static_folder = "pages/static"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

app.run()
