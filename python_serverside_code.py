from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/save_data', methods=['POST'])
def save_data():
    # Get the data from the request
    data = request.get_json()['data']

    # Save the data to a file in the Git repository
    with open('https://github.com/MyadamPuneeth/Portfolio_website_data/blob/main/data.txt', 'a') as f:
        f.write(data + '\n')

    # Commit the changes
    os.system("https://github.com/MyadamPuneeth/Portfolio_website_data && git add . && git commit -m 'Add new data' && git push")

    # Send a response back to the client
    return jsonify({'message': 'Data received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
