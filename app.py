from jinja2 import Template
# from College_data import fetch_data
# from College_data import level_count
from mailer import send_email
from date import date
import pandas as pd
import numpy as np

d=date()

date_from= d[0]
date_to=d[1]
week = d[2]
month=d[3]


df = {
    'Total Users': [6767676],
    'Mobile Users': [44423],
    'Desktop Users': [78456],
    'Mobile Verify Users': [878475],
    'Desktop verify users': [68654],
    'UG Count': [68654],
    'PG Count': [68654]
}
colleges_data=pd.DataFrame(df)

# colleges_data = fetch_data()
# level=level_count()


data = {'Totalusers':colleges_data['Total Users'].values[0],
        'MobileUsers':colleges_data['Mobile Users'].values[0],
        'DesktopUsers':colleges_data['Desktop Users'].values[0],
        'MobileVerifyUsers':int(np.int64(colleges_data['Mobile Verify Users'].values[0])),
        'Desktopverifyusers':colleges_data['Desktop verify users'].values[0],
        'ugcount':colleges_data['UG Count'].values[0],
        'pgcount':colleges_data['PG Count'].values[0],
        'month':month,
        'week_name':week,
        'date_from': date_from,
        'date_to':date_to}

with open("C:\\Users\\sm924\Desktop\\Registration report\\templates\\template2.html", "r", encoding="utf-8") as file:
    html_template = file.read()

template = Template(html_template)
html_content = template.render(data)

# Save to an HTML file
with open("C:\\Users\\sm924\Desktop\\Registration report\\templates\\output.html", "w") as file:
    file.write(html_content)
print('HTML File Updated........')

report_path = "C:\\Users\\sm924\Desktop\\Registration report\\templates\\output.html"
send_email(report_path)
print("Report generated and sent successfully!")
