from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


# Run using 'flask --app server --debug run'


@app.route("/")
def my_home():
    return render_template('index.html')


# Dynamic routing to HTML pages
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# Write to a text file the information entered in contacts page
def write_to_file(data):
    with open('database.txt', mode='a') as database_txt:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        file = database_txt.write(f'\n{name},{email},{message}')


# Write to a CSV file the information entered in contacts page
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


# Rout to Thank You page and get information from contacts page
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Something went wrong. Try again'
    else:
        return 'Something went wrong. Try again'
