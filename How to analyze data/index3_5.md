# 한국 넷플릭스 프로그램 관람등급 확인하기

## 추가 문제 설명

한국 넷플릭스 TV프로그램, 영화의 관람등급은 어떻게 될까? 시각화해보자

### 학습목표

목적에 맞게 시각화하기

## 답안1 - TV 프로그램

```python
netflix_rok_shows['rating'].unique()
결과) array(['TV-14', 'TV-PG', 'TV-MA', 'TV-Y7', 'TV-Y', 'TV-G'], dtype=object)
```

```python
f, ax = plt.subplots(figsize=(10, 6))
ax.set_title('넷플릭스 대한민국 한국 TV 프로그램 영상물 등급', family='D2Coding', size=20)

plt.xkcd()
    
sns.set(style = "whitegrid")
sns.countplot(data=netflix_rok_shows, x='rating', palette='pastel',
             order=netflix_rok_shows['rating'].value_counts().index[0:])
```

![3_5_1](https://user-images.githubusercontent.com/80409179/114969952-63c3a480-9eb4-11eb-8a33-bdf9ff01f2f6.png)

## 답안2 - 영화

```python
netflix_rok_movies['rating'].unique()
결과) array(['TV-MA', 'TV-PG', 'NR', 'TV-14', 'TV-Y7'], dtype=object)
```

```python
f, ax = plt.subplots(figsize=(10, 6))
ax.set_title('넷플릭스 대한민국 한국 영화 영상물 등급', family='D2Coding', size=20)

plt.xkcd()
    
sns.set(style = "whitegrid")
sns.countplot(data=netflix_rok_movies, x='rating', palette='husl',
             order=netflix_rok_movies['rating'].value_counts().index[0:])
```

![3_5_2](https://user-images.githubusercontent.com/80409179/114969953-645c3b00-9eb4-11eb-9c57-6c6fc7f2a61a.png)
