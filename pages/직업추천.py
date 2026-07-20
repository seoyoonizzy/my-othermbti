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
strength_desc = {
    "ISTJ": ["계획적: 목표를 세우면 세부 일정까지 촘촘하게 짜서 차근차근 실행에 옮기는 능력이 뛰어납니다.",
             "성실함: 맡은 업무는 끝까지 책임지고 마무리하려는 태도가 강해 신뢰를 얻기 쉽습니다.",
             "신뢰감: 규칙과 원칙을 지키는 모습이 일관되어 동료와 상사 모두에게 안정감을 줍니다."],
    "ISFJ": ["배려심: 주변 사람의 필요를 세심하게 살펴 실질적인 도움을 주는 데 능숙합니다.",
             "인내심: 반복적이고 지루한 업무도 불평 없이 꾸준히 해내는 힘이 있습니다.",
             "실용성: 이론보다 실제로 효과가 있는 방법을 찾아 적용하는 현실적인 감각을 갖고 있습니다."],
    "INFJ": ["직관력: 겉으로 드러나지 않는 사람들의 감정이나 상황의 흐름을 빠르게 파악합니다.",
             "헌신: 자신이 가치 있다고 여기는 목표에는 시간과 에너지를 아끼지 않고 몰입합니다.",
             "창의성: 기존 방식과 다른 새로운 시각으로 문제를 해결하는 아이디어를 자주 냅니다."],
    "INTJ": ["장기계획: 몇 년 뒤를 내다보며 큰 그림을 그리고 그에 맞춰 전략을 세우는 데 강합니다.",
             "논리력: 복잡한 정보를 체계적으로 정리해 합리적인 결론을 도출하는 능력이 뛰어납니다.",
             "결단력: 충분한 분석 후에는 흔들림 없이 결정을 밀고 나가는 추진력이 있습니다."],
    "ISTP": ["문제해결: 예상치 못한 상황에서도 원인을 빠르게 파악하고 실질적인 해결책을 찾아냅니다.",
             "적응력: 변화하는 환경에 크게 스트레스받지 않고 유연하게 대응합니다.",
             "냉철함: 위기 상황에서도 감정에 휘둘리지 않고 객관적으로 판단합니다."],
    "ISFP": ["미적감각: 색감, 구성, 분위기 등을 감각적으로 다루는 능력이 뛰어납니다.",
             "공감력: 타인의 감정을 있는 그대로 받아들이고 자연스럽게 공감해줍니다.",
             "적응력: 정해진 틀보다는 상황에 맞게 유연하게 대처하는 것을 편하게 느낍니다."],
    "INFP": ["창의성: 자신만의 독특한 시각으로 콘텐츠나 아이디어를 만들어내는 힘이 있습니다.",
             "가치중심: 스스로 믈고 있는 신념과 가치에 따라 흔들리지 않고 행동합니다.",
             "공감: 타인의 감정과 상황에 깊이 몰입해 진심으로 이해하려 노력합니다."],
    "INTP": ["창의적사고: 기존 틀을 벗어난 독창적인 아이디어와 이론을 자주 떠올립니다.",
             "논리력: 복잡한 개념을 분석하고 인과관계를 정확히 짚어내는 데 강합니다.",
             "호기심: 새로운 지식이나 원리를 파고드는 것을 즐기며 끝까지 탐구합니다."],
    "ESTP": ["실행력: 생각한 것을 바로 행동으로 옮기는 추진력이 강합니다.",
             "적응력: 예측 불가능한 상황에서도 순간적으로 판단하고 대응하는 능력이 뛰어납니다.",
             "설득력: 상황을 읊고 재치있게 사람들을 움직이는 화술을 갖고 있습니다."],
    "ESFP": ["에너지: 주변 분위기를 밝게 만들고 활기를 불어넣는 힘이 있습니다.",
             "친화력: 처음 만나는 사람과도 금방 친해지는 사교적인 매력을 지녔습니다.",
             "적응력: 변화하는 상황에도 즐겁게 적응하며 유연하게 움직입니다."],
    "ENFP": ["아이디어: 새로운 프로젝트나 캠페인에 대한 창의적인 발상을 끊임없이 떠올립니다.",
             "친화력: 다양한 사람들과 쉽게 관계를 맺고 팀 분위기를 이끌어갑니다.",
             "동기부여: 주변 사람들에게 열정을 전달해 함께 움직이게 만드는 힘이 있습니다."],
    "ENTP": ["아이디어: 기존의 방식에 도전하는 새로운 관점을 자주 제시합니다.",
             "설득력: 논리와 재치를 섞어 상대방을 자신의 의견으로 끌어당기는 능력이 있습니다.",
             "적응력: 예상치 못한 변화에도 빠르게 전략을 수정해 대응합니다."],
    "ESTJ": ["조직력: 사람과 자원을 체계적으로 배치해 효율적으로 일이 돌아가게 만듭니다.",
             "결단력: 복잡한 상황에서도 신속하고 명확한 결정을 내립니다.",
             "책임감: 맡은 역할과 결과에 대해 끝까지 책임지려는 태도가 강합니다."],
    "ESFJ": ["친화력: 조직 안에서 사람들 사이를 원만하게 이어주는 역할을 자연스럽게 해냅니다.",
             "조직력: 행사나 프로젝트를 세심하게 계획하고 관리하는 능력이 뛰어납니다.",
             "책임감: 팀원들과의 약속과 역할을 성실하게 지키려 노력합니다."],
    "ENFJ": ["설득력: 사람들의 마음을 움직여 같은 방향으로 이끄는 힘이 있습니다.",
             "공감능력: 타인의 감정을 빠르게 읽고 그에 맞는 지원을 제공합니다.",
             "조직력: 팀의 목표를 위해 사람들의 역할을 조화롭게 배분합니다."],
    "ENTJ": ["결단력: 큰 결정을 내려야 하는 순간에도 망설임 없이 방향을 정합니다.",
             "추진력: 목표를 향해 팀 전체를 이끌고 밀고 나가는 힘이 강합니다.",
             "카리스마: 자신감 있는 태도로 사람들에게 신뢰와 영향력을 줍니다."],
}

