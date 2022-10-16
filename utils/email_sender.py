import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(receiver, sender_name, sender_email, subject_name, topic_name, effect_url):
    admin_mail = "teacharvit@gmail.com"
    # receiver = "omkar3602@gmail.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Check out this AR effect from TeachAR."
    msg['From'] = admin_mail
    msg['To'] = receiver

    # Create the body of the message (a plain-text and an HTML version).
    text = f"Hi! {sender_name}({sender_email}) has invited you to checkout this AR effect based on the topic {topic_name}. Link: {effect_url}"
    html = f"""
    <html>
    <head></head>
    <body>
        <h2>Hi!</h2>
        <br>
        <h3>
            {sender_name}({sender_email}) has invited you to checkout this AR effect based on the topic {topic_name} on TeachAR. 
        </h3>
        <p>
            Subject: {subject_name}
            <br>
            Topic: {topic_name}
            <br>
            Link: {effect_url}
        </p>
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    
    # Authentication
    s.login(admin_mail, "aoukkzesdwcsqjbh")

    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.
    s.sendmail(admin_mail, receiver, msg.as_string())
    s.quit()