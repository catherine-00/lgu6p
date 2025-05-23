# 라이브러리 불러오기
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import seaborn as sns

# 제목
st.title("tips 데이터")

#tips 데이터셋 가져오기
tips = sns.load_dataset("tips")

#데이터 미리보기
st.subheader('데이터 미리보기')
st.dataframe(tips.head())

#기본 막대 그래프
st.subheader("기본 막대그래프")
fig = px.bar(tips,
             x='day',
             y='tip',
             title = '요일별 지불 금액',
             labels = {'day' : '요일',
                       'tip' : '평균 Tip($)'})
st.plotly_chart(fig, use_container_width=True)