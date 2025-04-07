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

import time

st.subheader("16. 애니메이션 꺾은선 그래프 (총 지불 금액의 순차적 변화)")

# 일부 데이터만 사용 (너무 많으면 오래 걸리니까)
progress_data = tips['total_bill'].values[:30]

# 빈 공간 만들기 (여기에 그래프 반복 갱신)
chart_area = st.empty()

# 애니메이션처럼 한 점씩 추가해가며 그래프 그리기
for i in range(2, len(progress_data) + 1):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(progress_data[:i], marker='o', color='skyblue')
    ax.set_title("총 지불 금액의 변화 (애니메이션)")
    ax.set_xlabel("순서")
    ax.set_ylabel("총 지불 금액")
    ax.grid(True)
    
    # 해당 그래프를 chart_area에 업데이트
    chart_area.pyplot(fig)
    time.sleep(0.1)  # 0.1초 지연 (속도 조절 가능)









# st.subheader("14. 꺾은선 그래프 (날짜별 총 지불금액 추세)")

# # 날짜 가정 (인덱스를 날짜로 사용)
# tips_line = tips.copy()
# tips_line['date'] = pd.date_range(start='2023-01-01', periods=len(tips))

# fig13, ax13 = plt.subplots(figsize=(8, 4))
# sns.lineplot(data=tips_line, x='date', y='total_bill', ax=ax13)
# ax13.set_title("날짜별 총 지불 금액 추세 (가상 날짜)")
# ax13.set_xlabel("날짜")
# ax13.set_ylabel("총 지불 금액")
# st.pyplot(fig13, use_container_width=True)


# st.subheader("15. 팁 금액의 정규분포 곡선")

# fig14, ax14 = plt.subplots(figsize=(7, 4))
# sns.histplot(data=tips, x='tip', kde=True, bins=20, ax=ax14)
# ax14.set_title("팁 금액의 분포와 정규 곡선")
# ax14.set_xlabel("팁 ($)")
# ax14.set_ylabel("빈도")
# st.pyplot(fig14, use_container_width=True)

# st.subheader("15-1. 팁 금액의 커널 밀도 곡선 (KDE)")

# fig15, ax15 = plt.subplots(figsize=(7, 4))
# sns.kdeplot(data=tips, x='tip', fill=True, ax=ax15)
# ax15.set_title("팁 금액의 밀도 곡선")
# ax15.set_xlabel("팁 ($)")
# st.pyplot(fig15, use_container_width=True)


# # 박스플롯
# st.subheader("5. 박스플롯 (요일별 팁 분포)")
# fig4, ax4 = plt.subplots(figsize=(7, 5))
# sns.boxplot(data=tips, x='day', y='tip', ax=ax4)
# ax4.set_title("요일별 팁 분포")
# ax4.set_xlabel("요일")
# ax4.set_ylabel("팁 ($)")
# st.pyplot(fig4, use_container_width=True)


# # 카운트플롯
# st.subheader("6. 카운트플롯 (성별 인원수)")
# fig5, ax5 = plt.subplots(figsize=(5, 4))
# sns.countplot(data=tips, x='sex', hue='smoker', ax=ax5)
# ax5.set_title("성별 흡연 여부에 따른 인원수")
# ax5.set_xlabel("성별")
# ax5.set_ylabel("인원 수")
# st.pyplot(fig5, use_container_width=True)

# # 파이차트 (matplotlib)
# st.subheader("7. 파이차트 (성별 비율)")
# sex_counts = tips['sex'].value_counts()
# fig6, ax6 = plt.subplots()
# ax6.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
# ax6.set_title("성별 비율")
# ax6.axis('equal')  # 원형 유지
# st.pyplot(fig6, use_container_width=True)

# # 팁 비율 컬럼 추가
# tips['tip_pct'] = tips['tip'] / tips['total_bill']

# # 팁 비율 boxplot
# st.subheader("8. 팁 비율 (총금액 대비)")
# fig7, ax7 = plt.subplots(figsize=(7, 5))
# sns.boxplot(data=tips, x='day', y='tip_pct', ax=ax7)
# ax7.set_title("요일별 팁 비율 분포")
# ax7.set_ylabel("팁 비율")
# st.pyplot(fig7, use_container_width=True)

# # 총 지불 금액 기준 상위 10명
# top10 = tips.sort_values(by='total_bill', ascending=False).head(10)
# top10 = top10.reset_index()  # 인덱스 사용을 위해

# st.subheader("10. 총 지불 금액 상위 10명")
# fig9, ax9 = plt.subplots(figsize=(7, 5))
# sns.barplot(data=top10, x='total_bill', y=top10.index, hue='sex', ax=ax9)
# ax9.set_title("총 지불 금액 상위 10명")
# ax9.set_xlabel("총 지불 금액")
# ax9.set_ylabel("손님 순번")
# st.pyplot(fig9, use_container_width=True)

# # 팁 비율 상위 N명
# st.subheader("12. 팁 비율 상위 N명 보기 (슬라이더)")

# # 슬라이더로 N 선택
# top_n = st.slider("상위 몇 명을 볼까요?", min_value=5, max_value=30, value=10)

# # 팁 비율 기준 상위 N명 추출
# top_tip_pct = tips.sort_values(by='tip_pct', ascending=False).head(top_n).reset_index()

# fig11, ax11 = plt.subplots(figsize=(7, 5))
# sns.barplot(data=top_tip_pct, x='tip_pct', y=top_tip_pct.index, hue='sex', ax=ax11)
# ax11.set_title(f"팁 비율 상위 {top_n}명")
# ax11.set_xlabel("팁 비율")
# ax11.set_ylabel("손님 순번")
# st.pyplot(fig11, use_container_width=True)

# # 요일 선택 산점도
# st.subheader("13. 요일별 산점도 보기 (드롭다운)")

# # 요일 리스트 가져오기
# days = tips['day'].unique()
# selected_day = st.selectbox("요일을 선택하세요:", options=days)

# # 선택한 요일에 해당하는 데이터 필터링
# filtered = tips[tips['day'] == selected_day]

# fig12, ax12 = plt.subplots(figsize=(7, 5))
# sns.scatterplot(data=filtered, x='total_bill', y='tip', hue='sex', size='size', ax=ax12)
# ax12.set_title(f"{selected_day}의 총지불금액 vs 팁")
# ax12.set_xlabel("총 지불 금액")
# ax12.set_ylabel("팁")
# st.pyplot(fig12, use_container_width=True)

