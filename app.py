from flask import Flask, request
from fetch_gross_profit import fetch_gross_profit

app = Flask(__name__)

@app.route('/fetch_gross_profit')
def get_gross_profit():
    ticker = request.args.get('ticker')
    return fetch_gross_profit(ticker)

if __name__ == "__main__":
    app.run(debug=True)
