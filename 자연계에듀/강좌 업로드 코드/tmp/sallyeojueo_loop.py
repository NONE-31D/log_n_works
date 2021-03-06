from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

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

# 상/하/1/2/확
# [761, 766, 800, 882, 906]

cid = [808]

flag = 0

for lecture_id in cid:
    #입력할 과목의 강좌 관리 페이지
    #lecture_id = 761
    url_lecture = "http://jayeongye.com/admin/course/edit.html?mode=view&id="+str(lecture_id) 

    driver.get(url_lecture)

    # 강좌 제목 리스트로 따오기
    # 강좌 제목 name : lectureTitles
    lectures_title = driver.find_elements_by_name('lectureTitles')
    titles = []
    for title in lectures_title:
        #print(title.get_attribute("value"))
        titles.append(title.get_attribute("value"))
        

    #강좌 영상 리스트로 따오기
    # 강좌 영상 제목 name : movies

    lectures_movies = driver.find_elements_by_name('movies')
    movies = []
    for movie in lectures_movies:
        #print(movie.get_attribute("value"))
        movies.append(movie.get_attribute("value"))



    #############여기부터 다시 입력 강좌 페이지로 이동#############
    # 하/1/2 913
    # 상/하/1/2 914
    # 상/하/1/2/확 915
    lecture_id = 917
    url_lecture = "http://jayeongye.com/admin/course/edit.html?mode=view&id="+str(lecture_id) 
    driver.get(url_lecture)

    # 근데 맨 처음의 경우 넣는 인덱스가 -4임 나도 모르겠어요 왜그래
    
    i = 1

    for idx, t in enumerate(titles):
        # 상황에 따라 수정하기 - 몇번째 강의부터 넣고싶은지
        if idx < 1:
            continue

        curr_title = t

        if "문제" in t:
            continue

        curr_title = "%02d"%(i) + t[2:]
        i += 1
        curr_movie = movies[idx]
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


