import mysql.connector
import pandas as pd

def fetch_data():
    mydb = mysql.connector.connect(
    host="stagingdb2.mycareers360.com",
    user="root",
    password="hjasgdjaHPOHO32DE8jfdh"
    )
    print('connection stablished')
    cursor=mydb.cursor()
    cursor.execute('use django360')
    print('django database selected')
    
    query= "SELECT SUM(CASE WHEN current_education_level IN (11, 12) THEN 1 ELSE 0 END) AS UG_count, SUM(CASE WHEN current_education_level IN (13, 14) THEN 1 ELSE 0 END) AS PG_count,COUNT(uid) as user_id,SUM(CASE WHEN device_type='mobile' THEN 1 ELSE 0 END) AS mobile_count,SUM(CASE WHEN device_type='web' THEN 1 ELSE 0 END) AS desktop_count,SUM(CASE WHEN mobile_verify=1 THEN 1 ELSE 0 END) AS mobile_verify,SUM(CASE WHEN email_verify=1 THEN 1 ELSE 0 END) AS email_verify  FROM users where (FROM_UNIXTIME(created) BETWEEN '2024-12-23' and '2024-12-29 ') and source_url  like '%www.careers360.com/%' and (source_url like '%/colleges/%' or source_url like '%/university/%') and source_url not like '%/course/%' and source_url not like '%-fctp%' and source_url  not like '%/courses%' and source_url not like '%/admission%' AND source_url NOT like '%/facilities%' and source_url  NOT like '%/cut%' and source_url  NOT like '%/all-questions%' and source_url  NOT like '%/placement%' and source_url  NOT like '%/reviews%' and source_url  NOT like '%/alumni%' and source_url  NOT like '%/affiliated-colleges%' "

    cursor.execute(query)
    r= cursor.fetchall()
    df=pd.DataFrame(r)
    df.columns=['UG Count','PG Count','Total Users','Mobile Users','Desktop Users','Mobile Verify Users','Desktop verify users']
    print('completed')
    return df

