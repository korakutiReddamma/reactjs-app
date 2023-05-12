from flask import Flask, render_template
import mysql.connector


app = Flask(__name__)
#to get accept the request from all the origins
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
    return response

@app.route('/')
def index():
    cnx = mysql.connector.connect(user='admin', password='Reddy123',
                                   host='database-1.cglklhnjxwru.ap-southeast-1.rds.amazonaws.com',
                                   database='react_db')
    cursor = cnx.cursor()
    query = "SELECT * FROM datajs"
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()
    return render_template('index.html', rows=rows)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)