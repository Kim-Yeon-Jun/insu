import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@st.experimental_singleton
def get_driver():
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

st.title("해외축구 뉴스 요약")

key_word = st.text_input("검색하고 싶은 키워드를 입력하세요!")
view_count = st.text_input("보고싶은 기사의 수를 입력하세요!", 1)

if st.button("검색 시작"):
    if not key_word:
        st.error("키워드를 입력해주세요!!")
    else:
        try:
            driver = get_driver()
            url = "https://sports.chosun.com/football/?action=worldfootball"
            driver.get(url)
            time.sleep(3)  # 페이지 로딩 대기
            st.success("크롤링 성공!")
            
            # 여기에 크롤링 로직을 추가하세요
            
        except Exception as e:
            st.error(f"크롤링 중 오류 발생: {str(e)}")
            st.error(f"오류 세부사항: {e.__class__.__name__}: {str(e)}")
        finally:
            driver.quit()
