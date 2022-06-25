from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
   return render_template('safe_rank.html')

@app.route("/cctv")
def cctv():
   return render_template('cctv.html')

@app.route("/police")
def police():
   return render_template('police.html')

@app.route("/nocover")
def nocover():
   return render_template('nocover.html')

@app.route("/localhouse")
def localhouse():
   return render_template('local+house.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)