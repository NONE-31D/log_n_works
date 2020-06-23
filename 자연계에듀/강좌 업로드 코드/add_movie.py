
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

import os

path = "C:\\Users\\user\\Desktop\\신유림\\chromedriver.exe"
driver = webdriver.Chrome(path)


# 어드민페이지 메인
url_admin = "http://jayeongye.com/admin/"
driver.get(url_admin)

# 아이디 박스랑 pw 박스 
id_box = driver.find_element_by_name('loginId')
id_box.send_keys("admin")
pw_box = driver.find_element_by_name('password')
pw_box.send_keys("eton!1290")
pw_box.send_keys(Keys.RETURN)


flag = 1


#웹하드에서 영상 있는 디렉토리 주소 넣기
dir_path = "Y:\\자연계에듀\\과학과\\구본철\\20\\하이탑 물리2\\200600"
titles = os.listdir(dir_path)


# 강좌 번호
lecture_id = 838
url_lecture = "http://jayeongye.com/admin/course/edit.html?mode=view&id="+str(lecture_id) 
driver.get(url_lecture)

for idx, t in enumerate(titles):
    # 상황에 따라 수정하기 - 몇번째 강의부터 넣고싶은지
    if idx < 0:
        continue

    curr_title = t.rstrip(".mp4")
    curr_movie = "%d_%02d"%(lecture_id, idx+70)
    images = driver.find_elements_by_tag_name('img')

    # 강좌 더하기
    if flag == 0:
        add_button = images[-3]
        flag += 1
    else:
        add_button = images[-4]
    add_button.click()

    # 강좌 제목 입력
    new_title = driver.find_elements_by_name('lectureTitles')
    new_title[-1].send_keys(curr_title)


    # 다시 태그 리로드
    images = driver.find_elements_by_tag_name('img')

    video_button = images[-5]
    video_button.click()


    handles = driver.window_handles
    size = len(handles)

    #[0] : 원래 윈도우
    #[1] : 팝업 윈도우

    driver.switch_to.window(handles[1])

    # 팝업창에서 타이틀 넣기 | 인덱스는 무조건 2
    pop_title = driver.find_element_by_name('title')
    pop_title.send_keys(curr_movie)
    pop_title.send_keys(Keys.RETURN)

    tag_a = driver.find_elements_by_tag_name('a')
    tag_a[2].click()

    driver.switch_to.window(handles[0])

    if idx%15 == 0:
        if (idx == len(titles)-1):
            break
        mod_button = images[-2]
        mod_button.click()

        Alert(driver).accept()



# 강좌 최종 수정하기 - 버튼 인덱스 -2
#driver.switch_to.window(handles[0])
mod_button = images[-2]
mod_button.click()

Alert(driver).accept()


