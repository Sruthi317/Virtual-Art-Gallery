from util.DBConnection import DBConnection

class Artistdao:
    def __init__(self):
        super().__init__()
        self.conn=DBConnection.getConnection()
        self.cursor=self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def Artist_choice(self):
        while True:
            print("\n**********\nArtist\n\n1.Insert\n2.Update\n3.Delete\n4.Select\n5.Display\n0.Exit\n**********\n")
            choice=int(input("Enter your choice : "))
            if choice==1:
                self.insert_artist()
            elif choice==2:
                self.update_artist()
            elif choice==3:
                self.delete_artist()
            elif choice==4:
                self.select_artist()
            elif choice==5:
                self.display_artist()
            elif choice==0:
                break
            else:
                print("Invalid choice")
    
    def insert_artist(self):
        """Artist
            ArtistID (Primary Key)
            Name
            Biography
            BirthDate
            Nationality
            Website
            Contact Information"""
        try:
            Artistid=int(input("Enter Artist ID : "))
            Name = input("Enter Artist name : ")
            Biography=input("Enter Artist biography : ")
            Birthdate=input("Enter Artist birthdate : ")
            Nationality=input("Enter artist nationality : ")
            Website=input("Enter Artist website : ")
            Contact_info=input("Enter Artist contact information : ")
            self.cursor.execute("""insert into artist values (?,?,?,?,?,?,?)""",
                                (Artistid,Name,Biography,Birthdate,Nationality,Website,Contact_info))
            self.conn.commit()
            print("Artist inserted Successfully !!!")
            return True
        
        except Exception as err:
            print(f"Artist cannot be inserted : {err}")
            return False
    
    def update_artist(self):
        try:
            Artistid=int(input("Enter Artist ID : "))
            Name = input("Enter Artist name : ")
            Biography=input("Enter Artist biography : ")
            Birthdate=input("Enter Artist birthdate : ")
            Nationality=input("Enter artist nationality : ")
            Website=input("Enter Artist website : ")
            Contact_info=input("Enter Artist contact information : ")
            self.cursor.execute("""Update artist set name=?, biography=?,birthdate=?, nationality=?, website=?, contact_information=? where artistid=?""",
                                (Name,Biography,Birthdate,Nationality,Website,Contact_info,Artistid))
            self.conn.commit()
            print("Artist updated successfully !!!")
            return True
        except Exception as err:
            print(f"Artist cannot be updated : {err}")
            return False
        
    def delete_artist(self):
        try:
            Artistid=int(input("Enter artist id : "))
            self.cursor.execute("""delete from artist where artistid=?""",(Artistid))
            self.conn.commit()
            print("Artist deleted successfully !!!")
            return True
        except Exception as err:
            print(f"Artist cannot be deleted : {err}")
            return False
        
    def select_artist(self):
        try:
            ArtistID=int(input("Enter Artist Id : "))
            self.cursor.execute("""select * from artist where artistid=?""",(ArtistID))
            result=self.cursor.fetchone()
            if result:
                for i in result:
                    print(i)
            return True
        except Exception as err:
            print(f"Artist ID cannot be selected : {err}")
            return False

    def display_artist(self):
        try:
            self.cursor.execute("""SELECT * FROM Artist""")
            result = self.cursor.fetchall()
            if result:
                for i in result:
                    print(i)
                return True
            else:
                print("Artist not found.")
                return False
        except Exception as err:
            print(f"Error occurred while fetching artist details: {err}")
            return False

