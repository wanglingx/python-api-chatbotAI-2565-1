import mysql.connector
class Connector:
    def ConnectorMysql():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="AI-Chatbot",
            auth_plugin='mysql_native_password'
        )
        print("Connection Success !")
        return mydb
