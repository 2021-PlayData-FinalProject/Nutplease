from flask_cors import CORS
from flask import Flask, request, jsonify, render_template

import os
import model

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return render_template('movies.html')
        # return 'Welcome to Nutplease Movie Recommendation System :)'

@app.route('/movie')
def recommendate_movies():
        res = model.recommendate_result(request.args.get('title'))
        return jsonify(res)

# @app.route('/movie')
# def movies():
#         return render_template('movies.html')

if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        app.run(host="127.0.0.1", port=port, debug=True)