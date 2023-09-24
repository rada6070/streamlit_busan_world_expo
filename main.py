import io
import matplotlib
import folium

import streamlit as st
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt

import i18n
import style
import assets
import data
import requests
import json
import random

from PIL import Image
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_js_eval import get_browser_language

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 관광지

용궁사1 = "해동용궁사를 추천합니다. 해동용궁사를 방문하면 역사와 자연의 아름다움이 어우러진 특별한 경험을 만날 수 있습니다."
용궁사2 = "해동용궁사를 추천합니다. 해동용궁사는 한국의 불교 역사와 문화를 체험하고 명상과 평화로움을 즐길 수 있는 최고의 장소 중 하나입니다."
용궁사3 = "해동용궁사를 추천합니다. 해동용궁사는 아름다운 건축물과 자연 경관으로 둘러싸여 있어, 사진 찍기에도 훌륭한 곳입니다"
용궁사4 = "해동용궁사를 추천합니다. 역사와 미를 동시에 즐기고 싶다면 해동용궁사가 더할 나위 없이 좋은 선택입니다."

해운대1 = "해운대를 추천합니다. 일몰을 바라보며 해운대 해변을 산책하면 일상의 스트레스를 잊을 수 있는 최적의 힐링 장소입니다."
해운대2 = "해운대를 추천합니다. 무엇보다, 해운대는 낮과 밤 모두 활기차고 아름다운 풍경을 선사하여 방문자들에게 특별한 경험을 선사합니다."
해운대3 = "해운대를 추천합니다. 해운대는 국내 최고의 해수욕장 중 하나로, 화사한 모래사장과 푸른 바다가 매력적입니다."

남포동1 = "남포동을 추천합니다. 남포동은 부산의 역사적인 중심지로, 오랜 역사와 현대적인 매력이 어우러진 곳입니다."
남포동2 = "남포동을 추천합니다. 현지 음식을 즐기기 위해 남포동 근처의 식당과 먹거리 거리를 탐험할 수 있습니다."
남포동3 = "남포동을 추천합니다. 이곳에서는 다양한 상점과 시장에서 쇼핑을 즐기며 지역 특산품을 구입할 수 있습니다."

태종대1 = "태종대를 추천합니다. 태종대는 부산의 아름다운 해안에 자리하고 있으며, 푸른 바다와 함께 자연 경관을 감상하기에 최적의 장소입니다."
태종대2 = "태종대를 추천합니다. 역사와 자연의 조화로운 분위기와 아름다운 경관은 방문자들에게 특별한 경험을 선사합니다."

송도해상케이블카1 = "송도해상케이블카를 추천합니다. 특히 일몰 시간에 케이블카를 타면 더욱 멋진 풍경을 만날 수 있으며, 사진을 찍기에도 좋은 장소 중 하나입니다."
송도해상케이블카2 = "송도해상케이블카를 추천합니다. 송도해상케이블카를 타면 자연과 도시의 조화로운 아름다움과 바다의 경치를 경험하며 특별한 추억을 만들 수 있습니다."

감천문화마을1 = "감천문화마을을 추천합니다. 감천문화마을은 부산에 위치한 예술과 문화가 공존하는 공간으로, 독특한 건축물과 예술 작품들이 즐비한 곳입니다."
감천문화마을2 = "감천문화마을을 추천합니다. 이 마을은 전통과 현대가 만나는 곳으로, 고요한 골목길과 예술 작품이 함께 어울려 아름다운 풍경을 제공합니다."

# 맛집

해목1 = "해목 해운대점을 추천합니다. 해목 해운대는 유명한 고급식당이고 장어덮밥과 장어와 관련된 식사, 참치, 연어 등 해산물을 주로 다루는 맛집입니다."

선창횟집1 = "선창횟집 해운대점을 추천합니다. 선창횟집은 많은 인원이 외식하기 좋은 곳이고 회 코스요리를 적당한 가격에 바다를 보면서 즐길 수 있습니다."

금수복국1 = "금수복국 해운대본점을 추천합니다. 금수복국 해운대본점은 복어와 복국을 주로 다루는 맛집이고 사람이 많아도 복잡하지 않고 친절하게 대응하는 서비스가 뛰어난 맛집입니다."

