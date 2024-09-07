"""Artwork
ArtworkID (Primary Key)
Title
Description
CreationDate
Medium
ImageURL (or any reference to the digital representation)"""

from util.DBConnection import DBConnection

class Artworkdao:
    def __init__(self):
        super().__init__()
        self.conn=DBConnection.getConnection()
        self.cursor=self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def Artwork_choice(self):
        while True:
            print("\n**********\nArtwork\n\n1.Insert\n2.Update\n3.Delete\n4.Select\n5.Display\n0.Exit\n**********\n")
            ch=int(input("Enter your choice : "))
            if ch==1:
                self.insert_artwork()
            elif ch==2:
                self.update_artwork()
            elif ch==3:
                self.delete_artwork()
            elif ch==4:
                self.select_artwork()
            elif ch==5:
                self.display_artwork()
            elif ch==0:
                break
            else: 
                print("Invalid choice")

    def insert_artwork(self):
        try:
            self.ArtworkID = int(input('Enter Artwork ID: '))
            self.Title = input('Enter Title: ')
            self.Description = input('Enter Description: ')
            self.CreationDate = input('Enter Creation Date: ')
            self.Medium = input('Enter Medium: ')
            self.ImageURL = input('Enter Image URL: ')
            self.cursor.execute("""insert into Artwork values (?,?,?,?,?,?)""",
                                (self.ArtworkID, self.Title, self.Description, self.CreationDate, self.Medium, self.ImageURL))
            self.conn.commit()
            return True
        except Exception as err:
            print(f"Artwork cannot be added : {err}")
            return False
        
    def update_artwork(self):
        try:
            self.ArtworkID = int(input('Enter Artwork ID: '))
            self.Title = input('Enter Title: ')
            self.Description = input('Enter Description: ')
            self.CreationDate = input('Enter Creation Date: ')
            self.Medium = input('Enter Medium: ')
            self.ImageURL = input('Enter Image URL: ')
            self.cursor.execute("""update artwork set Title=?, description=?, creationdate=?, medium=?, imageurl=?
                                where artworkid=?""",
                                (self.Title, self.Description, self.CreationDate, self.Medium, self.ImageURL,self.ArtworkID))
            self.conn.commit()
            print("Artwork updated successfully !!!")
            return True
        except Exception as err:
            print(f"Artwork cannot be added : {err}")
            return False
            
    def delete_artwork(self):
        try:
            self.artworkid=int(input("Enter Artwork ID to be deleted : "))
            self.cursor.execute("delete from artwork where artworkid=?",(self.artworkid,))
            self.conn.commit()
            print("Artwork deleted success")
            return True
        except Exception as err:
            print(f"Artwork cannot be deleted : {err}")
            return False
        
    def select_artwork(self):
        try:
            self.artworkid=int(input("Enter Artwork to be selected : "))
            self.cursor.execute("select * from artwork where artworkid=?",(self.artworkid,))
            result=self.cursor.fetchone()
            if result:
                return [result]
            else:
                print("No artwork found with the given ID.")
                return []
        except Exception as err:
            print(f"No artworkid found in artwork : {err}")

    def display_artwork(self):
        try:
            self.cursor.execute("""SELECT * FROM Artwork""")
            result = self.cursor.fetchall()
            if result:
                for i in result:
                    print(i)
                return True
            else:
                print("Artwork not found.")
                return False
        except Exception as err:
            print(f"Error occurred while fetching artwork details: {err}")
            return False

