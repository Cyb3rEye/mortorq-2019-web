from flask import Flask, render_template
app = Flask(__name__, template_folder="pages")
app._static_folder = "pages/static"
@app.route('/')
def index():
    return render_template('index.html')
app.run()
