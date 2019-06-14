import uuid
from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from controllers.usr import usr

app = Flask(__name__)
app.secret_key = b"flaskvl^qk#q^ml3v=0lk*b@^88b))hb17u@zj^m#!t#u%rlj$96r_wpython"
app.register_blueprint(usr)


def verifica_login(fn):
    def wrapper(*args, **kwargs):
        print("Meu decorado")
        response = fn(*args, **kwargs)
        return response

    return wrapper


@app.route("/")
@verifica_login
def index():
    name = "Samuel L Jackson"
    uuid_val = uuid.uuid4()
    return render_template("index.html", **locals())


@app.route("/config", methods=["POST"])
def config():
    return "Config"


@app.route("/config/<uuid:username>", methods=["GET"])
def my_config(username):
    return render_template("configurations/my_config.html", username=username)


@app.route("/usr/subr")
def usr_subr():
    return render_template("configurations/my_config.html")


@app.route("/usr/subr", methods=["POST"])
def post_usr_subr():
    username = request.form["nome"]
    age = request.form["idade"]
    my_file = request.files["arquivo"]
    my_file.save("teste.txt")
    return render_template("configurations/my_config.html", **locals())


@app.route("/login", methods=["GET"])
def get_login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def post_login():
    params = request.form
    login = params["login"]
    passwd = params["password"]
    if login == "mauricio" and passwd == "teste123":
        session["user"] = {"login": login, "passwd": passwd}
        return redirect("/config")
    return redirect("/login")


@app.route("/config")
def get_config():
    username = session["user"]["login"]
    return render_template("configurations/my_config.html", username=username)


@app.route("/logout", methods=["GET"])
def get_logout():
    del session["user"]
    return redirect("/login")


@app.before_request
def check_login():
    if request.path == "/login":
        return
    if not session.get("user", None):
        return redirect("login")
