class Artist:
    def __init__(self, artist_id, name, biography, birth_date, nationality, website, contact_info):
        self.__artist_id = artist_id
        self.__name = name
        self.__biography = biography
        self.__birth_date = birth_date
        self.__nationality = nationality
        self.__website = website
        self.__contact_info = contact_info

    def setArtistId(self, artist_id):
        self.__artist_id = artist_id

    def setName(self, name):
        self.__name = name

    def setBiography(self, biography):
        self.__biography = biography
    
    def setBirthDate(self, birth_date):
        self.__birth_date = birth_date

    def setNationality(self, nationality):
        self.__nationality = nationality

    def setWebsite(self, website):
        self.__website = website

    def setContactInfo(self, contact_info):
        self.__contact_info = contact_info

    def getArtistId(self):
        return self.__artist_id
    
    def getName(self):
        return self.__name
    
    def getBiography(self):
        return self.__biography
    
    def getBirthDate(self):
        return self.__birth_date
    
    def getNationality(self):
        return self.__nationality
    
    def getWebsite(self):
        return self.__website
    
    def getContactInfo(self):
        return self.__contact_info
    
    def __str__(self):
        return (f"Artist ID : {self.__artist_id}\n"
                f"Name : {self.__name}\n"
                f"Biography : {self.__biography}\n"
                f"Birth Date : {self.__birth_date}\n"
                f"Nationality : {self.__nationality}\n"
                f"Website : {self.__website}\n"
                f"Contact Info : {self.__contact_info}" )