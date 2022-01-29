from flask import Flask, render_template, request, redirect
import csv 

app = Flask(__name__)

@app.route("/")
def Homepage():
    return render_template("index.html")

@app.route("/<string:page_name>")
def Home(page_name):
    return render_template(page_name)

def savetodatabase(data):
    with open('database.csv','a', newline='') as file:
        email = data['email']
        subject = data["subject"]
        message = data["message"]
        filewriter = csv.writer(file, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([email, subject, message])

@app.route('/submitform', methods=['POST'])
def submitform():
    try:
        data = request.form.to_dict()
        savetodatabase(data)
        return redirect('/thankyou.html')
    except:
        return "There's been a problem. Could not save to database."