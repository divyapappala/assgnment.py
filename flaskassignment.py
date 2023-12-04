from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>flask assignment</h1>"

data=[
    {'id': 1,
     'name': "divya",
     'email': "divya@gmail.com"
    },  
    { 'id': 2,
    'name': "rekha",
    'email': "rekha@gmail.com"
    }
]


@app.route("/users")
def emp_details():
    #users = data
    return render_template("details.html", content = data)


@app.route("/users/<int:employee_id>")
def users(employee_id):
    for employee in data:
        if employee['id'] == employee_id:
            emp_data=[employee['name'],employee['email']]
            return emp_data
    return 'employee not found'


if __name__ == "__main__":
    app.run(debug=True)

