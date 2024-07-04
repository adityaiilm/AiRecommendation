from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form['data']
    data=data+'145'
    # Process the data as needed
    return jsonify({'message': 'Form submitted successfully!', 'data': data})

if __name__ == '__main__':
    app.run(debug=True)
