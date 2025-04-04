# 파일명 : mat_app.py 확인 명령어 : ls입력

import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

#출력할거임
# st.title("Matplotlib 튜토리얼")
# 실행 : streamlit run mat_app.py -> 이메일 작성하라고 나옴 -> 그냥 엔터
#  -> 크롬에 Matplotlib 튜토리얼 적힌 사이트 하나 나옴.

# 1. 한글폰트 설정하기
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
sns.set(font = 'Malgun Gothic',
        rc = {'axes.unicode_minus' : False},
        style = 'darkgrid')

# 2. 페이지 설정
st.set_page_config(page_title = 'Matplotlib & Seaborn 튜토리얼', layout = 'wide')
st.title("Matplotlib & Seaborn 튜토리얼")

# 3. 데이터셋 불러오기
tips = sns.load_dataset('tips')

# 데이터 미리보기
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

# 기본 막대 그래프, matplotlit + seaborn
st.subheader("1. 기본 막대 그래프")
# 객체 지향 방식으로 작성할 것.
# 그래프를 그리는 목적 : 예쁘게 잘 나오라고.
# fig, ax = plt.subplots(figsize = (10,6))

# matplotlib 문법
fig, ax = plt.subplots(figsize = (7,5)) 

# seaborn 문법 : 통계와 관련된 시각화
sns.barplot(data=tips, x = 'day', y = 'total_bill' ,ax=ax)

# matplotlib 문법
ax.set_title("요일별 평균 지불 금액")
ax.set_xlabel('요일')
ax.set_ylabel('평균 지불 금액($)')

# st.pyplot(fig)
# chatGPT한테 물어봄. 그래프 크기가 너무 크고 고정되어 있어서. 페이지 너비에 맞게 조절하는 것.

# streamlit 문법 : 웹 상에 보여주는 용도
# plt.show() -> 이 문법은 jupyter notebook, google colab에서 활용할 때 사용
st.pyplot(fig, use_container_width=True) 



# 산점도
# x축, y축이 연속형 변수여야 합니다.
st.subheader("2. 산점도")
# matplotlib 문법
fig1, ax1 = plt.subplots(figsize = (7,5)) 

# seaborn 문법 : 통계와 관련된 시각화
sns.barplot(data=tips, x = 'day', y = 'total_bill' ,ax=ax)
sns.scatterplot(data=tips, x = 'total_bill', y = 'tip',hue = 'day', size = 'size', ax=ax1)

# st.pyplot(fig)
# chatGPT한테 물어봄. 그래프 크기가 너무 크고 고정되어 있어서. 페이지 너비에 맞게 조절하는 것.

# streamlit 문법 : 웹 상에 보여주는 용도
# plt.show() -> 이 문법은 jupyter notebook, google colab에서 활용할 때 사용
st.pyplot(fig1, use_container_width=True) 


# 히트맵
st.subheader('3. 히트맵')

# 요일과 시간별 평균 팁 계산
pivot_df = tips.pivot_table(values = 'tip', index='day', columns='time', aggfunc='mean')
fig2, ax2 = plt.subplots(figsize = (7,5))
sns.heatmap(pivot_df, annot=True, fmt='.2f', ax=ax2)
st.pyplot(fig2, use_container_width=True)


# 회귀선이 있는 산점도
st.subheader('4. 회귀선이 있는 산점도')
fig3, ax3 = plt.subplots(figsize = (7,5))
sns.regplot(data=tips, x='total_bill', y='tip', scatter_kws={'alpha' : 0.5}, ax=ax3)
st.pyplot(fig3, use_container_width=True)

# 챗지피티 질문던지기 : fig, ax = plt.subplots() 이런 방식으로 만드세요!!