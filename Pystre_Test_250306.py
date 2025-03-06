import streamlit as st
import datetime
import pyupbit

# 사이드바 설정
st.sidebar.header("설정")
ticker = st.sidebar.text_input("티커", "KRW-BTC")
interval = st.sidebar.selectbox("시간 간격", ["minute1", "minute3", "minute5", "minute15", "minute30", "minute60", "day"])
date_selected = st.sidebar.date_input("날짜", datetime.date.today())
count = st.sidebar.slider("데이터 개수", min_value=10, max_value=500, value=100)

# 종료 날짜 (선택한 날짜의 다음날)
to = str(date_selected + datetime.timedelta(days=1))

# 데이터 가져오기
df = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

if df is None:
    st.error("데이터를 불러오지 못했습니다. 입력값을 확인하세요.")
else:
    st.title(f"{ticker} {date_selected} 차트")
    st.line_chart(df['close'])
    st.write("데이터 미리보기:")
    st.dataframe(df.head())