from flask import Flask,redirect,render_template,request,jsonify,send_from_directory,url_for


app = Flask(__name__)

@app.route("/")
def load_main_page():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)