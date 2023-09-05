import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import io

#언어 셀렉트 박스 변수

sl_box = [ 'English', '한국어', '日本語', '中文 简体 ', '中文 繁體 ' ]

sl_sc = st.sidebar.selectbox( 'lang select' , sl_box )

if sl_sc == sl_box[0] :
        global side_bar_main
        global side_bar_sub_1
        global side_bar_sub_2
        global side_bar_sub_3

        global page_1_title
        global page_1_explain_1

        global page_1_subheader_1
        global page_1_explain_when
        global page_1_explain_where
        global page_1_explain_thema

        global page_1_image_gall

        global page_1_subheader_2
        global page_1_explain_2

        global page_2_title

        global page_3_title
        global page_3_columns_1
        global page_3_columns_2
        global page_3_columns_3
        global page_3_columns_4

        side_bar_main = "Busan 2030 World Expo"
        side_bar_sub_1 = "Promotion of Busan World Expo"
        side_bar_sub_2 = "Map of Busan"
        side_bar_sub_3 = "Busan Tourist Site Preference Graph"

        page_1_title = "Promotion of Busan World Expo"
        page_1_explain_1 = "Busan World Expo 2030 is an international event that displays cultures and technologies from around the world."

        page_1_subheader_1 = "Key Event Information"
        page_1_explain_when = "Date: May 1, 2030 - October 31, 2030"
        page_1_explain_where = "Location: Busan, South Korea"
        page_1_explain_thema = "Theme: 'Innovation and Sustainability Opening a New World'"

        page_1_image_gall = "Image Gallery"

        page_1_subheader_2 = "Learn more information"
        page_1_explain_2 = "Check out the official website for more information:"

        page_2_title = "Map of Busan"

        page_3_title = "Busan Tourist Site Preference Graph"
        page_3_columns_1 = "Gamcheon Culture Village"
        page_3_columns_2 = "Jagalchi Market"
        page_3_columns_3 = "International Market"
        page_3_columns_4 = "Bujeon Market"

elif sl_sc == sl_box[1] :
        side_bar_main = "부산 2030 월드 엑스포"
        side_bar_sub_1 = "부산 월드 엑스포 홍보"
        side_bar_sub_2 = "부산의 지도"
        side_bar_sub_3 = "부산 관광지 선호도 그래프"

        page_1_title = "부산 2030 월드 엑스포"
        page_1_explain_1 = "부산 월드 엑스포 2030은 세계 각국의 문화와 기술을 전시하는 국제 행사입니다."

        page_1_subheader_1 = "주요 행사 정보"
        page_1_explain_when = "날짜: 2030년 5월 1일 - 10월 31일"
        page_1_explain_where = "장소: 부산, 대한민국"
        page_1_explain_thema = "테마: '새로운 세계를 여는 혁신과 지속가능성'"

        page_1_image_gall = "이미지 갤러리"

        page_1_subheader_2 = "더 알아보기"
        page_1_explain_2 = "공식 웹사이트에서 더 많은 정보를 확인하세요:"

        page_2_title = "부산의 지도"

        page_3_title = "부산 관광지 선호도 그래프"
        page_3_columns_1 = "감천 문화 마을"
        page_3_columns_2 = "자갈치 시장"
        page_3_columns_3 = "국제 시장"
        page_3_columns_4 = "부전 시장"

elif sl_sc == sl_box[2] :
        side_bar_main = "釜山2030ワールドエキスポ"
        side_bar_sub_1 = "釜山ワールドエキスポ広報"
        side_bar_sub_2 = "釜山の地図"
        side_bar_sub_3 = "釜山観光地選好度グラフ"

        page_1_title = "釜山2030ワールドエキスポ"
        page_1_explain_1 = "釜山ワールドエキスポ2030は世界各国の文化と技術を展示する国際行事です。"

        page_1_subheader_1 = "主な行事情報"
        page_1_explain_when = "日時:2030年5月1日-10月31日"
        page_1_explain_where = "場所:釜山、大韓民国"
        page_1_explain_thema = "テーマ:「新しい世界を切り開く革新と持続可能性」"

        page_1_image_gall = "イメージギャラリー"

        page_1_subheader_2 = "もっと調べる"
        page_1_explain_2 = "公式ウェブサイトでより多くの情報をご確認ください:"

        page_2_title = "釜山の地図"

        page_3_title = "釜山観光地選好度グラフ"
        page_3_columns_1 = "甘川文化村"
        page_3_columns_2 = "チャガルチ市場"
        page_3_columns_3 = "国際市場"
        page_3_columns_4 = "釜田市長"

