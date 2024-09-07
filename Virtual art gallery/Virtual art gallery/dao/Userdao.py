from util.DBConnection import DBConnection

class Userdao:
    def __init__(self):
        super().__init__()
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def User_choice(self):
        while True:
            print("\n**********\nUser\n\n1.Insert\n2.Update\n3.Delete\n4.Select\n5.Display\n0.Exit\n**********\n")
            choice=int(input("Enter your choice : "))
            if choice == 1:
                self.insert_user()
            elif choice == 2:
                self.update_user()
            elif choice == 3:
                self.delete_user()
            elif choice == 4:
                self.select_user()
            elif choice == 5:
                self.display_user()
            elif choice == 0:
                break
            else:
                print("Invalid choice")

    def insert_user(self):
        try:
            UserID = int(input("Enter User ID : "))
            Username = input("Enter Username : ")
            Password = input("Enter Password : ")
            Email = input("Enter Email : ")
            First_Name = input("Enter First Name : ")
            Last_Name = input("Enter Last Name : ")
            Date_of_Birth = input("Enter Date of Birth : ")
            Profile_Picture = input("Enter Profile Picture : ")
            FavoriteArtworks = input("Enter Favorite Artworks (comma-separated list of ArtworkIDs) : ")
            self.cursor.execute("""insert into users values (?,?,?,?,?,?,?,?,?)""",
                                (UserID, Username, Password, Email, First_Name, Last_Name,
                                 Date_of_Birth, Profile_Picture, FavoriteArtworks))
            self.conn.commit()
            print("User inserted Successfully !!!")
            return True
        except Exception as err:
            print(f"User cannot be inserted : {err}")
            return False

    def update_user(self):
        try:
            UserID = int(input("Enter User ID : "))
            Username = input("Enter Username : ")
            Password = input("Enter Password : ")
            Email = input("Enter Email : ")
            First_Name = input("Enter First Name : ")
            Last_Name = input("Enter Last Name : ")
            Date_of_Birth = input("Enter Date of Birth : ")
            Profile_Picture = input("Enter Profile Picture : ")
            FavoriteArtworks = input("Enter Favorite Artworks (comma-separated list of ArtworkIDs) : ")
            FavoriteArtworks_list = [int(artwork_id.strip()) for artwork_id in FavoriteArtworks.split(',') if artwork_id.strip()]
            FavoriteArtworks_str = ','.join(str(artwork_id) for artwork_id in FavoriteArtworks_list)

            # Prepare the update query
            update_query = "UPDATE users SET "
            update_values = []

            # Check each field and add it to the update query if it's not empty
            if Username:
                update_query += "username=?, "
                update_values.append(Username)
            if Password:
                update_query += "password=?, "
                update_values.append(Password)
            if Email:
                update_query += "email=?, "
                update_values.append(Email)
            if First_Name:
                update_query += "firstname=?, "
                update_values.append(First_Name)
            if Last_Name:
                update_query += "lastname=?, "
                update_values.append(Last_Name)
            if Date_of_Birth:
                update_query += "date_of_birth=?, "
                update_values.append(Date_of_Birth)
            if Profile_Picture:
                update_query += "profile_picture=?, "
                update_values.append(Profile_Picture)
            if FavoriteArtworks_list:
                update_query += "favorite_artworks=?, "
                update_values.append(FavoriteArtworks_str)

            # Remove the trailing comma and space from the query
            update_query = update_query.rstrip(", ")
            update_query += " WHERE userid=?"
            update_values.append(UserID)

            # Execute the update query
            self.cursor.execute(update_query, update_values)
            self.conn.commit()
            print("User updated successfully !!!")
            return True
        except Exception as err:
            print(f"User cannot be updated : {err}")
            return False


    def delete_user(self):
        try:
            UserID = int(input("Enter User ID : "))
            self.cursor.execute("""delete from users where userid=?""", (UserID,))
            self.conn.commit()
            print("User deleted successfully !!!")
            return True
        except Exception as err:
            print(f"User cannot be deleted : {err}")
            return False

    def select_user(self):
        try:
            UserID = int(input("Enter User ID : "))
            self.cursor.execute("""select * from users where userid=?""", (UserID,))
            result = self.cursor.fetchone()
            if result:
                for i in result:
                    print(i)
            return True
        except Exception as err:
            print(f"User ID cannot be selected : {err}")
            return False
    
    def display_user(self):
        try:
            self.cursor.execute("""SELECT * FROM users""")
            result = self.cursor.fetchall()
            if result:
                for i in result:
                    print(i)
                return True
            else:
                print("User not found.")
                return False
        except Exception as err:
            print(f"Error occurred while fetching user details: {err}")
            return False
