class ArtworkIdNotFoundException(Exception):
    def __init__(self,artworkid):
        super().__init__(f"Artwork ID {artworkid} not found.")