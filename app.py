from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("http://3.37.32.74/")
def index():
   return render_template('safe_rank.html')

@app.route("http://3.37.32.74/cctv")
def cctv():
   return render_template('cctv.html')

@app.route("http://3.37.32.74/police")
def police():
   return render_template('police.html')

@app.route("http://3.37.32.74/nocover")
def nocover():
   return render_template('nocover.html')

@app.route("http://3.37.32.74/localhouse")
def localhouse():
   return render_template('local+house.html')

if __name__ == '__main__':
    app.run()