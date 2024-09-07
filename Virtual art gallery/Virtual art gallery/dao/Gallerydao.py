from util.DBConnection import DBConnection

class Gallerydao:
    def __init__(self):
        super().__init__()
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def Gallery_choice(self):
        while True:
            print("\n**********\nGallery\n\n1.Insert\n2.Update\n3.Delete\n4.Select\n5.Display\n0.Exit\n**********\n")
            choice=int(input("Enter your choice : "))
            if choice == 1:
                self.insert_gallery()
            elif choice == 2:
                self.update_gallery()
            elif choice == 3:
                self.delete_gallery()
            elif choice == 4:
                self.select_gallery()
            elif choice == 5:
                self.display_gallery()
            elif choice == 0:
                break
            else:
                print("Invalid choice")

    def insert_gallery(self):
        try:
            GalleryID = int(input("Enter Gallery ID : "))
            Name = input("Enter Name : ")
            Description = input("Enter Description : ")
            Location = input("Enter Location : ")
            Curator = int(input("Enter Curator (ArtistID) : "))
            OpeningHours = input("Enter Opening Hours : ")
            self.cursor.execute("""insert into gallery values (?,?,?,?,?,?)""",
                                (GalleryID, Name, Description, Location, Curator, OpeningHours))
            self.conn.commit()
            print("Gallery inserted Successfully !!!")
            return True
        except Exception as err:
            print(f"Gallery cannot be inserted : {err}")
            return False

    def update_gallery(self):
        try:
            GalleryID = int(input("Enter Gallery ID : "))
            Name = input("Enter Name : ")
            Description = input("Enter Description : ")
            Location = input("Enter Location : ")
            Curator = int(input("Enter Curator (ArtistID) : "))
            OpeningHours = input("Enter Opening Hours : ")

            # Prepare the update query
            update_query = "UPDATE gallery SET "
            update_values = []

            # Check each field and add it to the update query if it's not empty
            if Name:
                update_query += "name=?, "
                update_values.append(Name)
            if Description:
                update_query += "description=?, "
                update_values.append(Description)
            if Location:
                update_query += "location=?, "
                update_values.append(Location)
            if Curator:
                update_query += "curator=?, "
                update_values.append(Curator)
            if OpeningHours:
                update_query += "openinghours=?, "
                update_values.append(OpeningHours)

            # Remove the trailing comma and space from the query
            update_query = update_query.rstrip(", ")
            update_query += " WHERE galleryid=?"
            update_values.append(GalleryID)

            # Execute the update query
            self.cursor.execute(update_query, update_values)
            self.conn.commit()
            print("Gallery updated successfully !!!")
            return True
        except Exception as err:
            print(f"Gallery cannot be updated : {err}")
            return False


    def delete_gallery(self):
        try:
            GalleryID = int(input("Enter Gallery ID : "))
            self.cursor.execute("""delete from gallery where galleryid=?""", (GalleryID,))
            self.conn.commit()
            print("Gallery deleted successfully !!!")
            return True
        except Exception as err:
            print(f"Gallery cannot be deleted : {err}")
            return False

    def select_gallery(self):
        try:
            GalleryID = int(input("Enter Gallery ID : "))
            self.cursor.execute("""select * from gallery where galleryid=?""", (GalleryID,))
            result = self.cursor.fetchone()
            if result:
                for i in result:
                    print(i)
            return True
        except Exception as err:
            print(f"Gallery ID cannot be selected : {err}")
            return False
        
    def display_gallery(self):
        try:
            self.cursor.execute("""SELECT * FROM Gallery""")
            result = self.cursor.fetchall()
            if result:
                for i in result:
                    print(i)
                return True
            else:
                print("Gallery not found.")
                return False
        except Exception as err:
            print(f"Error occurred while fetching gallery details: {err}")
            return False
