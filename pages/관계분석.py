
mbti 주제로 멀티페이지 웹앱을 만들고 싶은데 아이디어 내줘

MBTI 웹앱은 소비자행동/문화심리 관심사와도 잘 맞는 주제라, 단순 테스트를 넘어 마케팅적 요소를 넣으면 포트폴리오로도 활용도가 높습니다. 멀티페이지 구조에 맞춰 페이지별 아이디어를 정리했습니다.

핵심 테스트 & 결과 페이지
가장 기본이 되는 홈-테스트-결과 흐름으로, 16개 유형 카드를 그리드로 보여주고 클릭 시 상세 페이지로 이동하는 구조가 가장 널리 쓰입니다. 결과 페이지에는 유형별 특징, 강점/약점, 유명인 예시, 어울리는 직업 등을 카드 형태로 구성하면 완성도가 높아 보입니다. 실제 MBTI 검사 경험률이 2021년 31.6%에서 2023년 52.8%로 급증한 만큼, 결과 공유 기능(SNS 공유 버튼)을 넣으면 실사용성이 올라갑니다.

관계·궁합 분석 페이지
유형 간 궁합, 연애 스타일, 친구/직장 관계 매칭을 보여주는 페이지는 사용자 재방문을 유도하는 대표적인 기능입니다. 예를 들어 "내 유형 + 상대 유형"을 입력하면 궁합 점수와 관계 팁을 보여주는 인터랙티브 매칭 페이지를 만들 수 있습니다.

데이터 기반 심화 콘텐츠 페이지
전공 관심사(소비자행동, 문화적 차원)를 살려 다음과 같은 특화 페이지를 추가하면 차별화됩니다:

MBTI별 소비 성향/쇼핑 패턴 분석 페이지 (예: E-I축에 따른 구매 결정 방식 비교)

Hofstede 문화차원과 MBTI 분포를 연결한 국가별 통계 페이지 (실제 여론조사·설문 데이터 시각화)

커뮤니티 통계 페이지: 실시간 방문자 테스트 결과를 집계해 유형별 비율 차트로 보여주기

직업 추천 페이지: 유형별 적성 직군, 관련 산업 트렌드 소개

블로그/아티클 섹션: MBTI 관련 심리학·마케팅 인사이트 글 모음

기술 구현 방향
코딩 경험 수준에 따라 접근 방식이 달라지므로, 아래 표로 옵션을 비교했습니다.

방식	난이도	특징
HTML/CSS/JS 직접 코딩	중	페이지 라우팅 직접 구현, 커스터마이징 자유도 높음 
Python Reflex 프레임워크	중	Python만으로 멀티페이지 구현 가능, add_page로 라우트 관리 
AI 코딩툴 (v0 등)	하	프롬프트만으로 UI/기능 생성 후 배포까지 가능 
노코드 툴 (Waveon 등)	하	MBTI 전용 템플릿 제공, 코드 없이 배포 
Python 기초를 계획 중이시니 Reflex 프레임워크로 시작하면 홈 페이지에 16개 유형 카드를 배치하고 각 유형별 서브페이지(/istj, /enfp 등)를 라우트로 연결하는 구조를 비교적 쉽게 구현할 수 있습니다. 만약 빠르게 프로토타입만 만들어보고 싶다면 v0 같은 AI 툴로 5문항 테스트 앱을 프롬프트만으로 생성하고 바로 배포하는 방법도 있습니다.

어떤 방식으로 개발하실 계획이신가요? 코딩 실습(Python/Reflex 등)을 겸하고 싶으신지, 빠른 배포가 목적이신지에 따라 더 구체적인 페이지 구조와 코드 예시를 드릴 수 있습니다.

Claude Sonnet 5(으)로 준비됨
1. 스트림릿 클라우드에서 작동될 파이썬 코드를 만들어줘.
2. 핵심 테스트 &결과 페이지, 관계 분석 페이지, 직업 추천 페이지를 위한 코드를 각각 만들어줘
3. 별도의 라이브러리를 사용하면 안되고
4. 복사해서 붙여넣기 할 수 있는 완성된 코드를 부탁해.


app.py
Python

app.cpython-312.pyc
생성된 파일

