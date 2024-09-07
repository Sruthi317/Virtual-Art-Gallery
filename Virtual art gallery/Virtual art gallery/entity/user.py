class User:
    def __init__(self, user_id, username, password, email, first_name, last_name, birth_date, profile_picture, favorite_artworks):
        self.__user_id = user_id
        self.__username = username
        self.__password = password
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__profile_picture = profile_picture
        self.__favorite_artworks = favorite_artworks

    def setUserId(self, user_id):
        self.__user_id = user_id

    def setUsername(self, username):
        self.__username = username

    def setPassword(self, password):
        self.__password = password
    
    def setEmail(self, email):
        self.__email = email

    def setFirstName(self, first_name):
        self.__first_name = first_name

    def setLastName(self, last_name):
        self.__last_name = last_name

    def setBirthDate(self, birth_date):
        self.__birth_date = birth_date

    def setProfilePicture(self, profile_picture):
        self.__profile_picture = profile_picture

    def setFavoriteArtworks(self, favorite_artworks):
        self.__favorite_artworks = favorite_artworks

    def getUserId(self):
        return self.__user_id
    
    def getUsername(self):
        return self.__username
    
    def getPassword(self):
        return self.__password
    
    def getEmail(self):
        return self.__email
    
    def getFirstName(self):
        return self.__first_name
    
    def getLastName(self):
        return self.__last_name
    
    def getBirthDate(self):
        return self.__birth_date
    
    def getProfilePicture(self):
        return self.__profile_picture
    
    def getFavoriteArtworks(self):
        return self.__favorite_artworks
    
    def __str__(self):
        return (f"User ID : {self.__user_id}\n"
                f"Username : {self.__username}\n"
                f"Password : {self.__password}\n"
                f"Email : {self.__email}\n"
                f"First Name : {self.__first_name}\n"
                f"Last Name : {self.__last_name}\n"
                f"Birth Date : {self.__birth_date}\n"
                f"Profile Picture : {self.__profile_picture}\n"
                f"Favorite Artworks : {self.__favorite_artworks}" )