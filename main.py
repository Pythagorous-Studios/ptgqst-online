from flask import Flask, render_template
#from PtgQst.eng import eng
from PtgQst.logger import logger
app = Flask(__name__)

@app.route('/index')
def hello_world():
    return render_template("index.html")

if __name__=="__main__":
    print('ello')
