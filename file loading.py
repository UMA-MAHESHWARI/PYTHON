import os
import time
from flask import Flask, redirect, url_for, request, send_from_directory, render_template,flash, make_response,Response
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/path/to/the/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['txt'])
app = Flask(__name__)
app.config['UPLOAD_FOLDER']="D:/Programs/Flask/uploaded"
sizes = ['Bytes','KB','MB','GB']

def convertsize(size):
    for byte in sizes:
        if size<1024:
            return '{0:.2f} {1}'.format(size,byte)
        size = size/1024


@app.route("/",methods=["POST","GET"])
def upload():
    if request.method == "POST":
        if 'filetoupload' not in request.files:
            flash("No file Part")
            return redirect(request.url)
        file = request.files['filetoupload']
        
        if file.filename == "":
            flash("No file Part")
            return redirect(request.url)

        if allowed_filename(file.filename) and file:
            cookie = make_response(render_template("page2.html"))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename)) 
            cookie.set_cookie('filename',filepath,max_age=60*2)
            # filename = secure_filename(file.filename)
            file.save(filepath)
            #return redirect(url_for('send',filename=filename))
            return cookie
    # cookie = make_response(render_template("file.html"))
    # cookie.set_cookie("filename",expires=0)
    # return cookie
    return render_template('file.html')


def allowed_filename(filename):
    return '.' in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route("/size")
def size():
    metadata = os.stat(request.cookies.get("filename"))
    return "<h1><b><i>File size is :{}</b></i></h1>".format(convertsize(metadata.st_size))


@app.route("/date_modified")
def date_modified():
    metadata = os.stat(request.cookies.get("filename"))
    return "<h1><b><i>Last Modified Date :{}</b></h1>".format(time.asctime(time.localtime(metadata.st_mtime)))

@app.route("/number_of_lines")
def number_of_lines():
    num = 0
    fullpath = request.cookies.get("filename") 
    (directory,filename)=os.path.split(fullpath)
    with open(fullpath) as file:
        for line in file:
            num += 1
    return "<h1><b><i>Number Of Lines in {0} is {1}</b></i></h1>".format(filename,num)


@app.route("/findall")
def findall():
    return "<b><i>{0}<br><br>{1}<br><br>{2}</i></b>".format(size(),date_modified(),number_of_lines())

# @app.route("/del")
# def delete():
#     cookie = make_response(render_template("file.html"))
#     cookie.set_cookie("username",expires=0)
#     return cookie

# @app.route("/uploads/<filename>")
# def send(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

# @app.route("/file",methods=["POST","GET"])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['filetoupload']
#         f.save("D:/Programs/Flask/uploaded/uploaded_file.pdf")
#         return "Your File Uploaded Successfully"


# @app.route("/filesecure",methods=["POST","GET"])
# def file_upload():
#     if request.method == 'POST':
#         f = request.files['filetoupload']
#         f.save("D:/Programs/Flask/uploaded/"+secure_filename(f.filename))#Store using the original file name
#         return "Your File Uploaded Successfully"