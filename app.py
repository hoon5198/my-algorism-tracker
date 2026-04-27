# 기존 코드
import streamlit as st

st.set_page_config(page_title="알고리즘 코드 창고", layout="wide")

# --- UI 숨기기 코드 추가 ---
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
# -------------------------

st.title("💻 알고리즘 코드 기록장")
# ... 이후 코드 동일 ...

# 1. 데이터 저장 공간 확인
if "problem_list" not in st.session_state:
    st.session_state["problem_list"] = []

# --- 상단: 입력 구역 ---
st.subheader("✏️ 새로운 문제와 코드 등록")

# 플랫폼 대신 바로 제목과 난이도 입력
col1, col2 = st.columns([3, 1])
with col1:
    title = st.text_input("문제 제목 (예: 2557번 Hello World)")
with col2:
    difficulty = st.selectbox("난이도", ["하", "중", "상"])

# 핵심: 코드를 입력하는 칸 (높이를 조절할 수 있습니다)
code_content = st.text_area("소스 코드 입력", placeholder="여기에 작성한 코드를 붙여넣으세요...", height=200)

memo = st.text_area("풀이 핵심 요약 (메모)")

if st.button("기록 저장하기"):
    if title == "" or code_content == "":
        st.error("⚠️ 제목과 코드는 반드시 입력해야 합니다!")
    else:
        new_entry = {
            "title": title,
            "difficulty": difficulty,
            "code": code_content,
            "memo": memo
        }
        st.session_state["problem_list"].append(new_entry)
        st.success(f"✅ '{title}' 기록 완료!")

# --- 하단: 목록 구역 ---
st.markdown("---")
st.subheader("📚 나의 코드 저장소")

if st.session_state["problem_list"]:
    # 최신 등록순으로 보여주기 위해 리스트를 뒤집어서 출력합니다.
    for idx, item in enumerate(reversed(st.session_state["problem_list"])):
        with st.expander(f"📌 {item['title']} (난이도: {item['difficulty']})"):
            if item['memo']:
                st.write("**💡 풀이 메모:**")
                st.info(item['memo'])
            
            st.write("**📄 작성한 코드:**")
            # st.code를 사용하면 문법 강조(Syntax Highlighting)가 적용되어 가독성이 좋아집니다.
            st.code(item['code'], language='python')
            
            if st.button(f"삭제하기", key=f"del_{idx}"):
                # 실제 앱에서는 리스트 인덱스 관리가 필요하지만, 지금은 UI 확인용입니다.
                st.write("삭제 기능은 데이터베이스 연결 시 더 정확히 구현할 수 있습니다.")
else:
    st.write("아직 저장된 코드가 없습니다.")
