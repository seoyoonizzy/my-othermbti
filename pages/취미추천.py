import random
import streamlit as st
from data import MBTI_DATA

st.set_page_config(page_title="취미 추천", page_icon="🎨", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

st.title("🎨 MBTI 취미 추천")
st.write("유형별로 어울리는 취미와 여가 활동을 확인해보세요.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: {st.session_state.result_type}")

types = list(MBTI_DATA.keys())
default_idx = types.index(st.session_state.result_type) if st.session_state.result_type in types else 0
selected = st.selectbox("취미를 확인할 유형을 선택하세요", types, index=default_idx)

data = MBTI_DATA[selected]
st.header(f"{selected} - {data['nickname']}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("추천 취미")
    for hobby in data["hobbies"]:
        st.markdown(f"- {hobby}")
with col2:
    st.subheader("성향 키워드")
    for k in data["keywords"]:
        st.markdown(f"- {k}")

st.markdown("---")
st.subheader("오늘의 취미 추천 뽑기")
if st.button("랜덤 취미 뽑기"):
    pick = random.choice(data["hobbies"])
    st.success(f"오늘의 추천 취미: {pick}")

st.markdown("---")
st.subheader("유형별 취미 비교")
search_letter = st.multiselect("관심 있는 축 필터", ["E", "I", "S", "N", "T", "F", "J", "P"], key="hobby_filter")
filtered = [t for t in types if not search_letter or all(l in t for l in search_letter)]
for t in filtered:
    with st.expander(f"{t} - {MBTI_DATA[t]['nickname']}"):
        st.write(", ".join(MBTI_DATA[t]["hobbies"]))
