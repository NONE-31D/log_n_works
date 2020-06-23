import smtplib, os  # smtplib: 메일 전송을 위한 패키지
from email import encoders  # 파일전송을 할 때 이미지나 문서 동영상 등의 파일을 문자열로 변환할 때 사용할 패키지
from email.mime.text import MIMEText   # 본문내용을 전송할 때 사용되는 모듈
from email.mime.multipart import MIMEMultipart   # 메시지를 보낼 때 메시지에 대한 모듈
from email.mime.base import MIMEBase     # 파일을 전송할 때 사용되는 모듈
from openpyxl import load_workbook

db_csv = load_workbook("members.xlsx", data_only=True)
db_csv = db_csv['members']

domains = set()

# csv에서 이메일만 추출
for email in list(db_csv.columns)[3]:
    d = email.value.split('@')
    domains.add(d[1])

print(domains)