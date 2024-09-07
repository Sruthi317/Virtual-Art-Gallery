class Gallery:
    def __init__(self, gallery_id, name, description, location, curator):
        self.__gallery_id = gallery_id
        self.__name = name
        self.__description = description
        self.__location = location
        self.__curator = curator

    def setGalleryId(self, gallery_id):
        self.__gallery_id = gallery_id

    def setName(self, name):
        self.__name = name

    def setDescription(self, description):
        self.__description = description
    
    def setLocation(self, location):
        self.__location = location

    def setCurator(self, curator):
        self.__curator = curator

    def getGalleryId(self):
        return self.__gallery_id
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getLocation(self):
        return self.__location
    
    def getCurator(self):
        return self.__curator
    
    def __str__(self):
        return (f"Gallery ID : {self.__gallery_id}\n"
                f"Name : {self.__name}\n"
                f"Description : {self.__description}\n"
                f"Location : {self.__location}\n"
                f"Curator : {self.__curator}" )
