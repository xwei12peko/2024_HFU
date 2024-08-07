from flask import Flask, redirect, url_for, render_template    # flask是工具箱(modul模組)、Flask是工具(class類別)

app = Flask(__name__)      # 製作出一個由Flask類別生成的物件(object)

@app.route("/")            # 裝飾器: 根目錄要做啥事
@app.route("/<string:username>")
def say_hello_world(username=""):
    return render_template("hello.html", name=username)

@app.route("/tell_me_a_joke")
def tell_me_a_joke():
    return "<h1> CCC Ha Ha Ha! </h1>"

@app.route("/eat/<string:what_fruit>")
def eat_fruit(what_fruit):
    return redirect(url_for('say_fruit_is_gone', fruit=what_fruit))    # url_for(route_function_name)

@app.route("/eat_<string:fruit>")
def say_fruit_is_gone(fruit):
    return "<h1>" + fruit + " is gone.</h1>"


# 在command_line下: flask_linebot.py run
# 如果我直接執行這個檔案,那__name__就等於__main__
if __name__ == '__main__':
    # 或在command_line下: flask --app flask_linebot.py run
    app.run(debug=True)