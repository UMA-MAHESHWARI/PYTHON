from flask import Flask,render_template,request,send_from_directory
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/')
def submt():
    return (render_template('file_up.html'))

@app.route('/submitted',methods=['GET','POST'])
def submitted():
    if request.method=='POST':
        f=request.files['fil']
        f.save("C:/Users/UmaMaheshwari.s/Documents/uploads/"+secure_filename(f.filename))
        return send_from_directory("C:/Users/UmaMaheshwari.s/Documents/uploads",secure_filename(f.filename))
    return "SUCCESSFUL"
