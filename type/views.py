from django.shortcuts import render
import random
import json
from django.http import JsonResponse
import smtplib
import mysql.connector as m
def home(request):
    content = ['The sun rises in the east and sets in the west.\n', 'Learning new skills is essential for personal growth.\n', 'Exercise is a great way to improve physical health.\n', 'Traveling to new places is an exciting adventure.\n', "Kindness can make a big difference in someone's day.\n", 'Reading books is a wonderful way to gain knowledge.\n', 'A healthy diet is important for overall well-being.\n', 'Hard work and dedication can lead to great success.\n', 'Honesty is the foundation of any good relationship.\n', 'Music has the power to uplift and inspire people.\n', 'Nature is a source of beauty and inspiration.\n', 'Laughter is good for the soul and reduces stress.\n', 'Forgiveness is essential for healing and moving forward.\n', 'Communication is key to resolving conflicts and misunderstandings.\n', 'Time management is crucial for achieving goals.\n', 'Failure is not the end, but an opportunity to learn and grow.\n', 'Expressing gratitude can improve mental and emotional health.\n', 'Creativity allows us to express ourselves in unique ways.\n', 'Empathy and compassion are essential for building strong relationships.\n', 'Positive thinking can lead to positive outcomes in life.\n', 'Resilience is the ability to overcome obstacles and challenges.\n', 'Friendship is a valuable and important part of life.\n', 'Learning from mistakes is essential for personal growth.\n', 'Persistence and determination can help achieve difficult goals.\n', 'Love is a powerful force that can bring people together.\n', 'Trust is the foundation of any healthy relationship.\n', 'Patience is a virtue that can lead to great things.\n', 'Courage is necessary for facing fears and taking risks.\n', 'Teamwork and collaboration can lead to great achievements.\n', 'The beauty of diversity is in our differences and similarities.\n', 'Gratitude is the attitude that leads to happiness.\n', 'Empowering others can have a positive impact on their lives.\n', 'Kindness is contagious and can create a ripple effect.\n', 'Education is the key to unlocking opportunities in life.\n', 'Positivity and optimism can improve our outlook on life.\n', 'Passion and enthusiasm can lead to fulfilling experiences.\n', 'Creativity is the fuel that drives innovation and progress.\n', 'Integrity is essential for building trust and credibility.\n', 'Adversity can make us stronger and more resilient.\n', 'Curiosity and a desire for knowledge can lead to great discoveries.']
    word = random.choice(content) 
    return render(request,"type/index.html",{"sen":word})

def result(request):
    if request.method == "POST":
        data = json.loads(request.body)
        my_variable = data["my_variable"]
        return("")
    else:
        pass
def about(request):
    return render(request,"type/about.html")
    
def feed(request):
    return render(request,"type/feedback.html")
def send(request):
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    country = request.GET['country']
    message = request.GET['subject']
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    sender = "noreply.tetrabytes@gmail.com"
    recipient = "yt.infitips@gmail.com"
    s.login(sender, "jpigczuhtfkinxfh")
    email_body = f"""From: Typee <{sender}>
To: To Person <{recipient}>
Subject: New Feedback from {firstname} {lastname} from {country}
{message}
"""
    s.sendmail(sender, recipient, email_body)
    s.quit()
    try:
        con = m.connect(host="sql12.freesqldatabase.com",user="sql12606456",database="sql12606456",password="lhlnTEkiu9")
        #q = "create table feedback (fname varchar(45), lname varchar(45), country varchar(45), msg varchar(500));"
        q = "insert into feedback values ('{}','{}','{}','{}');".format(firstname,lastname,country,message)
        cur = con.cursor()
        cur.execute(q)
        con.commit()
        con.close()
    except:
        pass
    return render(request,"type/thankyou.html")
