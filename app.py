from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fetch_gross_profit', methods=['GET'])
def fetch_gross_profit():
    ticker = request.args.get('ticker')
    # Your logic to fetch gross profit
    return jsonify({'gross_profit': 'value'})

if __name__ == '__main__':
    app.run(debug=True)
