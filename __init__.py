from flask import Flask,render_template

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template_1():
    return render_template("resume_template.html")

@app.route('/mon_cv')
def resume_template_2():
    return render_template("mon_cv.html")

if(__name__ == "__main__"):
    app.run()
