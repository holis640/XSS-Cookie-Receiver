from flask import Flask, request

app = Flask(__name__)

@app.route('/grab', methods=['GET'])
def grab():
    allowed_cookies = ['session', 'user']
    cookies = {key: value for key, value in request.cookies.items() if key in allowed_cookies}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444)
