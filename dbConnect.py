import psycopg2

class DataBaseBean:

    def __init__(self):
        try:
            self.postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 5, user="postgre", password="postgre", host="127.0.0.1",port="5432",database="postgres")
        except (Exception, psycopg2.DatabaseError) as error:
            print("Ошибка при подключении к бд", error)
        pass

    def query(self, query, params):
        try:
            connection = self.postgreSQL_pool.getconn()
            cursor = connection.cursor()
            cursor.execute(query, params)
            connection.commit()
            return cursor.rowcount

        except (Exception, psycopg2.DatabaseError) as error:    
            print("Ошибка при исполнении запроса", error)
        finally:
            if connection:
                cursor.close()
                self.postgreSQL_pool.putconn(connection)
     
    def __del__(self):
        print("Закрытие соединений...")
        self.postgreSQL_pool.closeall


'''       
    # Use getconn() to Get Connection from connection pool
    ps_connection = postgreSQL_pool.getconn()

    if (ps_connection):
        print("successfully recived connection from connection pool ")
        ps_cursor = ps_connection.cursor()
        ps_cursor.execute("select * from report")
        mobile_records = ps_cursor.fetchall()

        print("Displaying rows from mobile table")
        for row in mobile_records:
            print(row)

        ps_cursor.close()

        # Use this method to release the connection object and send back to connection pool
        postgreSQL_pool.putconn(ps_connection)
        print("Put away a PostgreSQL connection")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # closing database connection.
    # use closeall() method to close all the active connection if you want to turn of the application
    if postgreSQL_pool:
        postgreSQL_pool.closeall
    print("PostgreSQL connection pool is closed")
'''