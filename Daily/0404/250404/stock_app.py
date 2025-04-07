import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="주식 차트 대시보드", layout="wide")

# 제목
st.title("📈 주식 차트 대시보드")

# 사이드바
st.sidebar.header("주식 정보")
stock_dict = {
    "Apple": "AAPL",
    "Google": "GOOG",
    "Microsoft": "MSFT",
    "Amazon": "AMZN",
    "Tesla": "TSLA"
}
stock_name = st.sidebar.selectbox("기업 선택", list(stock_dict.keys()))
ticker = stock_dict[stock_name]

start_date = st.sidebar.date_input("시작 날짜", pd.to_datetime("2024-04-04"))
end_date = st.sidebar.date_input("종료 날짜", pd.to_datetime("2025-04-04"))

# 데이터 불러오기
df = yf.download(ticker, start=start_date, end=end_date)

# 현재 가격 및 52주 고저 출력
st.subheader(f"{stock_name} ({ticker}) 주식 정보")
col1, col2, col3 = st.columns(3)
col1.metric("📌 현재 가격", f"${float(df['Close'].iloc[-1]):.2f}")
col2.metric("📈 52주 최고가", f"${float(df['High'].max()):.2f}")
col3.metric("📉 52주 최저가", f"${float(df['Low'].min()):.2f}")

# 탭 설정
tab1, tab2, tab3 = st.tabs(["Matplotlib", "Seaborn", "Plotly"])

# Matplotlib 차트
with tab1:
    st.subheader("Matplotlib 차트")
    fig, ax = plt.subplots()
    ax.plot(df.index, df["Close"], label="종가")
    ax.set_title(f"{stock_name} ({ticker}) 주가")
    ax.set_xlabel("날짜")
    ax.set_ylabel("가격 ($)")
    ax.legend()
    st.pyplot(fig)

# Seaborn 차트
with tab2:
    st.subheader("Seaborn 차트")

    # 1차원 Series로 안전하게 변환
    close_series = df["Close"]
    if isinstance(close_series, pd.DataFrame):
        close_series = close_series.squeeze()

    fig2, ax2 = plt.subplots()
    sns.lineplot(x=df.index, y=close_series, ax=ax2)
    ax2.set_title(f"{stock_name} 주가")
    ax2.set_xlabel("날짜")
    ax2.set_ylabel("종가 ($)")
    st.pyplot(fig2)


# Plotly 차트
with tab3:
    st.subheader("Plotly 차트")
    fig3 = px.line(df, x=df.index, y="Close", title=f"{stock_name} 주가 (인터랙티브)")
    st.plotly_chart(fig3, use_container_width=True)
