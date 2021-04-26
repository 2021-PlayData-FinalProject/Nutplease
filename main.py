from flask_cors import CORS
from flask import Flask, jsonify, request, render_template

import os
import model

# 영화 검색 시 유사한 영화 제안
def get_suggestions():
        data = model.get_data()
        return list(data['title'].str.upper())

def convert_to_list(my_list):
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["','')  # 처음
    my_list[-1] = my_list[-1].replace('"]','')  # 마지막
    return my_list

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
        suggestions = get_suggestions()
        return render_template('index.html', suggestions=suggestions)

@app.route('/movie', methods=["GET"])
def similarity_movies():
        res = model.recommendate_result(request.args.get('title'))
        return jsonify(res)

@app.route("/recommend",methods=["POST"])
def recommend():
    title = request.form['title']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    suggestions = get_suggestions()

    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    
    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}

    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_cards,suggestions=suggestions)

if __name__ == '__main__':
        port = int(os.environ.get("PORT", 5000))
        app.run(host="127.0.0.1", port=port, debug=True)