import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='password', db='hotdeal', charset='utf8')
# 커서 가져오기
cursor = db.cursor()
with db.cursor() as cursor:
    # Create a new record
    sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

# connection is not autocommit by default. So you must commit to save
# your changes.
db.commit()

sql = '''
SELECT * FROM post
'''
cursor.execute(sql)
result = cursor.fetchall()
for value in result:
    print(value)
db.close()