elif sl_sc == sl_box[3] :
        side_bar_main = "釜山2030年世界博览会"
        side_bar_sub_1 = "釜山世界博览会宣传"
        side_bar_sub_2 = "釜山地图"
        side_bar_sub_3 = "釜山观光地偏好度图表"

        page_1_title = "釜山2030年世界博览会"
        page_1_explain_1 = "釜山世界博览会2030是展示世界各国文化和技术的国际活动。"

        page_1_subheader_1 = "主要活动信息"
        page_1_explain_when = "日期:2030年5月1日-10月31日"
        page_1_explain_where = "地点:釜山，韩国"
        page_1_explain_thema = "主题:'开启新世界的革新和可持续性'"

        page_1_image_gall = "图片画廊"

        page_1_subheader_2 = "更多了解"
        page_1_explain_2 = "请在官方网站上查看更多信息 :"

        page_2_title = "釜山地图"

        page_3_title = "釜山观光地偏好度图表"
        page_3_columns_1 = "甘川文化村"
        page_3_columns_2 = "札嘎其市场"
        page_3_columns_3 = "国际市场"
        page_3_columns_4 = "副前市长"

elif sl_sc == sl_box[4] :
        side_bar_main = "釜山2030年世界博覽會"
        side_bar_sub_1 = "釜山世界博覽會宣傳"
        side_bar_sub_2 = "釜山地圖"
        side_bar_sub_3 = "釜山觀光地偏好度圖表"

        page_1_title = "釜山2030年世界博覽會"
        page_1_explain_1 = "釜山世界博覽會2030是展示世界各國文化和技術的國際活動。"

        page_1_subheader_1 = "主要活動信息"
        page_1_explain_when = "日期:2030年5月1日-10月31日"
        page_1_explain_where = "地點:釜山，韓國"
        page_1_explain_thema = "主題:'開啓新世界的革新和可持續性'"

        page_1_image_gall = "圖片畫廊"

        page_1_subheader_2 = "更多瞭解"
        page_1_explain_2 = "請在官方網站上查看更多信息 :"

        page_2_title = "釜山地圖"

        page_3_title = "釜山觀光地偏好度圖表"
        page_3_columns_1 = "甘川文化村"
        page_3_columns_2 = "札嘎其市場"
        page_3_columns_3 = "國際市場"
        page_3_columns_4 = "副前市長"

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
    choose = option_menu(side_bar_main, [side_bar_sub_1, side_bar_sub_2, side_bar_sub_3],
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

if choose == side_bar_sub_1 :
    # 페이지 제목과 부산 월드 엑스포 2030 로고 이미지 표시
    st.title(side_bar_sub_1)
    st.image("https://image.edaily.co.kr/images/Photo/files/NP/S/2022/06/PS22062300100.jpg", use_column_width=True)

    # 월드 엑스포 2030에 대한 간단한 설명 추가
    st.write(page_1_explain_1)

    # 주요 행사 정보 표시
    st.subheader(page_1_subheader_1)
    st.write(page_1_explain_when)
    st.write(page_1_explain_where)
    st.write(page_1_explain_thema)

    # 부산 월드 엑스포 2030 관련 이미지 표시
    st.subheader(page_1_image_gall)
    image_urls = [
        "https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/https://thumb.mt.co.kr/06/2021/11/2021110114172440715_1.jpg/dims/optimize/",
        "https://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimizehttps://thumb.mtstarnews.com/06/2023/04/2023040312452334740_1.jpg/dims/optimize",
        "https://newsroom-prd-data.s3.ap-northeast-2.amazonaws.com/wp-content/uploads/2022/11/%EC%97%91%EC%8A%A4%ED%8F%AC-%EC%B9%BC%EB%9F%BC_%EC%97%91%EC%8A%A4%ED%8F%AC%EA%B0%80-%EB%AA%B0%EA%B3%A0-%EC%98%A8-%EB%86%80%EB%9D%BC%EC%9A%B4-%EB%B3%80%ED%99%94_04.png",
    ]

    # 이미지 갤러리를 가로로 표시
    st.image(image_urls, width=200)

    #월드 엑스포에 대한 정보를 더 자세히 보여주는 링크 제공
    st.subheader(page_1_subheader_2)
    st.write(page_1_explain_2)
    st.write("[www.expo2030busan.kr](https://www.expo2030busan.kr/index.do)")

if choose == side_bar_sub_2 :
    st.title(side_bar_sub_2) 
    # 제목 생성 
    df = pd.DataFrame( [ 35.1795543, 129.0756416 ] , columns = [ 'lat', 'lon' ] )
    st.map(df)
    # 지도 생성 

if choose == side_bar_sub_3 :
    st.title(side_bar_sub_3)

