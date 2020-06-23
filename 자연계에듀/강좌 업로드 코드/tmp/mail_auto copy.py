import smtplib, os  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from openpyxl import load_workbook


googleid = "foo-bar@email.com"
pw = "foo"


db_csv = load_workbook("members.xlsx", data_only=True)
db_csv = db_csv['members']

recv_email = []

# # csv에서 이메일만 추출
# for email in list(db_csv.columns)[3]:
#     recv_email.append(email.value)

# 테스트용 이메일 목록
for i in range(10):
    recv_email.append("test@email.com")

# smtp 메일 서버 접속
smtp = smtplib.SMTP('smtp.gmail.com', 587)   # 587: 서버의 포트번호
smtp.ehlo()
smtp.starttls()   # tls방식으로 접속, 그 포트번호가 587
smtp.login(googleid, pw)

# 메일 형식 작성
mail = MIMEMultipart()
mail['Subject'] = "제목입니다 테스트"



ctxt = MIMEText('SMTP로 메일 보내기\n 본문 메시지입니다.')
mail.attach(ctxt)

for email in recv_email:
    mail['To'] = email
    smtp.sendmail(googleid, email, mail.as_string())
    print("Successfully sended to %s>>>>>>>"%(email))