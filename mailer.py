import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(report_path):
    sender_email = "sumit.mishra@careers360.com"
    receiver_email = "sumitmishra0730@gmail.com"
    password = "jbmq mgqy wvzj xipi"

    # Email Setup
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Weekly Registration Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Email Body
    text = "Please find attached the weekly registration report."
    html = f"""
    <html>
        <body>
            <p>Dear Stakeholder,</p>
            <p>Please find attached the weekly registration report.</p>
            <p>Click <a href="file://{os.path.abspath(report_path)}">here</a> to view the report.</p>
        </body>
    </html>
    """
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html, "html"))

    # Send Email
    with open(report_path, "r") as file:
        attachment = MIMEText(file.read(), "html")
        attachment.add_header(
            "Content-Disposition", f"attachment; filename= {report_path}",
        )
        msg.attach(attachment)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())