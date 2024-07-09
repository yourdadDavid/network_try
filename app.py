from flask import Flask, send_from_directory,url_for,redirect,render_template,request
import uuid
import os

app=Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload' ,methods=['GET','POST'])
def upload():
    if request.method=='POST':
        avatar=request.files['avatar']
        if avatar :
            filename=random_file(avatar.filename)
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            return redirect(url_for('uploaded_file',filename=filename))
    return render_template("index.html")
def random_file(filename):
    ext=os.path.splitext(filename)[1]
    new_filename=uuid.uuid4().hex+ext
    return new_filename

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)        

if __name__=='__main__':
    app.run(debug=True)