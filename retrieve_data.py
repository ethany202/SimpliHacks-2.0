import mysql.connector

class RetrieveData():
    def __init__(self):
        self.host = 'jtb9ia3h1pgevwb1.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
        self.username = 'fwchtxhm4yyl2zm8'
        self.password = 'hotcpncj2aymful3'
        self.database = 'i6od8rz9wvzh7zwz'
        self.connection=None

    #initiate connection between python and MySQL
    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.host, database=self.database, user=self.username, password=self.password)
            if self.connection.is_connected():
                return self.connection
        except Exception as e:
            print("Error while connecting to MySQL database", e)
        return None
    


    # close connection to MySQL database
    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()

    # check if muscle group exists and the stretches available
    def check_stretches(self, muscle_group):
        try:
            select_stmt = "SELECT stretch_desc FROM stretches WHERE group_name IN ('" +str(muscle_group)+"')"
            cursor = self.connection.cursor()
            cursor.execute(select_stmt)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print("Error while retrieving user info", e)
        return []

    # determine which muscles are present in certain muscle group
    def check_muscles(self, muscle_group):
        try:
            select_stmt = "SELECT muscle FROM muscle_groups WHERE group_name IN ('" +str(muscle_group)+"')"
            print(select_stmt)
            cursor = self.connection.cursor()
            cursor.execute(select_stmt)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print("Error while retrieving user info", e)
        return []