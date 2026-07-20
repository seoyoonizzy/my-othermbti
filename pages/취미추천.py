import random
import streamlit as st
from data import MBTI_DATA, MBTI_EMOJI

st.set_page_config(page_title="취미 추천", page_icon="🎨", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

def get_hobby_icon(hobby: str) -> str:
    mapping = [
        (["독서", "책", "시 읽기", "소설"], "📚"),
        (["다큐멘터리", "영화", "영상"], "🎬"),
        (["체스", "퍼즐", "퀴즈", "보드게임"], "♟️"),
        (["정원", "식물"], "🌿"),
        (["모형", "DIY", "공예"], "🔨"),
        (["베이킹", "요리"], "🍳"),
        (["뜨개질"], "🧶"),
        (["사진", "촬영"], "📷"),
        (["등산"], "⛰️"),
        (["글쓰기", "일기", "다이어리"], "✍️"),
        (["명상"], "🧘"),
        (["심리학"], "🧠"),
        (["봉사"], "🤲"),
        (["코딩", "게임 개발", "프로젝트"], "💻"),
        (["자동차", "드라이브", "기계"], "🚗"),
        (["캠핑"], "🏕️"),
        (["자전거"], "🚴"),
        (["게임"], "🎮"),
        (["그림"], "🖌️"),
        (["음악"], "🎵"),
        (["여행"], "✈️"),
        (["춤", "댄스"], "💃"),
        (["파티", "클럽"], "🎊"),
        (["쇼핑"], "🛍️"),
        (["스포츠", "익스트림"], "🏃"),
        (["새로운 사람", "네트워킹", "모임"], "🗣️"),
        (["공연", "연극"], "🎭"),
        (["토론", "디베이트"], "💬"),
        (["창업", "투자", "리더십", "자기계발"], "📈"),
        (["골프"], "⛳"),
        (["멘토링", "코칭"], "🧑‍🏫"),
        (["언어 학습"], "🗺️"),
    ]
    for keywords, icon in mapping:
        if any(k in hobby for k in keywords):
            return icon
    return "🎯"

st.title("🎨 MBTI 취미 추천")
st.write("유형별로 어울리는 취미와 여가 활동을 확인해보세요.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: {st.session_state.result_type}")

types = list(MBTI_DATA.keys())
default_idx = types.index(st.session_state.result_type) if st.session_state.result_type in types else 0
selected = st.selectbox("취미를 확인할 유형을 선택하세요", types, index=default_idx)

data = MBTI_DATA[selected]

illust_col, title_col = st.columns([1, 4])
with illust_col:
    st.markdown(
        f"<div style='font-size:100px; text-align:center;'>{MBTI_EMOJI[selected]}</div>",
        unsafe_allow_html=True,
    )
with title_col:
    st.header(f"{selected} - {data['nickname']}")
    st.caption(", ".join(data["keywords"]))

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🎯 추천 취미")
    for hobby in data["hobbies"]:
        icon = get_hobby_icon(hobby)
        st.markdown(f"- {icon} {hobby}")
with col2:
    st.subheader("✨ 성향 키워드")
    for k in data["keywords"]:
        st.markdown(f"- 🔑 {k}")

st.markdown("---")
st.subheader("🎰 오늘의 취미 추천 뽑기")

gacha_placeholder = st.empty()
gacha_placeholder.markdown(
    "<div style='font-size:90px; text-align:center;'>🎰</div>",
    unsafe_allow_html=True,
)

if st.button("뽑기 기계 돌리기 🎲"):
    pick = random.choice(data["hobbies"])
    icon = get_hobby_icon(pick)
    gacha_placeholder.markdown(
        "<div style='font-size:90px; text-align:center;'>🎉🎰🎉</div>",
        unsafe_allow_html=True,
    )
    st.balloons()
    st.success(f"{icon} 오늘의 추천 취미: **{pick}**")

st.markdown("---")
st.subheader("🔍 유형별 취미 비교")
search_letter = st.multiselect(
    "관심 있는 축 필터 (예: E, N, T, J)",
    ["E", "I", "S", "N", "T", "F", "J", "P"],
    key="hobby_filter",
)
filtered = [t for t in types if not search_letter or all(l in t for l in search_letter)]
for t in filtered:
    with st.expander(f"{MBTI_EMOJI[t]} {t} - {MBTI_DATA[t]['nickname']}"):
        for hobby in MBTI_DATA[t]["hobbies"]:
            icon = get_hobby_icon(hobby)
            st.markdown(f"- {icon} {hobby}")
