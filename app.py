from flask import Flask, render_template
# from flask import register

app = Flask(__name__)

posts=[
    {
        "Name":"shoaib",
        "dept":"it",
        "id":"21881A12B0",
        "title":"About1"
    },
    {
        "Name":"danish",
        "dept":"it",
        "id":"21881A12C0",
        "title":"About2"
    }


]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/register")
def register():
    form=register()
    return render_template('register.html',title="Register", form=form)

if __name__ == "__main__":
    app.run(debug=True)