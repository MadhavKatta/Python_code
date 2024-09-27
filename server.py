from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''
        <html>
        <head>
            <title>Welcome Page</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #333;
                }
                p {
                    font-size: 20px;
                    color: #666;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to My Super Page</h1>
            <p>This is a Python 3.9 powered web application using Flask!</p>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
