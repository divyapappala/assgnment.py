from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/')
def student():
            data=[
                     {'id': 1, 'name': "divya", 'email': "divya@gmail.com"},
                     {'id': 2, 'name': "rekha", 'email': "rekha@gmail.com"},
                     {'id': 3,'name': "ajay",'email': "kdajay@gmail.com"}
                 ]
            return jsonify(data)
@app.route('/details')
def find_student():
        details=[
                {'id': 3,'name': "ajay",'email': "kdajay@gmail.com"}      
             ]
        return jsonify(details)
if __name__=='__main__':
    app.run(debug=True)