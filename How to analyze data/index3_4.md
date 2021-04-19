# 언제 새로운 한국 넷플릭스 영상 컨텐츠가 만들어졌을까?

## 추가 문제 설명

한국 넷플릭스 TV프로그램, 영화는 각각 어떤 시기에 만들어졌을까? 연도-월별로 시각화해보자

## 학습목표

시각화 라이브러리 plotly를 활용해 목적에 맞게 시각화 하기

## 답안1 - TV 프로그램

1. 시각화 라이브러리 plotly를 먼저 설치한다.

```python
# Plotly 설치
!pip install plotly
```

```python
# Plotly express 설치
!pip install -q plotly_express
```

```python
# plotly 버전 업데이트
!pip install plotly --upgrade
```

```python
# plotly express 버전 업데이트
!pip install express --upgrade
```

```python
# cufflinks 설치
!pip install -q cufflinks
```

2. plotly의 Heatmap 그래프를 사용해 시각화 한다.

```python
netflix_shows_date = netflix_rok_shows[['date_added']].dropna()
netflix_shows_date['year'] = netflix_shows_date['date_added'].apply(lambda x : x.split(', ')[-1])
netflix_shows_date['month'] = netflix_shows_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][::-1]
df = netflix_shows_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order]

fig = px.imshow(df, labels=dict(color='Count'), x=df.columns, y=df.index)
fig.update_layout(title='넷플릭스 대한민국 TV 프로그램 업데이트 연도별 월간 추가 추세')

fig.show()
```

![3_4_1](https://user-images.githubusercontent.com/80409179/114969947-632b0e00-9eb4-11eb-9c32-6b89d5b07599.png)
🧐**Heatmap을 시각화로 사용한 이유는?**

한국 Netflix TV show 프로그램이 **어떤 연도**의 **어떤 월**에 출시되었는지 확인 하고자함이었기 때문에

## 답안2- 영화

1. TV 프로그램과 같은 방식으로 구현했는데 에러가 발생했다.

```python
netflix_movies_date = netflix_rok_movies[['date_added']].dropna()
netflix_movies_date['year'] = netflix_movies_date['date_added'].apply(lambda x : x.split(', ')[-1])
netflix_movies_date['month'] = netflix_movies_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'][::-1]
df = netflix_movies_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order]

fig = px.imshow(df, labels=dict(x='', y='', color='Count'), x=df.columns, y=df.index)
fig.update_layout(title='넷플릭스 대한민국 한국 영화 업데이트 연도별 월간 추가 추세')

fig.show()
```

- 에러발생

![3_4_2](https://user-images.githubusercontent.com/80409179/114969949-632b0e00-9eb4-11eb-92c8-9f8fe4cab809.png)

2. 이유를 확인해보니 month에 있었다. 영화의 경우 12월에 출시된 영상물이 없었고 그래서 1번과정에서 오류가 발생한 것이다.

```python
netflix_movies_date['month'].unique()

결과)array(['September', 'April', 'October', 'February', 'January', 'May',
       'June', 'March', 'November', 'July', 'August'], dtype=object)
```

3. 12월을 제외하고 검색하자 시각화를 할 수 있었다.

```python
netflix_movies_date = netflix_rok_movies[['date_added']].dropna()
netflix_movies_date['year'] = netflix_movies_date['date_added'].apply(lambda x : x.split(', ')[-1])
netflix_movies_date['month'] = netflix_movies_date['date_added'].apply(lambda x : x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November'][::-1]
df = netflix_movies_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order]

fig = px.imshow(df, labels=dict(color='Count'), x=df.columns, y=df.index)
fig.update_layout(title='넷플릭스 대한민국 한국 영화 업데이트 연도별 월간 추가 추세')

fig.show()
```
![3_4_3](https://user-images.githubusercontent.com/80409179/114969951-63c3a480-9eb4-11eb-968f-81eec1225f2a.png)
