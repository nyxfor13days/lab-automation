from flask import Flask, render_template, request

app = Flask(__name__)


class App:
    def __init__(self):
        pass

    @app.route('/')
    def index():
        template_data = {
            "title": "Home"
        }
        return render_template('index.html', **template_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
