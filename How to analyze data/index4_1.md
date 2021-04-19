# 시각화도구 - plotly express란?

## Plotly란?

Python으로 시각화 할 수 있는 라이브러리 중 하나 

```python
from matplotlib import font_manager

for font in font_manager.fontManager.ttflist:
    if 'D2Coding' in font.name:
        print(font.name, font.fname)
```

## 다른 시각화 도구도 많은데 왜 plotly?

Python의 대표적인 시각화 도구는 matplotlib, seaborn 이 있다. 

matplotlib, seaborn은 써봤고 세련된 데이터 시각화 툴 없나 찾는 분이 있다면 plotly를 추천해요.
웹 시각화 라이브러리인 d3.js 를 이용하여 보다 interactive 하게 그래프를 만들어줍니다.

**참고 : Plotly 공식 사이트**

[Plotly Python Graphing Library](https://plotly.com/python/)