script.py
코드
Streamlit Cloud에 바로 배포할 수 있는 단일 파일(app.py) 코드를 준비했습니다. streamlit 기본 내장 기능만 사용했고 별도 라이브러리는 필요 없습니다 .

파일 구성 및 배포 방법
이 코드는 하나의 app.py 파일 안에 사이드바 라디오 메뉴로 3개 페이지를 전환하는 멀티페이지 구조입니다. GitHub 저장소에 app.py만 올리고 Streamlit Community Cloud에서 "New app" → 저장소 선택 → main file path를 app.py로 지정하면 바로 배포됩니다. requirements.txt는 streamlit 한 줄만 있으면 충분합니다.

페이지별 구현 내용
핵심 테스트 & 결과 페이지: 12문항 슬라이더 설문으로 4개 축(E/I, S/N, T/F, J/P) 점수를 계산해 16가지 유형 중 하나를 도출하고, 유형별 별명·키워드·강점·약점·축별 점수를 보여줍니다. 하단에는 16개 유형 전체를 expander 카드로 훑어볼 수 있습니다.

관계 분석 페이지: 두 유형을 선택하면 미리 정의된 상성 데이터를 기반으로 궁합 점수(진행바)와 관계 팁을 무작위 범위 내에서 생성해 보여주고, 내 유형과 가장 잘 맞는/노력이 필요한 유형 목록도 표시합니다.

직업 추천 페이지: 유형별 추천 직업, 업무 강점, 주의점을 보여주고, E/I/S/N/T/F/J/P 축 필터로 관심 있는 성향의 유형들을 빠르게 비교할 수 있는 검색 기능을 넣었습니다.

세 페이지는 st.session_state로 연결되어 있어, 테스트 결과로 나온 유형이 관계 분석·직업 추천 페이지의 기본 선택값으로 자동 반영됩니다. 코드는 그대로 복사해서 app.py에 붙여넣으면 실행 가능하며, MBTI 데이터(닉네임, 키워드, 강점/약점, 궁합, 직업)는 딕셔너리 형태로 상단에 모아둬서 나중에 데이터를 쉽게 추가·수정할 수 있습니다.

Claude Sonnet 5(으)로 준비됨
혹시 핵심 테스트&결과 페이지랑 나머지 다른 페이지를 따로 저장해야하지는 않을까?


Multipage app, directory structure, and imports
discuss.streamlit

Session_state - how to use it to save values while ...
discuss.streamlit

Create a multipage app - Streamlit Docs
streamlit
결론부터 말하면, 지금 드린 단일 파일 코드는 정상적으로 작동하지만, Streamlit의 정식 멀티페이지 구조(pages/ 폴더 방식)로 나누면 더 깔끔하고 안정적입니다.

왜 나누는 게 좋은가
현재 코드는 사이드바 라디오로 "가짜 멀티페이지"를 만든 것이라, 코드가 길어질수록 유지보수가 어렵고 URL이 페이지별로 분리되지 않습니다. Streamlit이 공식 지원하는 방식은 app.py(entrypoint)와 같은 위치에 pages/라는 폴더를 만들고, 그 안에 1_핵심테스트.py, 2_관계분석.py, 3_직업추천.py처럼 파일을 나눠 넣는 것입니다. 이렇게 하면 Streamlit이 파일명을 인식해 사이드바 네비게이션과 각 페이지의 고유 URL을 자동으로 만들어줍니다.

session_state는 그대로 유지됩니다
페이지를 여러 파일로 나눠도 st.session_state는 하나의 세션 안에서 모든 페이지에 걸쳐 공유되므로, 테스트 결과(MBTI 유형)를 관계 분석·직업 추천 페이지에서도 그대로 불러올 수 있습니다. 다만 위젯의 key가 다른 페이지에서도 겹치지 않도록 주의해야 하고, 값이 한 번은 초기화된 후에 참조되어야 오류가 나지 않습니다.

권장 파일 구조
파일 경로	역할
app.py	진입점, 공통 데이터(MBTI_DATA)와 첫 화면(테스트&결과) 
pages/1_관계분석.py	관계 분석 페이지 
pages/2_직업추천.py	직업 추천 페이지 
이렇게 3개 파일로 분리하면 각 페이지가 독립된 .py 파일이 되어 코드 가독성이 좋아지고, GitHub에서 각 기능을 따로 수정하기도 쉬워집니다. 다만 MBTI_DATA 딕셔너리는 세 파일에서 공통으로 쓰이니 별도 파일(data.py)로 분리해 각 페이지에서 import하는 방식이 가장 효율적입니다.

