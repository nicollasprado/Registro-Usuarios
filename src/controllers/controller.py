from flask.views import MethodView
from flask import request, render_template, redirect
from src.database import mysql


cursor = mysql.cursor()


class IndexController(MethodView):
    def get(self):
        return render_template("public/index.html")
    
    def post(self):
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        cursor.execute("INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, password))
        cursor.connection.commit()
        return redirect('/')
    
class ViewRegisteredController(MethodView):
    def get(self):
        cursor.execute("SELECT * FROM users")
        dataDB = cursor.fetchall()
        return render_template('public/verCadastrados.html', data = dataDB)
    
    
class ViewRegisteredSearchController(MethodView):
    def post(self):
        search = request.form["search"]
        cursor.execute("SELECT * FROM users WHERE id = %s OR first_name = %s OR last_name = %s OR email = %s OR password = %s", (search, search, search, search, search))
        dataSearch = cursor.fetchall()
        return render_template('public/verCadastradosSearch.html', data = dataSearch)