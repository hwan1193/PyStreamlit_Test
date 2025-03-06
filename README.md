# PyStreamlit_Test
Streamlit은 파이썬으로 손쉽게 인터랙티브한 웹 애플리케이션을 만들 수 있는 오픈소스 라이브러리입니다. 주로 데이터 사이언스와 머신러닝 프로젝트에서 빠르게 프로토타입이나 대시보드를 구축할 때 많이 사용되며, 복잡한 웹 개발 지식 없이도 몇 줄의 코드로 멋진 웹&amp;앱을 만들 수 있는 장점이 있습니다.

![local host_Test결과 실행 내용03_250306](https://github.com/user-attachments/assets/20582207-ddce-4991-af8d-b4301f4fc83c)

========================================================================================
1. 사이드바 설정
st.sidebar.text_input(), selectbox(), date_input(), slider()를 사용해 사용자가 티커, 시간 간격, 날짜, 데이터 개수를 선택할 수 있도록 합니다.

2. 데이터 가져오기
pyupbit.get_ohlcv() 함수를 이용해 선택한 조건에 맞는 OHLCV 데이터를 가져옵니다.
선택한 날짜의 다음날을 종료 날짜(to)로 지정하여, 해당 날짜의 데이터를 불러옵니다.

3. 데이터 출력
데이터가 성공적으로 불러와졌다면, 제목을 표시하고, 종가(close)를 기준으로 선 차트를 그리고, 데이터 프레임의 일부를 미리 보여줍니다.
데이터가 없을 경우, 에러 메시지를 출력합니다.

![image](https://github.com/user-attachments/assets/5861db8b-a204-499e-803f-abd65252bac8)