지금 상태로도 실행에는 문제가 없지만, 앞으로 계속 기능을 추가하실 계획이라면 지금 분리해두는 게 관리하기 편합니다. 파일을 3개(app.py + pages 폴더 2개 + data.py)로 나눈 완성 코드를 바로 만들어드릴까요, 아니면 지금 단일 파일 그대로 유지하시겠어요?

Claude Sonnet 5(으)로 준비됨
파일을 3개(app.py + pages 폴더 2개 + data.py)로 나눈 완성 코드를 바로 만들어줘


app.py
Python

data.py
Python

requirements.txt
생성된 파일

app.cpython-312.pyc
생성된 파일

data.cpython-312.pyc
생성된 파일

1_관계분석.py
Python

2_직업추천.py
Python

1_관계분석.cpython-312.pyc
생성된 파일

2_직업추천.cpython-312.pyc
생성된 파일
요청하신 대로 파일 4개(app.py, data.py, pages/1_관계분석.py, pages/2_직업추천.py)로 나눈 완성 코드를 만들었고 모두 문법 오류 없이 컴파일 확인했습니다 .

폴더 구조 및 배포 방법
GitHub 저장소를 아래 구조로 그대로 만들면 Streamlit Cloud가 자동으로 사이드바 네비게이션을 생성합니다.

text
your-repo/
├── app.py          ← 진입점 (핵심 테스트 & 결과 페이지)
├── data.py          ← MBTI_DATA, QUESTIONS 공통 데이터
├── requirements.txt ← streamlit
└── pages/
    ├── 1_관계분석.py
    └── 2_직업추천.py
Streamlit Cloud에서 "New app" → 저장소 연결 → Main file path를 app.py로 지정하면 배포됩니다. pages/ 폴더 안 파일들은 파일명 앞 숫자 순서대로 사이드바에 자동 정렬되어 나타납니다.

각 파일 역할
data.py: 16개 유형의 닉네임·키워드·강점/약점·궁합·직업 데이터와 12개 테스트 문항을 모아둔 공통 모듈입니다. 세 페이지에서 from data import MBTI_DATA, QUESTIONS로 불러다 씁니다.

app.py: 첫 화면으로, 12문항 슬라이더 설문 후 4개 축 점수를 계산해 결과를 보여주고, 계산된 유형을 st.session_state.result_type에 저장합니다.

pages/1_관계분석.py: st.session_state.result_type을 기본값으로 불러와 궁합 점수와 관계 팁을 보여줍니다.

pages/2_직업추천.py: 마찬가지로 세션에 저장된 내 유형을 기본 선택값으로 사용해 추천 직업·강점·주의점을 보여주고 축 필터 검색 기능도 제공합니다.

세션 상태는 파일이 나뉘어도 동일한 브라우저 세션 안에서 공유되므로, 테스트 결과 유형이 자동으로 다른 두 페이지의 기본 선택값에 반영됩니다. 파일을 로컬에 저장한 뒤 그대로 GitHub에 올리고 requirements.txt만 함께 커밋하면 별다른 추가 설정 없이 바로 실행됩니다.

Claude Sonnet 5(으)로 준비됨
취미 추천 페이지도 추천하고 싶어. 반영해서 다른 코드들까지 수정해서 메인페이지, 관계분석 페이지, 직업 추천 페이지, 취미 추천 페이지, 딕셔너리 까지 수정해서 따로 만들어줘
2단계 완료


script.py
코드


3_취미추천.py
Python

3_취미추천.cpython-312.pyc
생성된 파일

script.py
코드
취미 추천 페이지를 추가하고 관련 파일들을 모두 수정 완료했습니다. 총 5개 파일 구조로 컴파일 오류 없이 준비됐습니다 .

