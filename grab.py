from flask import Flask, request

app = Flask(__name__)

@app.route('/grab', methods=['GET'])
def grab():
    cookies = request.cookies

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)¡
