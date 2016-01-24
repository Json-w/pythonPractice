import requests
from mysqlPrcatice import DBManager

p = requests.get('https://pic4.zhimg.com/953bf0a87f045858dd8c9cb9cef0883b_b.jpg')
with open('/home/jason/python/pic.jpg', 'wb') as f:
    f.write(p.content)

if __name__ == '__main__':
    db = DBManager()
    con = db.get_con()
    cur = con.cursor()
    cur.execute(
            'insert into `user` (username,password,chooseTvShowId,activitiesId,follwerId) values("jason","123",1,1,1)')

    cur.close()
    con.commit()
    con.close()

# p = requests.get('https://pic4.zhimg.com/953bf0a87f045858dd8c9cb9cef0883b_b.jpg')
# with open('/home/jason/python/pic.jpg', 'wb') as f:
#     f.write(p.content)

# 超时
try:
    requests.get('http://www.baidu.com', timeout=0.01)
except requests.exceptions.ConnectTimeout as timeOutErr:
    print('timeout {0}'.format(timeOutErr))

