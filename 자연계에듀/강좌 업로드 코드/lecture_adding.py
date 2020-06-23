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


# 대충 로직
# 1. 하이탑 과목을 우선 리스트에 갖다 넣기 
# 2. 내가 업데이트 해야하는 과목 페이지의 과목명 가져와서 리스트[0]이랑 비교
# 동일할 경우 이후부터 강의 추가


# 추가된 과목 코드
# 물리 : 838 화학 836 생명 837
# 블랙라벨 수2 : 882 / 26
# 화학 스타트 : 48
# 물리 스타트 : 46
# 하이탑 중1 778 중2 801 중3 866
cid_from = [836]



# 추가할 과목 타이틀 뜯어오기
for lecture_id in cid_from:
    #입력할 과목의 강좌 관리 페이지
    url_lecture = "http://jayeongye.com/admin/course/edit.html?mode=view&id="+str(lecture_id) 
    driver.get(url_lecture)

    # 강좌 제목 리스트로 따오기
    # 강좌 제목 name : lectureTitles
    lectures_title = driver.find_elements_by_name('lectureTitles')
    titles = []
    for title in lectures_title:
        titles.append(title.get_attribute("value"))

    #강좌 영상 리스트로 따오기
    # 강좌 영상 제목 name : movies
    
    lectures_movies = driver.find_elements_by_name('movies')
    movies = []
    for movie in lectures_movies:
        movies.append(movie.get_attribute("value"))


    # 마지막 강좌 코드
    start = 62

    # 업데이트를 해야 하는 강의 코드들
    #블랙라벨 수2 : 884, 886, 912, 913, 914, 915
    # 하이탑 2015
    # 물리2 : 857, 858, 843, 846, 848, 852, 862, 863, 865
    # 화학2 : 859, 860, 840, 844, 849, 853, 862, 863, 864, 865
    # 생물2 : 857, 859, 841, 850, 854, 862, 864, 865
    # 지구과학2 : 858, 860, 861, 842, 847, 851, 855, 863, 864, 865
    # 하이탑 123 : 874
    # 하이탑 23 : 872
    
    cid_toUpadate = [ 859, 860, 840, 844, 849, 853, 862, 863, 864, 865 ]

    for cid in cid_toUpadate:
        url_lecture = "http://jayeongye.com/admin/course/edit.html?mode=view&id="+str(cid) 
        driver.get(url_lecture)

        # tbody 뜯어와서 그 안에 있는 제목부터 비교. 
        # id: lecture_table
        #lec_table = driver.find_elements_by_xpath("//table[@id='lecture_table']/tbody/tr/td/table/tbody/tr/td")
        lec_table = driver.find_elements_by_xpath("//table[@id='lecture_table']//table")

        #마지막으로 입력된 강의가 뭔지
        start_t = titles[start]

        for i, lec in enumerate(lec_table):
            title = lec.find_element_by_xpath(".//input[@name='lectureTitles']")
            title = title.get_attribute("value")
            m_id = lec.find_element_by_xpath(".//input[@name='movies']")
            m_id = m_id.get_attribute("value")
            
            
            # 마지막으로 입력한 강의랑 같으면 for문으로 새로운 강의 입력 ㄱㄱ
            if title == start_t:
                add_button = lec.find_element_by_xpath(".//img[@src='../images/add_bt.gif']")
                for _ in range(len(titles) - start - 1):
                #for _ in range(1):
                    # 추가 버튼 및 클릭
                    add_button.click()
                break

        # 인풋 값 비어있는 애들만 해당 td나 table 받아와야함 
        new_lec =  driver.find_elements_by_xpath("//table[@id='lecture_table']//table")
        new_lec = new_lec[i+1 : i+len(titles)- start]

        for i, lec in enumerate(new_lec):
            # if i==1: break
            t = lec.find_element_by_xpath(".//input[@name='lectureTitles']")
            t.send_keys(titles[start+i+1])
            
            add_vid = lec.find_element_by_xpath(".//img[@src='../images/movie_search_bt.gif']")
            add_vid.click()

            handles = driver.window_handles
            size = len(handles)

            #[0] : 원래 윈도우
            #[1] : 팝업 윈도우

            driver.switch_to.window(handles[1])

            pop_title = driver.find_element_by_name('title')
            pop_title.send_keys(movies[start+i+1])
            pop_title.send_keys(Keys.RETURN)

            tag_a = driver.find_elements_by_tag_name('a')
            tag_a[2].click()

            driver.switch_to.window(handles[0])

        submit = driver.find_element_by_xpath(".//img[@src='../images/chair_md_bt.gif']")
        submit.click()
        Alert(driver).accept()



            
    pass