weakness_desc = {
    "ISTJ": ["융통성 부족: 예상치 못한 변화가 생기면 기존 방식을 고집해 적응에 시간이 걸릴 수 있습니다.",
             "변화 거부: 새로운 시스템이나 프로세스 도입에 거부감을 느껴 속도가 늦어질 수 있습니다."],
    "ISFJ": ["자기희생: 타인을 돕는 데 집중하다 보니 본인의 업무나 휴식을 소홀히 할 수 있습니다.",
             "변화 스트레스: 갑작스러운 일정 변경이나 새로운 환경에 적응하는 데 부담을 느낄 수 있습니다."],
    "INFJ": ["완벽주의: 스스로 세운 기준이 높아 작은 실수에도 과도하게 스트레스를 받을 수 있습니다.",
             "번아웃 취약: 많은 것을 혼자 감당하려다 지치기 쉬워 휴식과 경계 설정이 필요합니다."],
    "INTJ": ["과도한 비판: 자신과 타인의 결과물에 엄격한 기준을 적용해 관계에서 마찰이 생길 수 있습니다.",
             "감정표현 어려움: 생각을 논리적으로 전달하는 데는 강하지만 감정을 표현하는 데는 서툴 수 있습니다."],
    "ISTP": ["감정표현 부족: 속마음을 잘 드러내지 않아 주변 사람들이 오해할 수 있습니다.",
             "장기계획 약함: 눈앞의 문제 해결에는 강하지만 먼 미래를 계획하는 데는 흥미가 떨어질 수 있습니다."],
    "ISFP": ["갈등회피: 불편한 상황을 피하려다 필요한 의견 표현을 미루는 경우가 있습니다.",
             "계획성 부족: 즉흥적으로 움직이는 것을 선호해 장기적인 일정 관리에 어려움을 겪을 수 있습니다."],
    "INFP": ["현실감 부족: 이상과 가치에 집중하다 보니 현실적인 제약을 놓칠 때가 있습니다.",
             "비판에 민감: 자신의 아이디어나 결과물에 대한 피드백을 개인적으로 받아들이기 쉽습니다."],
    "INTP": ["사회성 부족: 아이디어에 몰입하다 보면 주변과의 소통이나 협업에 소홀해질 수 있습니다.",
             "실행력 약함: 분석과 이론에 강하지만 실제 실행 단계로 넘어가는 데 시간이 걸릴 수 있습니다."],
    "ESTP": ["충동적: 순간의 판단으로 행동하다 보니 신중한 검토가 필요한 결정에서 실수할 수 있습니다.",
             "장기계획 약함: 즉흥적인 대응에 강하지만 먼 미래를 위한 계획 수립은 소홀해질 수 있습니다."],
    "ESFP": ["집중력 부족: 다양한 자극에 관심이 분산되어 한 가지 일에 오래 몰입하기 어려울 수 있습니다.",
             "계획성 약함: 즉흥적인 성향 때문에 장기적인 일정 관리나 세부 계획에서 어려움을 겪을 수 있습니다."],
    "ENFP": ["집중력 부족: 새로운 아이디어에 쉽게 흥미를 느껴 하나의 프로젝트를 끝까지 밀고가기 어려울 수 있습니다.",
             "쉽게 지침: 열정적으로 시작하지만 반복적인 업무가 이어지면 동기가 빨리 떨어질 수 있습니다."],
    "ENTP": ["끈기부족: 새로운 아이디어에 매력을 느껴 기존 프로젝트를 마무리하는 힘이 약할 수 있습니다.",
             "논쟁적: 자신의 의견을 강하게 주장하다 보니 불필요한 갈등이 생길 수 있습니다."],
    "ESTJ": ["융통성 부족: 정해진 규칙과 절차를 중시해 예외적인 상황에 대응하는 게 어려울 수 있습니다.",
             "고집: 자신의 방식이 옳다고 믿는 경향이 강해 타인의 의견을 받아들이기 어려울 때가 있습니다."],
    "ESFJ": ["비판에 민감: 타인의 평가나 피드백을 개인적으로 받아들여 상처받기 쉽습니다.",
             "타인의존: 주변의 인정과 조화를 중요하게 여겨 독립적인 결정을 내리는 데 부담을 느낄 수 있습니다."],
    "ENFJ": ["자기희생: 타인을 돕는 데 집중하다 보니 자신의 필요를 뒤로 미루는 경우가 많습니다.",
             "비판에 민감: 자신의 노력에 대한 부정적인 피드백을 크게 받아들일 수 있습니다."],
    "ENTJ": ["독선적: 목표 달성을 우선시하다 보니 타인의 의견을 충분히 듣지 않을 때가 있습니다.",
             "감정소홀: 효율과 성과에 집중하다 보면 주변 사람들의 감정을 놓칠 수 있습니다."],
}