이재모피자1 = "이재모피자 테이크아웃점 부산중구점을 추천합니다. 부산의 유명한 피자 맛집으로 많은 사람들에게 실망시키지 않는 맛으로 많은 사람들에게 추천받는 부산의 맛집중 하나입니다."

할매국밥1 = "60년전통 할매국밥 범일동점을 추천합니다. 부산의 음식을 떠올리라하면 대부분 국밥을 떠올리고 국밥맛집인 60년전통 할매국밥 범일동점을 추천합니다. 만약 처음 먹는다면 최고의 음식점으로 경험하고 싶은분들께 추천합니다."

# 자연/공원

해운대해수욕장1 = "해운대 해수욕장을 추천합니다. 여름에는 수영, 해변 놀이, 서핑 등 다양한 레저 활동을 즐기기에 최적의 장소이며, 겨울에는 해안을 따라 산책하기에도 좋습니다."
해운대해수욕장2 = "해운대 해수욕장을 추천합니다. 해운대 해수욕장 근처에는 다양한 레스토랑, 카페, 상점들이 있어 지역 음식과 쇼핑을 즐길 수 있습니다."
해운대해수욕장3 = "해운대 해수욕장을 추천합니다. 부산의 대표적인 관광지 중 하나로, 교통 접근성이 우수하여 관광객들에게 즐거운 휴가를 제공합니다."

광안리1 = "광안리 해수욕장을 추천합니다. 광안대교의 조명은 밤에 특히 아름다우며, 해변가에서 산책하며 로맨틱한 분위기를 느낄 수 있습니다."
광안리2 = "광안리 해수욕장을 추천합니다. 여름에는 수영, 서핑, 비치발리볼 등 다양한 레저 활동을 즐기며, 겨울에는 해안을 따라 산책하는 것도 좋습니다."

기념공원1 = "UN기념공원을 추천합니다. UN기념공원은 역사적으로 중요한 장소로서 평화와 국제 협력에 대한 의미를 다시 생각해보고 싶을 때 방문하기 좋은 장소입니다."
기념공원2 = "UN기념공원을 추천합니다. 유엔과 평화에 관한 다양한 정보와 전시물이 전시되어 있어, 평화와 국제 협력에 대한 이해를 높일 수 있습니다."
기념공원3 = "UN기념공원을 추천합니다. 공원은 평화와 협력의 가치를 강조하며, 다양한 기념비와 조형물들이 자리하고 있어 역사와 문화를 체험할 수 있습니다."

용두산1 = "용두산 공원을 추천합니다. 용두산 공원은 자연 속에서 휴식을 즐기고자 하는 사람들에게 좋은 장소로, 역사와 자연의 조화로운 아름다움을 느낄 수 있습니다."
용두산2 = "용두산 공원을 추천합니다. 주변에 부산타워가 있고 옆에 남포동이 있어 주변 번화가에 쉽게 접근할 수 있습니다."

송도1 = "송도 해수욕장을 추천합니다. 송도 해수욕장 부근에는 송도 센트럴파크와 다양한 관광 명소가 있어, 해변에서 레저를 즐긴 후에 관광할 곳이 많습니다."
송도2 = "송도 해수욕장을 추천합니다. 부산 송도 해수욕장은 여름 휴가와 해변에서의 휴식을 즐기기에 최적의 목적지 중 하나로, 가족이나 친구와 함께 즐거운 시간을 보낼 수 있습니다."
송도3 = "송도 해수욕장을 추천합니다. 해변이 깨끗하게 관리되어 있어 수영, 썬베드에서 휴식, 비치발리볼, 서핑 등 다양한 해변 활동을 즐기기에 안성맞춤입니다."

이기대1 = "이기대를 추천합니다. 이기대는 가족 나들이, 산책, 피크닉, 사진 찍기, 그리고 자연을 즐기는 활동을 하기에 최적의 장소입니다."
이기대2 =  "이기대를 추천합니다. 오륙도 스카이워크부터 시작해서 이기대를 걷는 해안산책로가 오륙도-농바위-어울마당-이기대-동생말 경로로 4.6km 이어져 있는데 말 그대로 바위 절벽에 구름다리와 울타리로 길을 낸 곳이라 경치가 좋습니다."

# 카페/ 디저트

모모스커피1 = "모모스커피 부산본점을 추천합니다. 주택을 개조한 듯한 카페 인테리어가 인상깊은 감성카페입니다."
모모스커피2 = "모모스커피 부산본점을 추천합니다. 베이커리 종류의 맛이 상당하며 다양한 커피의 풍미가 깊다는 평이 자자합니다."

