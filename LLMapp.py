import streamlit as st
import openai

# Streamlit 앱 제목
st.title('GPT-4 Chat Completion 앱')

# GPT API 키 입력
api_key = st.secrets["api_key"]

if api_key:
    # OpenAI API 키 설정
    openai.api_key = st.secrets["api_key"]

    # 사용자 입력
    user_input = st.text_area('당신의 질문을 입력하세요:')

    if st.button('응답 생성'):
        if user_input:
            try:
                # GPT-4 Chat Completion 요청
                response = openai.ChatCompletion.create(
                    model='gpt-4o',  # GPT-4 모델 사용
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.subheader('GPT-4 응답')
                st.write(response.choices[0].message['content'].strip())
            except Exception as e:
                st.error(f"오류가 발생했습니다: {e}")
        else:
            st.warning('먼저 질문을 입력해주세요.')
else:
    st.warning('먼저 OpenAI API 키를 입력해주세요.')
