import pyodbc

class DBConnection:
    con = None

    @staticmethod
    def getConnection():
        try:
            if DBConnection.con is None or DBConnection.con.closed:  
                DBConnection.con = pyodbc.connect(
                    'Driver={SQL Server};'
                    'Server=HP\SQLEXPRESS;'
                    'Database=VirtualArtGallery;'
                )
        except pyodbc.Error as err:
            raise err  
        return DBConnection.con
