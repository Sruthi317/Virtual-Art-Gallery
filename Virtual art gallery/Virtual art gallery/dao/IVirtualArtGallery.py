from abc import ABC, abstractmethod
from entity.artwork import Artwork
from typing import List

class IVirtualArtGallery(ABC):
    @abstractmethod
    def addArtwork(self,artwork) -> bool:
        pass
    
    @abstractmethod
    def updateArtwork(self,artwork) -> bool:
        pass

    @abstractmethod
    def removeArtwork(self,artworkid) -> bool:
        pass

    @abstractmethod
    def getArtworkById(self,artworkid) -> Artwork:
        pass

    @abstractmethod
    def searchArtworks(self,artwork) -> List[Artwork]:
        pass

    @abstractmethod
    def addArtworkToFavorite(self,userid,artworkid) -> bool:
        pass

    @abstractmethod
    def removeArtworkFromFavorite(self,userid,artworkid) -> bool:
        pass

    @abstractmethod
    def getUserFavoriteArtworks(self,userid) -> bool:
        pass



