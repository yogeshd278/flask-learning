from flask import Flask
app = Flask(__name__)

@app.route('/display/<name>')
def display_name(name):
    return 'Hello %s !!' % name

if __name__ == '__main__':
    app.run(debug = True) 