업데이트된 파일 구조
text
your-repo/
├── app.py            ← 진입점 (핵심 테스트 & 결과 페이지, 사이드바 안내문 수정)
├── data.py           ← MBTI_DATA에 hobbies 필드 추가, QUESTIONS
├── requirements.txt  ← streamlit
└── pages/
    ├── 1_관계분석.py
    ├── 2_직업추천.py
    └── 3_취미추천.py   ← 신규 추가
주요 변경 사항
data.py: 16개 유형 각각에 hobbies 필드(취미 4~5개씩)를 새로 추가했습니다. 예를 들어 ISTJ는 독서·역사 다큐멘터리·체스·정원 가꾸기·모형 조립, ENFP는 여행·새로운 사람 만나기·창작 활동 등으로 성향에 맞게 구성했습니다.

pages/3_취미추천.py: 새 페이지로, 유형 선택 시 추천 취미와 성향 키워드를 보여주고, "랜덤 취미 뽑기" 버튼으로 오늘의 취미를 무작위 추천하는 기능도 넣었습니다. 직업 추천 페이지처럼 E/I/S/N/T/F/J/P 축 필터로 유형별 취미를 비교할 수도 있습니다.

app.py: 사이드바 안내 문구에 '취미 추천' 페이지를 추가해 사용자가 4개 페이지 모두 인지할 수 있게 했습니다.

관계분석·직업추천 페이지: 구조 변경 없이 기존 코드 그대로 유지되며, data.py의 hobbies 필드 추가는 다른 페이지 동작에 영향을 주지 않습니다.

5개 파일 모두 그대로 복사해서 해당 경로에 저장한 뒤 GitHub에 올리면 Streamlit Cloud에서 4개 페이지(테스트&결과, 관계분석, 직업추천, 취미추천)가 사이드바에 순서대로 나타납니다.

Claude Sonnet 5(으)로 준비됨

import random
import streamlit as st
from data import MBTI_DATA

st.set_page_config(page_title="관계 분석", page_icon="💞", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

st.title("💞 MBTI 관계 분석")
st.write("나와 상대방의 유형을 선택하면 궁합과 관계 팁을 알려드립니다.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: **{st.session_state.result_type}**")

types = list(MBTI_DATA.keys())
default_idx = types.index(st.session_state.result_type) if st.session_state.result_type in types else 0

col1, col2 = st.columns(2)
with col1:
    my_type = st.selectbox("나의 유형", types, index=default_idx)
with col2:
    other_type = st.selectbox("상대방의 유형", types, index=(default_idx + 1) % 16)

if st.button("궁합 확인하기"):
    my_data = MBTI_DATA[my_type]

    if other_type in my_data["compat_best"]:
        level, msg = "매우 좋음 🟢", "서로의 강점이 보완되는 이상적인 궁합입니다."
        score = random.randint(85, 98)
    elif other_type in my_data["compat_worst"]:
        level, msg = "노력 필요 🔴", "가치관의 차이가 있을 수 있어 서로 이해하려는 노력이 중요합니다."
        score = random.randint(40, 60)
    else:
        level, msg = "보통 🟡", "무난하게 잘 지낼 수 있는 관계입니다."
        score = random.randint(65, 84)

    st.subheader(f"{my_type} ❤️ {other_type}")
    st.metric("궁합 점수", f"{score}점")
    st.write(f"**{level}** — {msg}")
    st.progress(score / 100)

    st.subheader("💡 관계 팁")
    if "E" in my_type and "I" in other_type:
        st.markdown("- 서로의 에너지 충전 방식(외부활동 vs 혼자 시간)을 존중해주세요.")
    if "T" in my_type and "F" in other_type:
        st.markdown("- 감정적 배려와 논리적 설명 사이의 균형을 맞춰보세요.")
    if "J" in my_type and "P" in other_type:
        st.markdown("- 계획성과 즉흥성의 차이를 갈등이 아닌 다양성으로 받아들여보세요.")
    st.markdown("- 정기적으로 서로의 생각을 솔직하게 공유하는 시간을 가지세요.")

st.markdown("---")
st.subheader("🌟 나와 잘 맞는 유형 한눈에 보기")
st.write(f"**{my_type}**와 가장 잘 맞는 유형: " + ", ".join(MBTI_DATA[my_type]["compat_best"]))
st.write(f"**{my_type}**와 노력이 필요한 유형: " + ", ".join(MBTI_DATA[my_type]["compat_worst"]))
