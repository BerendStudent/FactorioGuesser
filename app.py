from flask import Flask,redirect,render_template,request,jsonify,send_from_directory,url_for
import os

app = Flask(__name__)

@app.route("/")
def load_main_page():
    return render_template('index.html')


@app.route("/guessr")
def render_work_page():
    return render_template('index.html')


@app.route("/about")
def render_about_page():
    return render_template('about.html')


@app.route("/possibleguesses", methods=["GET"])
def supply_image_names():
    choices = []
    with os.scandir('./static/images') as entries:
        for entry in entries:
            filename, extension = os.path.splitext(entry.name)
            choices.append(filename)
    return jsonify(choices), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)