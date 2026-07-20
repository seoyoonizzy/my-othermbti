import random
import streamlit as st
from data import MBTI_DATA

st.set_page_config(page_title="관계 분석", page_icon="💞", layout="wide")

if "result_type" not in st.session_state:
    st.session_state.result_type = None

st.title("💞 MBTI 관계 분석")
st.write("나와 상대방의 유형을 선택하면 궁합과 관계 팁을 알려드립니다.")

if st.session_state.result_type:
    st.sidebar.success(f"내 유형: {st.session_state.result_type}")

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
        level = "매우 좋음"
        msg = "서로의 강점이 보완되는 이상적인 궁합입니다."
        score = random.randint(85, 98)
    elif other_type in my_data["compat_worst"]:
        level = "노력 필요"
        msg = "가치관의 차이가 있을 수 있어 서로 이해하려는 노력이 중요합니다."
        score = random.randint(40, 60)
    else:
        level = "보통"
        msg = "무난하게 잘 지낼 수 있는 관계입니다."
        score = random.randint(65, 84)

    st.subheader(f"{my_type} + {other_type}")
    st.metric("궁합 점수", f"{score}점")
    st.write(f"{level} - {msg}")
    st.progress(score / 100)

    st.subheader("관계 팁")
    if "E" in my_type and "I" in other_type:
        st.markdown("- 서로의 에너지 충전 방식을 존중해주세요.")
    if "T" in my_type and "F" in other_type:
        st.markdown("- 감정적 배려와 논리적 설명 사이의 균형을 맞춰보세요.")
    if "J" in my_type and "P" in other_type:
        st.markdown("- 계획성과 즉흥성의 차이를 다양성으로 받아들여보세요.")
    st.markdown("- 정기적으로 서로의 생각을 솔직하게 공유하는 시간을 가지세요.")

st.markdown("---")
st.subheader("나와 잘 맞는 유형 한눈에 보기")
st.write(f"{my_type}와 가장 잘 맞는 유형: " + ", ".join(MBTI_DATA[my_type]["compat_best"]))
st.write(f"{my_type}와 노력이 필요한 유형: " + ", ".join(MBTI_DATA[my_type]["compat_worst"]))
