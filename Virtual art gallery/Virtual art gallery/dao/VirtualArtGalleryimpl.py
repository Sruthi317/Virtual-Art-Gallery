import pyodbc
from dao.IVirtualArtGallery import IVirtualArtGallery
from util.DBConnection import DBConnection
from exception.Artworkid_exception import ArtworkIdNotFoundException
from exception.Userid_exception import UserIdNotFoundException
from entity.artwork import Artwork
from typing import List, Tuple
"""Artwork
ArtworkID (Primary Key)
Title
Description
CreationDate
Medium
ImageURL (or any reference to the digital representation)"""
class VirtualArtGalleryimpl(IVirtualArtGallery):
    def __init__(self):
        self.conn=DBConnection.getConnection()
        self.cursor=self.conn.cursor()

    def __del__(self):
        if self.conn is not None and not self.conn.closed:
            self.conn.close()

    def addArtwork(self,artwork:Artwork) -> bool:
        try:
            self.cursor.execute("""insert into Artwork values (?,?,?,?,?,?)""",
                                (artwork.getArtworkId(), artwork.getTitle(),artwork.getDescription(),artwork.getCreationDate(),
                                 artwork.getMedium(),artwork.getImageUrl()))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Artwork cannot be added : {err}")
            return False
    
    def updateArtwork(self,artwork:Artwork) -> bool:
        try:
            self.cursor.execute("""update artwork set title=? , description=?, creationdate=?, medium=?, imageurl=?
                                where artworkid=?""",(artwork.getTitle(), artwork.getDescription(),
                                artwork.getCreationDate(), artwork.getMedium(), artwork.getImageUrl(),artwork.getArtworkId()))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Artwork cannot be updated : {err}")
            return False

    def removeArtwork(self,artworkid) -> bool:
        try:
            self.cursor.execute("""delete from artwork where artworkid=?""",(artworkid,))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Artwork cannot be deleted : {err}")
            return False     
            
    def getArtworkById(self,artworkid) -> Artwork:
        try:
            self.cursor.execute("""select * from artwork where artworkid=?""",(artworkid,))
            result=self.cursor.fetchone()
            if result:
                artworks=Artwork(*result)
                return artworks
        except ArtworkIdNotFoundException as err:
            print (f"Exception : {err}")
            return []

    def searchArtworks(self, keyword: str) -> List[Tuple[str]]:
        try:
            self.cursor.execute("""SELECT * FROM artwork WHERE title LIKE ?""", ('%' + keyword + '%',))
            records = self.cursor.fetchall()
            if records:
                # Convert each record to a tuple and add it to the list
                artworks = [(str(record[0]), record[1], record[2], record[3], record[4], record[5]) for record in records]
                return artworks
            else:
                print("No artworks found with the given keyword.")
                return []
        except pyodbc.Error as e:
            print(f"Error fetching artworks: {e}")
            return []


    def addArtworkToFavorite(self,userid,artworkid) -> bool:
        try:
            self.cursor.execute("""update users set favorite_artworks=? where userid=?""",(artworkid,userid,))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Artwork cannot be added to favourite: {err}")
            return False

    def removeArtworkFromFavorite(self, userId, artworkId) -> bool:
        try:
            self.cursor.execute("""UPDATE Users SET favorite_artworks = NULL WHERE userid = ? AND favorite_artworks = ?""", (userId, artworkId,))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Artwork cannot be removed from favorites: {err}")
            return False

    def getUserFavoriteArtworks(self, userId) -> bool:
        try:
            self.cursor.execute("""
                SELECT a.*
                FROM Users u
                JOIN artwork a ON u.favorite_artworks = a.artworkid
                WHERE u.UserID = ?
            """, (userId,))
            result = self.cursor.fetchall()
            if result:
                print(f"Favorite artworks for user {userId}:")
                for row in result:
                    artwork_id, title, description, creation_date, medium, image_url = row
                    print(f"Artwork ID: {artwork_id}")
                    print(f"Title: {title}")
                    print(f"Description: {description}")
                    print(f"Creation Date: {creation_date}")
                    print(f"Medium: {medium}")
                    print(f"Image URL: {image_url}")
                return True
            else:
                print("User has no favorite artworks.")
                return False
        except UserIdNotFoundException as err:
            print(f"User ID not found : err")
        except pyodbc.Error as err:
            print(f"Error fetching user's favorite artworks: {err}")
            return False

    def searchGalleries(self, keyword: str) -> List[Tuple[str]]:
        try:
            self.cursor.execute("""SELECT * FROM gallery WHERE name LIKE ?""", ('%' + keyword + '%',))
            records = self.cursor.fetchall()
            if records:
                # Convert each record to a tuple and add it to the list
                galleries = [(record[0], record[1], record[2], record[3],record[4],record[5]) for record in records]
                return galleries
            else:
                print("No galleries found with the given keyword.")
                return []
        except pyodbc.Error as e:
            print(f"Error fetching galleries: {e}")
            return []


