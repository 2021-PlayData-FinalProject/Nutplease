# 한국이 제작한 Netflix 프로그램은 몇 개일까요?

## **학습 목표**

데이터 불러오기, 새로운 데이터 프레임 생성

## 답안

1. Kaggle에서 로컬저장소에 저장한 데이터를 불러왔습니다.

```python
# netflix 전체 데이터를 불러오고 netflix_df이라고 지정해줬습니다.
import pandas as pd

netflix_df = pd.read_csv('../00.DataSet/netflix_titles.csv',
                         encoding='utf-8', engine='python')
```

2. 영상물의 국가명이 "South Korea"인 정보에 대한 개수를 확인해보니 **183**개 영상물에 대한 데이터가 있네요.

```python
# country가 'South Korea'인 데이터를 불러오고 nettflix_rok_df라 지정해주었습니다.
# dataframe.shape를 활용해 데이터 프레임의 개수를 확인했습니다.
# 12개의 열과 183개의 행으로 이루어진 데이터 프레임이라는 것을 알 수 있습니다.

netflix_rok_df = netflix_df[netflix_df['country'] == 'South Korea']
print(netflix_rok_df.shape)

결과 : (183, 12)
```

## 의문점

한국 netflix 영상물만 출력하려면 어떻게 country가 'South Korea'여야 한다는 조건을 알 수 있지?

1. 전체 데이터에 구성된 칼럼명과 내용을 확인해 한국 영상물만 출력할 수 있는 힌트를 얻어본다.

```python
# for구문 활용해서 netflix_df의 column들 하나씩 출력하기
# dataframe.info()보다 데이터 정보가 가독성있게 출력됨
# 칼럼 내용 출력되고 칼럼 명이 name이라는 이름으로 출력됨
# {} 딕셔너리형태로 뽑고 반복문으로 뽑기 
for col in netflix_df.columns:
    print("{}\n".format(netflix_df[col].head()))
```

- **country라는 칼럼에 제작 국가명이 담겨져 있음을 알 수 있다.**

```
결과)
0    s1
1    s2
2    s3
3    s4
4    s5
Name: show_id, dtype: object

0    TV Show
1      Movie
2      Movie
3      Movie
4      Movie
Name: type, dtype: object

0       3%
1     7:19
2    23:59
3        9
4       21
Name: title, dtype: object

0                  NaN
1    Jorge Michel Grau
2         Gilbert Chan
3          Shane Acker
4       Robert Luketic
Name: director, dtype: object

0    João Miguel, Bianca Comparato, Michel Gomes, R...
1    Demián Bichir, Héctor Bonilla, Oscar Serrano, ...
2    Tedd Chan, Stella Chung, Henley Hii, Lawrence ...
3    Elijah Wood, John C. Reilly, Jennifer Connelly...
4    Jim Sturgess, Kevin Spacey, Kate Bosworth, Aar...
Name: cast, dtype: object

**0           Brazil
1           Mexico
2        Singapore
3    United States
4    United States
Name: country, dtype: object**

0      August 14, 2020
1    December 23, 2016
2    December 20, 2018
3    November 16, 2017
4      January 1, 2020
Name: date_added, dtype: object

0    2020
1    2016
2    2011
3    2009
4    2008
Name: release_year, dtype: int64

0    TV-MA
1    TV-MA
2        R
3    PG-13
4    PG-13
Name: rating, dtype: object

0    4 Seasons
1       93 min
2       78 min
3       80 min
4      123 min
Name: duration, dtype: object

0    International TV Shows, TV Dramas, TV Sci-Fi &...
1                         Dramas, International Movies
2                  Horror Movies, International Movies
3    Action & Adventure, Independent Movies, Sci-Fi...
4                                               Dramas
Name: listed_in, dtype: object

0    In a future where the elite inhabit an island ...
1    After a devastating earthquake hits Mexico Cit...
2    When an army recruit is found dead, his fellow...
3    In a postapocalyptic world, rag-doll robots hi...
4    A brilliant group of students become card-coun...
Name: description, dtype: object
```

## 사용된 코드

- dataframe.columns : 데이터 프레임의 컬럼명을 확인할 수 있다.
- format() : 필드에 있는 data또는 변형할 data를 지정된 형식에 맞추어 문자열로 변환해 주는 함수인데, 주로 화면에 출력되는 데이터를 보기 좋은 형태로 만들기 위해 사용합니다. 이 함수로 출력된 데이터는 숫자가 아니라 문자의 형태이다.