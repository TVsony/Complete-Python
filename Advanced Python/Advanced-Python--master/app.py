from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        char_values = string.ascii_letters + string.digits + string.punctuation 
        generated_password = ''.join(random.choice(char_values) for _ in range(password_length))
        return render_template('index.html', password=generated_password)

if __name__ == '__main__':
    app.run(debug=True)
