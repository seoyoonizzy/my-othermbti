import streamlit as st
from data import MBTI_DATA

st.set_page_config(page_title="직업 추천", page_icon="💼", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

st.title("💼 MBTI 직업 추천")
st.write("유형별로 어울리는 직업과 산업 분야를 확인해보세요.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: {st.session_state.result_type}")

types = list(MBTI_DATA.keys())
default_idx = types.index(st.session_state.result_type) if st.session_state.result_type in types else 0
selected = st.selectbox("직업을 확인할 유형을 선택하세요", types, index=default_idx)

data = MBTI_DATA[selected]
st.header(f"{selected} - {data['nickname']}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("추천 직업")
    for job in data["jobs"]:
        st.markdown(f"- {job}")
with col2:
    st.subheader("업무 강점")
    for s in data["strengths"]:
        st.markdown(f"- {s}")
    st.subheader("주의할 점")
    for w in data["weaknesses"]:
        st.markdown(f"- {w}")

st.markdown("---")
st.subheader("유형별 직업 비교")
search_letter = st.multiselect("관심 있는 축 필터", ["E", "I", "S", "N", "T", "F", "J", "P"])
filtered = [t for t in types if not search_letter or all(l in t for l in search_letter)]
for t in filtered:
    with st.expander(f"{t} - {MBTI_DATA[t]['nickname']}"):
        st.write(", ".join(MBTI_DATA[t]["jobs"]))
