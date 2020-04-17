import unittest
import json
import os
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import setup_db


class ResourceTestCase(unittest.TestCase):
    """This class represents the resource test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "bookshelf_test"
        self.database_path = ""
        setup_db(self.app, self.database_path)

        self.new_book = {
            'title': 'Anansi Boys',
            'author': 'Neil Gaiman',
            'rating': 5
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_paginated_books(self):
        res = self.client.get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_books'])
        self.assertTrue(len(data['books']))


if __name__ == "__main__":
    unittest.main()