에테르1 = "에테르 영도점을 추천합니다. 꼭대기 테라스에서 바다를 보면서 먹기 좋을 정도로 뷰가 좋습니다."
에테르2 = "에테르 영도점을 추천합니다. 굉장히 커다란 건물 하나가 전부 카페여서 많은 사람들이 갈 수 있으며 다양한 각도에서 경치를 즐길 수 있습니다."

초량1 = "초량1941 초량점을 추천합니다. 일본식의 카페라서 이색적인 느낌이 나는 외관을 보유하고 있습니다 그로인해 많은 사람들이 찾아가고 대부분의 음료가 우유종류 인것을 생각하고 가셔야 합니다."
초량2 = "초량1941 초량점을 추천합니다. 올라가는길이 힘드니 차량을 통해 이동하지 않는것을 추천하는데 그것을 감안해도 건물의 외관이 굉장히 아름다워 찾아갈만한 곳 입니다."

코랄라니1 = "코랄라니 부산기장점을 추천합니다. 코랄라니는 경관이 최고인 대형 베이커리 카페입니다."
코랄라니2 = "코랄라니 부산기장점을 추천합니다. 코랄라니는 대형 베이커리이고 경관이 굉장히 좋기에 많은 사람을 수용하면서 바다에 위치하여 야외석에서 바다를 보면서 먹기 좋은 카페입니다."

오션브리즈1 = "오션브리즈 청사포점을 추천합니다. 카페가 굉장히 넓어 많은 사람들이 갈 수 있고 바다를 보면서 먹기 좋은 카페입니다."

볼트1 = "Cafe de 220VOLT 영도점을 추천합니다. 카페의 위쪽에서는 영도에서 부산바다와 시내를 내려다 볼 수 있는 매력적인 경관을 가지고 있습니다."
볼트2 = "Cafe de 220VOLT 영도점을 추천합니다. 부산에서 힐링하면서 옥상 루프탑에서 바람을 쐴 수 있을 정도로 멋진 분위기를 가진 카페입니다."

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.markdown("<h1 style='text-align: center; color: black;'>부산 EXPO 챗봇 </h1>", unsafe_allow_html=True)

# 디자인 칸 2개로 분리
col1, col2= st.columns([1,1])

# 브라우저 기본 언어 불러오기
try:
    preferred_language = i18n.FindLangByTag(get_browser_language())
except AttributeError:
    preferred_language = "ko"


# 스타일 시트 불러오기
assets.import_assets("assets/style.css", st)

# 이미지 중앙
with col1 :
    col11, col12, col13 = st.columns([1,6,1])

    with col11:
        st.write("")
        
    with col12:
        st.image('data:image/png;base64,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', width=180)

    with col13:
        st.write("") 
        
# 언어 선택
with col2 :
  language_list = list(i18n.LangList().keys())
  language_select = str(
      st.selectbox("Change Language", ["브라우저 기본 설정", *language_list])
  )
  
  if language_select == "브라우저 기본 설정":
      language = i18n.LoadLangByCode(preferred_language)
  else:
      language = i18n.LoadLangByCode(i18n.LangList(language_select))

