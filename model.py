import pandas as pd
import scipy.sparse as spa

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 데이터셋 로드 후 'title' 컬럼값을 소문자로 변경함
def get_data():
    netflix_tmdb_data = pd.read_csv('dataset/netflix_tmdb_merge.csv.zip')
    netflix_tmdb_data['title'] = netflix_tmdb_data['title'].str.lower()
    
    return netflix_tmdb_data

# 'cast' 컬럼과 'genres' 컬럼을 'combine' 이라는 컬럼을 새로 생성하고 기존의 컬럼을 drop 시킴
def combine_data(data):
    comb_data = data.drop(columns=['type', 'title', 'date_added', 'rating', 'duration', 'movie_id', 'overview'])
    comb_data['combine'] = comb_data[comb_data.columns[0:2]].apply(lambda x: ','.join(x.dropna().astype(str)), axis=1)
    comb_data = comb_data.drop(columns=['cast', 'genres'])
       
    return comb_data

'''
위의 combine_data()가 반환한 값과 get_data()의 'overview' 컬럼을 가져온 후,
각각 CountVectorizer와 TfidfVectorizer를 적용하고 코사인 유사도를 계산함
'''
def transform_data(data_combine, data_overview):
    cnt = CountVectorizer(stop_words='english')
    cnt_mtx = cnt.fit_transform(data_combine['combine'])

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_mtx = tfidf.fit_transform(data_overview['overview'])

    combine_sparse = spa.hstack([cnt_mtx, tfidf_mtx], format='csr')
    cosine_sim = cosine_similarity(combine_sparse, combine_sparse)

    return cosine_sim

'''
"title": 컨텐츠 제목(영화), "data": get_data() 리턴값,
"combine": combine_data() 리턴값, "transform": transform_data() 리턴값
'''
def contents_recommendate(title, data, combine, transform):
    indices = pd.Series(data.index, index=data['title'])
    index = indices[title]

    similarity_scores = list(enumerate(transform[index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    similarity_scores = similarity_scores[1:11]  # 입력받은 영화와 유사한 Top10 영화를 추출함

    content_indices = [i[0] for i in similarity_scores]

    content_id = data['movie_id'].iloc[content_indices]
    content_title = data['title'].iloc[content_indices]
    content_genres = data['genres'].iloc[content_indices]

    recommendate_content = pd.DataFrame(columns=['Content_Id', 'Content_Name', 'Genres'])

    recommendate_content['Content_Id'] = content_id
    recommendate_content['Content_Name'] = content_title
    recommendate_content['Genres'] = content_genres

    return recommendate_content

def recommendate_result(content_name):
    content_name = content_name.lower()
    
    find_content = get_data()
    combine_result = combine_data(find_content)
    transform_result = transform_data(combine_result, find_content)

    if content_name not in find_content['title'].unique():
        return 'This Content does not exist in the DataBase.'
    else:
        recommendations = contents_recommendate(content_name, find_content, combine_result, transform_result)
        return recommendations.to_dict('records')