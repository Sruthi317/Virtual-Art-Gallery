import sys, os
import unittest
from dao.Artworkdao import Artworkdao
from dao.VirtualArtGalleryimpl import VirtualArtGalleryimpl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestArtwork(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = Artworkdao()
        self.obj2 = VirtualArtGalleryimpl()

    # TEST ARTWORK IS ADDED OR NOT
    def test_add_artwork(self):
        print("test_add_artwork")
        result = self.obj1.insert_artwork()
        self.assertEqual(result, True)

    # TEST ARTWORK IS UPDATED OR NOT
    def test_update_artwork(self):
        print("test_update_artwork")
        result = self.obj1.update_artwork()
        self.assertEqual(result, True)

    # TEST ARTWORK IS DELETED OR NOT
    def test_delete_artwork(self):
        print("test_delete_artwork")
        result = self.obj1.delete_artwork()
        self.assertEqual(result, True)

    # TEST SEARCH ARTWORKS FUNCTIONALITY
    def test_searchArtworks(self):
        print("test_searchArtworks")
        result = self.obj2.searchArtworks('Mona Lisa')
        self.assertEqual(result, [('102', 'Mona Lisa', 'Portrait painting of a woman',
                                   '1503-01-02', 'Oil painting',
                                   'mona_lisa.jpg')])

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()



