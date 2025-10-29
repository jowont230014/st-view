import streamlit as st

st.title("퀴즈 만들어보기")

password1 = "도전"
answer1 = ["python", "파이썬"]

quiz1_password = st.text_input("퀴즈를 풀고 싶다면, [도전]이라고 적어주세요", key="quiz1_password")

if quiz1_password == password1:
    quiz1 = st.text_input("Streamlit을 구성하는 언어는 무엇일까요?")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1.lower() in answer1:
            st.balloons()
            st.success("정답입니다! 🎉")
            st.write("Streamlit은 파이썬으로 이루어져 있어 ╰(*°▽°*)╯")
        else:
            st.warning("정답이 아니야. 다시 생각해봐!")
    if st.button("힌트 보기", key="check_hint_button1"):
        st.write("p로 시작하는 언어야 😉")

elif quiz1_password != "" and quiz1_password != password1:
    st.error("비밀번호가 틀렸어!")
