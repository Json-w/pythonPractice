from mysql import connector


class DBManager:
    host = '127.0.0.1'
    port = 3306
    user = 'root'
    password = ''
    db = 'tvShows'

    def get_con(self):
        return connector.connect(host=self.host, port=self.port, user=self.user, password=self.password,
                                 database=self.db);


if __name__ == '__main__':
    for i in range(10):
        db = DBManager().get_con()
        print('打开db链接:{}'.format(i))
        db.close
