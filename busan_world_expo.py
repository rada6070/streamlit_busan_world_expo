import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

# st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://live.lge.co.kr/wp-content/uploads/2015/07/%EB%B0%94%EB%8B%A4.jpg");
#              background-attachment: fixed;
#              background-size: cover
#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# Remove whitespace from the top of the page and sidebar

sl_box = [ 'English', '한국어' ]

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


with st.sidebar:
    choose = option_menu("부산 2030 월드 엑스포", ["부산 월드 엑스포 홍보", "부산의 지도", "부산 관광지 그래프"],
                         icons=['house', 'map', 'bar-chart'],
                         menu_icon="bi bi-menu-up", default_index=0,
                         styles={
        "menu-title": {"color": "black"},
        "container": {"padding": "5!important", "color": "black", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "color": "black", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

st.sidebar.image("https://i.namu.wiki/i/tvGyhYywWMsAcu6DB_LNqDgXsPeaXzDt4Su8mc8pckqINu1ceRlXh6mqVaquCFE9vCBk9Pduf9xkzWr0gcC_Ng.svg", use_column_width=True)

st.sidebar.selectbox( 'lang select' , sl_box )

if choose == "부산 월드 엑스포 홍보" :
    # 페이지 제목과 부산 월드 엑스포 2030 로고 이미지 표시
    st.title("부산 월드 엑스포 2030")
    st.image("https://image.edaily.co.kr/images/Photo/files/NP/S/2022/06/PS22062300100.jpg", use_column_width=True)

    # 월드 엑스포 2030에 대한 간단한 설명 추가
    st.write("부산 월드 엑스포 2030은 세계 각국의 문화와 기술을 전시하는 국제 행사입니다.")

    # 주요 행사 정보 표시
    st.subheader("주요 행사 정보")
    st.write("날짜: 2030년 5월 1일 - 10월 31일")
    st.write("장소: 부산, 대한민국")
    st.write("테마: '새로운 세계를 여는 혁신과 지속가능성'")

    # 부산 월드 엑스포 2030 관련 이미지 표시
    st.subheader("이미지 갤러리")
    image_urls = [
        "https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/",
        "https://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimizehttps://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimize",
        "https://newsroom-prd-data.s3.ap-northeast-2.amazonaws.com/wp-content/uploads/2022/11/%EC%97%91%EC%8A%A4%ED%8F%AC-%EC%B9%BC%EB%9F%BC_%EC%97%91%EC%8A%A4%ED%8F%AC%EA%B0%80-%EB%AA%B0%EA%B3%A0-%EC%98%A8-%EB%86%80%EB%9D%BC%EC%9A%B4-%EB%B3%80%ED%99%94_04.png",
    ]

    # 이미지 갤러리를 가로로 표시
    st.image(image_urls, width=200)

    #월드 엑스포에 대한 정보를 더 자세히 보여주는 링크 제공
    st.subheader("더 알아보기")
    st.write("공식 웹사이트에서 더 많은 정보를 확인하세요:")
    st.write("[www.expo2030busan.kr](https://www.expo2030busan.kr/index.do)")

if choose == "부산의 지도" :
    st.title('부산의 지도') 
    ## 위도와 경도 값을 가진 샘플 DataFrame 생성
    data = pd.DataFrame({
        'latitude': [35.1795543],
        'longitude': [129.0756416]
    })
    
    ## 데이터를 사용하여 지도 생성
    st.map(data)

if choose == "부산 관광지 그래프" :
    st.title('부산 관광지 선호도 그래프')
    chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=['감천 문화 마을', '자갈치 시장', '국제 시장', '부전 시장'])

    st.bar_chart(chart_data)
