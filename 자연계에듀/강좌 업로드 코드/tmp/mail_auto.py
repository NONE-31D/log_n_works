import smtplib, os  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from openpyxl import load_workbook


googleid = "anderer.syl@gmail.com"
pw = "cpfm-dlvmf152"


db_csv = load_workbook("members.xlsx", data_only=True)
db_csv = db_csv['members']

recv_email = []

# # csv에서 이메일만 추출
# for email in list(db_csv.columns)[3]:
#     recv_email.append(email.value)

# 테스트용 이메일 목록
for i in range(10):
    recv_email.append("anderer.syl+%02d@gmail.com"%(i))

# smtp 메일 서버 접속
smtp = smtplib.SMTP('smtp.gmail.com', 587)   # 587: 서버의 포트번호
smtp.ehlo()
smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
smtp.login(googleid, pw)

# 메일 형식 작성
mail = MIMEMultipart()
mail['Subject'] = "제목입니다 테스트"

body = """

<!-- https://2-jissun.tistory.com/2 깃 명령어 확인-->


<html>
    <head>
        <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR|Oxanium:400,600&display=swap" rel="stylesheet">
        <link href="index.css" rel="stylesheet" type="text/css" />
        <link href="side.css" rel="stylesheet" type="text/css" />
        <link href="main.css" rel="stylesheet" type="text/css" />
        
    </head>
    <header>
        <div id="outer">
            <img src="img/logo.png" width="40px" height="40px"/>
            <h2>NONE-31D</h2>
        </div>
        <nav id="top_menu">
          <span class="menu"><a href="index.html">MAIN</a>
          </span><span class="menu"><a>PROJECT</a>
          </span><span class="menu"><a>BLOG</a>
          </span><span class="menu"><a>REPO</a></span>
        </nav>
    </header>
    <body>
        <div id="upper_main">
            <img src="img/upper_logo_대지 1.png"/>
        </div>
        <div id="bottom">
            <div id="side">
                <div class="curr_menu">
                    MAIN
                    <div class="sub_menu">
                        <ul>
                            <li>Profile</li>
                            <li><a href="main/thingstodo.html">Things to do</a></li>
                        </ul>
                    </div>
                </div>
                
            </div>
            <div id="main">
                <div id="subject">
                    INDEX
                </div>
                <div id="content">
                    <ul>
                        대충 인덱스 화면입니다
                    </ul>
                </div>
            </div>
        </div>
        
    </body>
</html>

"""

#ctxt = MIMEText('SMTP로 메일 보내기\n 본문 메시지입니다.')
ctxt =MIMEText(body, 'HTML') 
mail.attach(ctxt)

for email in recv_email:
    mail['To'] = email
    smtp.sendmail(googleid, email, mail.as_string())
    print("Successfully sended to %s>>>>>>>"%(email))