with open("output/data.py", "r", encoding="utf-8") as f:
    content = f.read()

content += "\n\nSTRENGTH_DESC = " + repr(strength_desc) + "\n"
content += "\nWEAKNESS_DESC = " + repr(weakness_desc) + "\n"

with open("output/data.py", "w", encoding="utf-8") as f:
    f.write(content)

import py_compile
py_compile.compile("output/data.py", doraise=True)
print("data.py OK, length:", len(content))

emoji_map = {
    "ISTJ": "📋", "ISFJ": "🛡️", "INFJ": "🕯️", "INTJ": "🧠",
    "ISTP": "🔧", "ISFP": "🎨", "INFP": "🌙", "INTP": "🔬",
    "ESTP": "🏁", "ESFP": "🎉", "ENFP": "🌟", "ENTP": "💡",
    "ESTJ": "📊", "ESFJ": "🤝", "ENFJ": "🌻", "ENTJ": "👑",
}

with open("output/data.py", "r", encoding="utf-8") as f:
    content = f.read()

content += "\nMBTI_EMOJI = " + repr(emoji_map) + "\n"

with open("output/data.py", "w", encoding="utf-8") as f:
    f.write(content)

import py_compile
py_compile.compile("output/data.py", doraise=True)

career_py = r'''
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
'''

with open("output/pages/2_직업추천.py", "w", encoding="utf-8") as f:
    f.write(career_py)

py_compile.compile("output/pages/2_직업추천.py", doraise=True)
print("career page OK")
