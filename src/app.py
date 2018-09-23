from flask import Flask, render_template
app = Flask(__name__, template_folder="pages")
app._static_folder = "pages/static"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/programming/')
def programming():
    return render_template('programming.html')

@app.route('/awards/')
def awards():
    return render_template('awards.html')
@app.route('/sponsors/')
def sponsors():
    return render_template('sponsors.html')
if __name__ == '__main__':
    app.run()
