from flask import Flask, render_template, redirect, url_for, request
import psycopg2

app = Flask(__name__)
# Connect to database
conn = psycopg2.connect(host='localhost', port='5432',user ='postgres',password='ubaid321', database='ubaid_portfolio')

# cursor setup
cur = conn.cursor()

# Define url
@app.route('/',methods=['GET','POST'])
def Home():
    try:
        if request.method == 'POST':
            Name = request.form['name']
            Email = request.form['email']
            Subject = request.form['subject']
            Message = request.form['message']
    except:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)