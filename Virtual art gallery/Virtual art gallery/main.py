from dao.VirtualArtGalleryimpl import VirtualArtGalleryimpl
from entity.artwork import Artwork
from entity.user import User
from dao.Artworkdao import Artworkdao
from dao.Artistdao import Artistdao
from dao.Userdao import Userdao
from dao.Gallerydao import Gallerydao

class MainModule:
    def __init__(self):
        self.ArtworkRecord = VirtualArtGalleryimpl()
    
    print("\nWelcome to the Virtual Art Gallery Management System")
    print("---------------------------------------------------")
    while True:
        print("\n---------\n1.Artist\n2.Artwork\n3.User\n4.Gallery\n0.EXIT\n---------\n")
        ch = int(input("Enter choice: "))
        if ch == 1:
            artist = Artistdao()
            artist.Artist_choice()
        elif ch == 2:
            artwork = Artworkdao()
            artwork.Artwork_choice()
        elif ch == 3:
            user = Userdao()
            user.User_choice()
        elif ch == 4:
            gallery = Gallerydao()
            gallery.Gallery_choice()
        elif ch == 0:
            break
        else:
            print("Invalid choice")

    def switch(self,choice):
        switcher={
            1: self.addArtwork,
            2: self.updateArtwork,
            3: self.removeArtwork,
            4: self.getArtworkById,
            5: self.searchArtworks,
            6: self.addArtworkToFavorite,
            7: self.removeArtworkFromFavorite,
            8: self.getUserFavoriteArtworks,
            9: exit
        }
        func = switcher.get(choice, lambda: print("Invalid choice"))
        func()
        """Artwork
        ArtworkID (Primary Key)
        Title
        Description
        CreationDate
        Medium
        ImageURL (or any reference to the digital representation)"""
    def addArtwork(self):
        try:
            Artworkid = input("Enter Artwork ID : ")
            Title = input("Enter Title for artwork : ")
            Description = input("Enter Description for artwork : ")
            Creation_date=input("Enter Creation date for artwork : ")
            medium=input("Enter Medium : ")
            imageurl=input("Enter ImageURL : ")
            artwork=Artwork(Artworkid,Title,Description,Creation_date,medium,imageurl)
            success=self.ArtworkRecord.addArtwork(artwork)
            if success:
                print("Artwork Added successfully")
            else:
                print("Unable to add artwork")
        except Exception as e:
            print("Error : {e}")
    
    def updateArtwork(self):
        try:
            artworkId = input("Enter Artwork ID to update: ")
            artwork = self.ArtworkRecord.getArtworkById(artworkId)
            if artwork:
                print("Current Artwork Details:")
                print(artwork)
                # Prompt for updated information
                title = input("Enter new title (leave blank to keep current): ")
                description = input("Enter new description (leave blank to keep current): ")
                creation_date = input("Enter new creation date (leave blank to keep current): ")
                medium = input("Enter new medium (leave blank to keep current): ")
                image_url = input("Enter new image URL (leave blank to keep current): ")

                # Update the artwork if new information provided
                if title:
                    artwork.setTitle(title)
                if description:
                    artwork.setDescription(description)
                if creation_date:
                    artwork.setCreationDate(creation_date)
                if medium:
                    artwork.setMedium(medium)
                if image_url:
                    artwork.setImageUrl(image_url)

                # Update the record
                if self.ArtworkRecord.updateArtwork(artwork):
                    print("Artwork updated successfully.")
                else:
                    print("Unable to update artwork.")
            else:
                print("Artwork not found.")
        except Exception as e:
            print(f"Error: {e}")

    def removeArtwork(self):
        try:
            artworkId = input("Enter Artwork ID to remove: ")
            if self.ArtworkRecord.removeArtwork(artworkId):
                print("Artwork removed successfully.")
            else:
                print("Unable to remove artwork.")
        except Exception as e:
            print(f"Error: {e}")

    def getArtworkById(self):
        try:
            artworkId = input("Enter Artwork ID: ")
            artwork = self.ArtworkRecord.getArtworkById(artworkId)
            if artwork:
                print("Artwork details:")
                print(artwork)
            else:
                print("Artwork not found.")
        except Exception as e:
            print(f"Error: {e}")

    def searchArtworks(self):
        try:
            title = input("Enter Artwork Title: ")
            artworks = self.ArtworkRecord.searchArtworks(title)
            if artworks:
                for art in artworks:
                    print(art)
            else:
                print("Artwork title not found")
        except Exception as e:
            print(f"Error: {e}")

    def addArtworkToFavorite(self):
        try:
            userId = input("Enter User ID: ")
            artworkId = input("Enter Artwork ID to add to favorites: ")
            if self.ArtworkRecord.addArtworkToFavorite(userId, artworkId):
                print("Artwork added to favorites successfully.")
            else:
                print("Unable to add artwork to favorites.")
        except Exception as e:
            print(f"Error: {e}")

    def removeArtworkFromFavorite(self):
        try:
            userId = input("Enter User ID: ")
            artworkId = input("Enter Artwork ID to remove from favorites: ")
            if self.ArtworkRecord.removeArtworkFromFavorite(userId, artworkId):
                print("Artwork removed from favorites successfully.")
            else:
                print("Unable to remove artwork from favorites.")
        except Exception as e:
            print(f"Error: {e}")

    def getUserFavoriteArtworks(self):
        try:
            userId = input("Enter User ID: ")
            if self.ArtworkRecord.getUserFavoriteArtworks(userId):
                print("Favorite artworks fetched successfully.")
            else:
                print("Unable to fetch favorite artworks.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main_module = MainModule()
    while True:
        print("\n1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. Get Artwork By ID")
        print("5. Search Artwork")
        print("6. Add Artwork to Favorite")
        print("7. Remove Artwork from Favorite")
        print("8. Get User Favorite Artworks")
        print("9. Exit")
        choice = int(input("Enter your choice: "))
        main_module.switch(choice)