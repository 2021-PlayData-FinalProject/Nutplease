# 한국 넷플릭스 프로그램의 장르는?

## 학습목표

기초문제1에서 한국 넷플릭스 프로그램에 대한 정보가 담긴 데이터 프레임을 netflix_rok_df라고 지정해주었다. 이번에는 한국 넷플릭스 프로그램은 어떤 장르가 있는지 확인해보고 장르별로 데이터를 확인해보자

## 답안

1. 한국 Netflix 영상 데이터 프레임의 type을 확인해보니 Movie와 TV show가 있다.

```python
# netflix_rok_df는 1번에서 생성한 한국 netflix 프로그램만 포함한 데이터프레임 변수명
# unique 함수를 사용해 데이터의 중복 발생시 1개만 출력되게 함
# 예제의 경우 결과값이 2개 뿐이지만, 결과값이 무수히 많을 경우에는 unique 사용이 필수적이다.

netflix_rok_df['type'].unique()

결과) array(['Movie', 'TV Show'], dtype=object)
```

## 사용된 코드

- series.unique() : series객체의 고유값을 반환