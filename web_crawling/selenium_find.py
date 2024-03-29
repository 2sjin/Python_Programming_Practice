# 네이버 메인 화면에서 키워드 검색
# 셀레니움4 find_element 활용

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = "https://naver.com"
keyword = input("검색어를 입력하세요: ")

# 프로그램 종료 후 브라우저 유지
# (디버깅 필요)
options = Options()
options.add_experimental_option("detach", True)

# 웹드라이버 열기
driver = webdriver.Chrome()

# URL 접속 후, 페이지 정보 요청하기
driver.get(url)
time.sleep(1)

# 검색창을 찾아 키 입력(HTML 태그 클래스명)
driver.find_element(By.CLASS_NAME, "input_text").send_keys(keyword + "\r\n")

# 웹드라이버 닫기
input()
driver.quit()

"""
# 검색창을 찾아 키 입력(HTML 태그 ID)
driver.find_element(By.ID, "query").send_keys(keyword + "\r\n")

# 검색창을 찾아 키 입력(HTML 태그 이름)
driver.find_element(By.NAME, "query").send_keys(keyword + "\r\n")

# 검색창을 찾아 키 입력(CSS 셀렉터)
driver.find_element(By.CSS_SELECTOR, "[title='검색어 입력']").send_keys(keyword + "\r\n")

# 검색창을 찾아 키 입력(XPATH 복사-붙여넣기)
driver.find_element(By.XPATH, "//*[@id='query']").send_keys(keyword + "\r\n")

# 링크 클릭(링크 텍스트 일치)
driver.find_element(By.LINK_TEXT, "쇼핑LIVE").click()

# 링크 클릭(링크 텍스트 부분 일치)
driver.find_element(By.PARTIAL_LINK_TEXT, "핑L").click()
"""