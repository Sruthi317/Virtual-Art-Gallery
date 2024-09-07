import sys,os
import unittest
from dao.Gallerydao import Gallerydao
from dao.VirtualArtGalleryimpl import VirtualArtGalleryimpl

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestGalleryManagement(unittest.TestCase):
    # SET UP
    def setUp(self):
        print("Set Up")
        self.obj1 = Gallerydao()
        self.obj2 = VirtualArtGalleryimpl()

    # TEST GALLERY IS ADDED OR NOT
    def test_add_gallery(self):
        print("test_add_gallery")
        result = self.obj1.insert_gallery()
        self.assertEqual(result, True)

    # TEST GALLERY IS UPDATED OR NOT
    def test_update_gallery(self):
        print("test_update_gallery")
        result = self.obj1.update_gallery()
        self.assertEqual(result, True)

    # TEST GALLERY IS DELETED OR NOT
    def test_delete_gallery(self):
        print("test_delete_gallery")
        result = self.obj1.delete_gallery()
        self.assertEqual(result, True)

    # TEST SEARCH GALLERIES FUNCTIONALITY
    def test_searchGalleries(self):
        print("test_searchGalleries")
        result = self.obj2.searchGalleries('Louvre Museum')
        self.assertEqual(result, [(401, 'Louvre Museum', 'World-renowned art museum located in Paris',
                                   'Paris', 201, '9 AM to 6 PM')])

    # TEAR DOWN
    def tearDown(self):
        print("Tear Down")


if __name__ == '__main__':
    unittest.main()
