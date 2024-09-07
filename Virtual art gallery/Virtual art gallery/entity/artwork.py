"""Artwork
ArtworkID (Primary Key)
Title
Description
CreationDate
Medium
ImageURL (or any reference to the digital representation"""

class Artwork:
    def __init__(self):
        self.__artworkid=None
        self.__title=None
        self.__description=None
        self.__creationdate=None
        self.__medium=None
        self.__imageurl=None

    def __init__(self,artworkid,title,description,creationdate,medium,imageurl):
        self.__artworkid=artworkid
        self.__title=title
        self.__description=description
        self.__creationdate=creationdate
        self.__medium=medium
        self.__imageurl=imageurl

    def setArtworkId(self,artworkid):
        self.__artworkid=artworkid

    def setTitle(self,title):
        self.__title=title

    def setDescription(self,description):
        self.__description=description
    
    def setCreationDate(self,creationdate):
        self.__creationdate=creationdate

    def setMedium(self,medium):
        self.__medium=medium

    def setImageUrl(self,imageurl):
        self.__imageurl=imageurl

    def getArtworkId(self):
        return self.__artworkid
    
    def getTitle(self):
        return self.__title
    
    def getDescription(self):
        return self.__description
    
    def getCreationDate(self):
        return self.__creationdate
    
    def getMedium(self):
        return self.__medium
    
    def getImageUrl(self):
        return self.__imageurl
    
    def __str__(self):
        return (f"Artwork ID : {self.__artworkid}\n"
                f"Title : {self.__title}\n"
                f"Description : {self.__description}\n"
                f"Creation Date : {self.__creationdate}\n"
                f"Medium : {self.__medium}\n"
                f"Imageurl : {self.__imageurl}" )
    
