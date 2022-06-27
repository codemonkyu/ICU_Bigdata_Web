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

@app.route("/house")
def house():
   return render_template('house.html')

@app.route("/population")
def population():
   return render_template('population.html')  

@app.route("/final_select_dong")
def final_select_dong():
   return render_template('final_select_dong.html')  

@app.route("/finally_area")
def finally_area():
   return render_template('finally_area.html')    

@app.route("/district")
def discrict():
   return render_template('district.html') 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
