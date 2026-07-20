import streamlit as st
from data import MBTI_DATA, QUESTIONS

st.set_page_config(page_title="MBTI 웹앱", page_icon="🧠", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

st.title("🧪 MBTI 간이 테스트")
st.write("12개의 문항에 답하고 나의 성격 유형을 확인해보세요.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: **{st.session_state.result_type}**")
    st.sidebar.caption(MBTI_DATA[st.session_state.result_type]["nickname"])
st.sidebar.info("왼쪽 상단에서 관계 분석, 직업 추천, 취미 추천 페이지로 이동할 수 있습니다.")

with st.form("mbti_form"):
    scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    for idx, (q, a, b) in enumerate(QUESTIONS):
        val = st.slider(q, min_value=1, max_value=5, value=3, key=f"q_{idx}",
                         help="1: 전혀 그렇지 않다 ~ 5: 매우 그렇다")
        scores[a] += val
        scores[b] += (6 - val)
    submitted = st.form_submit_button("결과 확인하기")

if submitted:
    mbti = ""
    mbti += "E" if scores["E"] >= scores["I"] else "I"
    mbti += "S" if scores["S"] >= scores["N"] else "N"
    mbti += "T" if scores["T"] >= scores["F"] else "F"
    mbti += "J" if scores["J"] >= scores["P"] else "P"
    st.session_state.result_type = mbti

    data = MBTI_DATA[mbti]
    st.balloons()
    st.header(f"당신의 유형은 {mbti} — {data['nickname']} 입니다!")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("✨ 키워드")
        for k in data["keywords"]:
            st.markdown(f"- {k}")
        st.subheader("💪 강점")
        for s in data["strengths"]:
            st.markdown(f"- {s}")
    with col2:
        st.subheader("⚠️ 약점")
        for w in data["weaknesses"]:
            st.markdown(f"- {w}")
        st.subheader("📊 축별 점수")
        st.write(f"E {scores['E']} : I {scores['I']}")
        st.write(f"S {scores['S']} : N {scores['N']}")
        st.write(f"T {scores['T']} : F {scores['F']}")
        st.write(f"J {scores['J']} : P {scores['P']}")

    st.info("👈 왼쪽 메뉴에서 관계 분석과 직업 추천, 취미 추천 페이지로 이동해 더 자세한 정보를 확인해보세요.")

st.markdown("---")
st.subheader("📚 전체 유형 둘러보기")
cols = st.columns(4)
for i, (mtype, data) in enumerate(MBTI_DATA.items()):
    with cols[i % 4]:
        with st.expander(f"{mtype}"):
            st.caption(data["nickname"])
            st.write(", ".join(data["keywords"]))
