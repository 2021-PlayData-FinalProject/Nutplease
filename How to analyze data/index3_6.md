# 한국 넷플릭스 프로그램 상영시간 확인하기

## 추가 문제 설명

한국 넷플릭스 TV프로그램, 영화의 상영시간은 어떻게 구성되어 있을까? 시각화해보자

## 학습목표

목적에 맞게 시각화하기

## 답안1 - TV 프로그램

```python
netflix_rok_shows['duration'].unique()
결과) array(['1 Season', '2 Seasons', '5 Seasons', '4 Seasons', '3 Seasons'],
      dtype=object)
```

```python
colors = ['lightslategray']
colors[0] = 'crimson'

show_dur = pd.value_counts(netflix_rok_shows['duration'])
fig = go.Figure([go.Bar(x=show_dur.index, y=show_dur.values,
                        text=show_dur.values, marker_color=colors)])
fig.update_traces(textposition='outside')
fig.update_layout(title='한국 TV 프로그램 상영시간 분포도', xaxis={'categoryorder':'total descending'})

fig.show()
```
![3_6_1](https://user-images.githubusercontent.com/80409179/114969954-64f4d180-9eb4-11eb-879c-06b4d1fd00dd.png)

## 답안2 - 영화

```python
netflix_rok_df['duration'].unique()
결과) array(['99 min', '1 Season', '107 min', '135 min', '2 Seasons', '133 min',
       '109 min', '137 min', '110 min', '140 min', '128 min', '102 min',
       '143 min', '118 min', '5 Seasons', '111 min', '63 min', '122 min',
       '4 Seasons', '123 min', '112 min', '139 min', '136 min', '91 min',
       '130 min', '116 min', '125 min', '100 min', '126 min', '3 Seasons',
       '54 min'], dtype=object)
```

```python
colors = ['lightslategray']
colors[0] = 'crimson'

movie_dur = pd.value_counts(netflix_rok_movies['duration'])
fig = go.Figure([go.Bar(x=movie_dur.index, y=movie_dur.values,
                        text=movie_dur.values, marker_color=colors)])
fig.update_traces(textposition='outside')
fig.update_layout(title='한국 영화 상영시간 분포도', xaxis={'categoryorder':'total descending'})

fig.show()
```

![3_6_2](https://user-images.githubusercontent.com/80409179/114969955-64f4d180-9eb4-11eb-8d83-b3b37b4c24ce.png)