class ChatBot:
    def __init__(self):
        # 질문과 대답을 매핑한 딕셔너리를 초기화합니다.
        self.responses = {
            "---질문 선택---": [
                "질문을 선택하고 답변해주세요"
            ],

            # 관광지 질문과 대답
            "부산에서 가볼만한 관광지에 대해 추천해줘": [
                용궁사1,
                용궁사2,
                용궁사3,
                용궁사4,
                해운대1,
                해운대2,
                해운대3,
                남포동1,
                남포동2,
                남포동3,
                태종대1,
                태종대2,
                송도해상케이블카1,
                송도해상케이블카2,
                감천문화마을1,
                감천문화마을2
            ],
            
            # 맛집 질문과 대답
            "부산에서 가볼만한 맛집에 대해 추천해줘": [
                해목1,
                선창횟집1,
                금수복국1,
                이재모피자1,
                할매국밥1
            ],

            # 자연/공원 질문과 대답
            "부산에서 가볼만한 자연/공원에 대해 추천해줘": [
                해운대해수욕장1,
                해운대해수욕장2,
                해운대해수욕장3,
                광안리1,
                광안리2,
                기념공원1,
                기념공원2,
                기념공원3,
                용두산1,
                용두산2,
                송도1,
                송도2,
                송도3,
                이기대1,
                이기대2
            ],

            # 카페/디저트 질문과 대답
            "부산에서 가볼만한 카페/디저트에 대해 추천해줘": [
                모모스커피1,
                모모스커피2,
                에테르1,
                에테르2,
                초량1,
                초량2,
                코랄라니1,
                코랄라니2,
                오션브리즈1,
                볼트1,
                볼트2
            ],

            # 엑스포 기대효과 질문과 대답
            "부산에 엑스포가 개최될 시 기대효과에 대해 알려줘": [
                "EXPO, 올림픽, 월드컵 등 국제 행사는 그 행사가 개최되는 도시나 국가에 경제적 이익과 홍보 효과를 가져다 줄 수 있습니다.",
                "스마트 혁신 강국으로서 국가의 위상을 제고할 수 있습니다.",
                "부산을 거점으로 제2경제권 부흥을 통해 국가가 균형을 이루어 발전할 수 있습니다.",
                "예상 관람객을 약 3,480만명이고 약 43조원의 생산을 유발하고, 약 18조원의 부가가치를, 약 50만명이 일자리를 가질 수 있다고 기대를 할 수 있습니다.",
                "많은 외국인들이 엑스포를 관람하러 오기 때문에 관광산업이 거대해져 지역에 큰 활기를 불러올 수 있습니다.",
                "엑스포는 국제 무대에서 도시의 이미지를 높이는데 도움이 되므로, 이를 통해 부산은 세계적으로 더 많은 관심을 받아 긍정적인 평가를 받을 수 있습니다."
            ],

            # 엑스포 질문과 대답
            "엑스포에 대해 알려줘": [
                "엑스포는 국제 박람회를 가리키는 용어로, 다양한 국가와 기업이 과학, 기술, 문화, 경제, 환경 등 다양한 주제를 공유하고 전시하는 국제 행사를 말합니다.",
                "엑스포는 특정 주제 혹은 주제에 기반되어 개최되고 대부분 그 해의 글로벌 이슈와 관련이 있어 참가자들은 해당 주제에 대한 해결책과 혁신적인 아이디어를 제시합니다.",
                "엑스포는 대규모 전시관과 공연장을 포함해 참가 국가들은 자국의 다양한 작품을 전시하고 다양한 문화 행사와 공연을 개최합니다.",
                "엑스포는 지속 가능한 발전과 환경 보호와 관련된 주제를 다루고 환경 친화적인 기술과 사회적 책임에 대한 논의가 이루어지며, 환경 보호 의식을 증진시킬 수 있습니다.",
                "엑스포는 혁신과 기술 개발을 촉진하는 플랫폼으로 활용되고 참가 국가들은 자국의 과학과 기술 분야의 발전을 선보여 혁신적인 솔루션을 제공합니다."
            ]
        }

    
    def get_random_question(self, current_question):
        # 현재 질문을 제외하고 랜덤하게 질문을 선택합니다.
        question_list = list(self.responses.keys())
        question_list.remove(current_question)
        return random.choice(question_list)
    
    def get_response(self, question):
        # 질문에 해당하는 대답을 랜덤하게 선택합니다.
        if question in self.responses:
            answers = self.responses[question]
            return random.choice(answers)
        else:
            return "죄송해요. 제가 대답할 수 있는 내용이 아닙니다."

# ChatBot 인스턴스를 생성합니다.
chatbot = ChatBot()

# 스트림릿 앱의 제목을 설정합니다.
st.title("챗봇")

# 각 질문에 대한 버튼을 생성하고 버튼이 클릭되면 해당 질문에 대한 답변을 출력합니다.
question_options = list(chatbot.responses.keys())[1:]  # 첫 번째 옵션인 "---질문 선택---"은 제외합니다.

for question in question_options:
    if st.button(question):
        response = chatbot.get_response(question)
        st.write(f"{question}라는 질문을 받았습니다.")
        st.write(f"{response}")

st.title(language["side_bar_sub_2"])
m = folium.Map(location=[35.1795543, 129.0756416], zoom_start=11)

st_data = st_folium(m, width=725)

