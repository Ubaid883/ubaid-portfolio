from flask import Flask, render_template, redirect, url_for, request, jsonify
import psycopg2
from psycopg2 import errors

app = Flask(__name__)
# Connect to database
conn = psycopg2.connect(host='localhost', port='5432',user ='postgres',password='ubaid321', database='contact')

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
            cur.execute("INSERT INTO user_info (name,email,subject,message) VALUES(%s,%s,%s,%s)",(Name,Email,Subject,Message))
            conn.commit()
            cur.execute("SELECT * FROM user_info")
            new_user = cur.fetchall()
            
            return jsonify({
                        'message': 'User inserted successfully',
                        'user': {
                            'id': new_user[0],
                            'name': new_user[1],
                            'email': new_user[2]
                        }
                    })
            return redirect('/')
    except errors.UniqueViolation as e:
        print("Unique constraint violated:", e)  # ✔️ Correct
        conn.rollback()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)