from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    print("启动测试Flask应用...")
    app.run(debug=True)
