import streamlit as st
from data import MBTI_DATA, STRENGTH_DESC, WEAKNESS_DESC, MBTI_EMOJI

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

st.subheader("🎯 추천 직업")
job_cols = st.columns(len(data["jobs"]))
for col, job in zip(job_cols, data["jobs"]):
    with col:
        st.markdown(
            f"<div style='text-align:center; padding:10px; border-radius:10px; "
            f"background-color:#f0f2f6;'>{MBTI_EMOJI[selected]}<br><b>{job}</b></div>",
            unsafe_allow_html=True,
        )

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("💪 업무 강점")
    for desc in STRENGTH_DESC[selected]:
        st.markdown(f"- {desc}")
with col2:
    st.subheader("⚠️ 주의할 점")
    for desc in WEAKNESS_DESC[selected]:
        st.markdown(f"- {desc}")

st.markdown("---")
st.subheader("🔍 유형별 직업 비교")
search_letter = st.multiselect("관심 있는 축 필터 (예: E, N, T, J)", ["E", "I", "S", "N", "T", "F", "J", "P"])
filtered = [t for t in types if not search_letter or all(l in t for l in search_letter)]
for t in filtered:
    with st.expander(f"{MBTI_EMOJI[t]} {t} - {MBTI_DATA[t]['nickname']}"):
        st.write(", ".join(MBTI_DATA[t]["jobs"]))
