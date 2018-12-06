from flask import Flask,render_template,request,send_from_directory
from werkzeug.utils import secure_filename
import os
import time
app = Flask(__name__)
@app.route('/')
def submt():
    return (render_template('file_up.html'))
@app.route('/submitted',methods=['GET','POST'])
def submitted():
    if request.method=='POST':
        f=request.files['fil']
        global filename
        filename = f.filename
        f.save("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename))
        return (render_template('f1.html'))
        
@app.route('/submitted/size',methods=['GET','POST'])
def size():
    if request.method=='POST':
        return str(os.path.getsize("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename)))

@app.route('/submitted/line',methods=['GET','POST'])
def lines():
    if request.method=='POST':
        return str(sum(1 for line in open("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename))))

@app.route('/submitted/last',methods=['GET','POST'])
def last():
    if request.method=='POST':
        return time.ctime(os.path.getmtime("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename)))

@app.route('/submitted/all',methods=['GET','POST'])
def all():
    if request.method=='POST':
        a=time.ctime(os.path.getmtime("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename)))
        b=str(os.path.getsize("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename)))
        c=str(sum(1 for line in open("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(filename))))
        return "LAST MODIFIED=" + a +"<br>"+ "SIZE="+b+"<br>"+"NO OF LINES="+c