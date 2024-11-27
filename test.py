import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_driver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        # Chrome 드라이버 초기화
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        st.write("Chrome 브라우저 초기화 성공")
        return driver
    except Exception as e:
        st.write(f"Chrome 초기화 실패: {str(e)}")
        try:
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            
            # Firefox 드라이버 초기화
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service, options=firefox_options)
            st.write("Firefox 브라우저 초기화 성공")
            return driver
        except Exception as e:
            st.error(f"Firefox 초기화 실패: {str(e)}")
            return None

url = "https://sports.chosun.com/football/?action=worldfootball"

st.title("해외축구 뉴스 요약")

key_word = st.text_input("검색하고 싶은 키워드를 입력하세요!")
view_count = st.text_input("보고싶은 기사의 수를 입력하세요!", 1)

if st.button("검색 시작"):
    if not key_word:
        st.error("키워드를 입력해주세요!!")
    else:
        driver = get_driver()
        if driver:
            try:
                driver.get(url)
                time.sleep(3)  # 페이지 로딩 대기
                st.success("크롤링 성공!")
            except Exception as e:
                st.error(f"크롤링 중 오류 발생: {str(e)}")
                st.error(f"오류 세부사항: {e.__class__.__name__}: {str(e)}")
            finally:
                driver.quit()
        else:
            st.error("브라우저 드라이버를 초기화하지 못했습니다.")
