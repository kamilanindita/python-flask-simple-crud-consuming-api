from flask import Flask,render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import json
import requests

app = Flask(__name__)

app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_DB"]="website_crud"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql = MySQL(app)



@app.route("/")
def index():
    title="Index"
    return render_template("index.html",title=title)
    
@app.route("/buku")
def buku():
    url='http://localhost/native/oop_crud_mysql_mysqli_api_server/api/buku.php'
    title="Buku"
    data = requests.get(url)
    data=json.loads(data.text)
    result=data['data']
    return render_template("buku.html",data=result,title=title)
    
@app.route("/buku/add")
def add():
    title="Tambah"
    return render_template("tambah.html",title=title)
   
@app.route("/buku/tambah/save",methods=["POST"])
def save():
    penulis=request.form["penulis"]
    judul=request.form["judul"]
    kota=request.form["kota"]
    penerbit=request.form["penerbit"]
    tahun=request.form["tahun"]
    
    params={ 
        'penulis':penulis,
        'judul':judul,
        'kota':kota,
        'penerbit':penerbit,
        'tahun':tahun

    }

    requests.post('http://localhost/native/oop_crud_mysql_mysqli_api_server/api/buku.php',json=params)
    return redirect(url_for('buku'))
  

@app.route("/buku/edit/<id>")
def edit(id):
    title="Edit"
    params={
        'id':id
    }
    url='http://localhost/native/oop_crud_mysql_mysqli_api_server/api/buku.php'
    data = requests.get(url,params)
    data=json.loads(data.text)
    result=data['data']
   
    return render_template("edit.html",data=result,title=title)


   
@app.route("/buku/update/<id>",methods=["POST"])
def update(id):
    penulis=request.form["penulis"]
    judul=request.form["judul"]
    kota=request.form["kota"]
    penerbit=request.form["penerbit"]
    tahun=request.form["tahun"]


    data={ 
        'id':id,
        'penulis':penulis,
        'judul':judul,
        'kota':kota,
        'penerbit':penerbit,
        'tahun':tahun

    }

    requests.put('http://localhost/native/oop_crud_mysql_mysqli_api_server/api/buku.php',json=data)
    return redirect(url_for('buku'))

@app.route("/buku/delete/<id>")
def delete(id):
    params={
        'id':id
    }

    data = requests.delete('http://localhost/native/oop_crud_mysql_mysqli_api_server/api/buku.php',json=params)
    return redirect(url_for('buku'))
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
