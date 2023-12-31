#!/usr/bin/python3
"""Unit tests for class User"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Instantiation of User"""

    def test_instantiate(self):
        """Pass instantiation"""
        self.assertEqual(User, type(User()))

    def test_id(self):
        """Pass public id string format"""
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        """Pass created at datetime"""
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        """Pass updated at datetime"""
        self.assertEqual(datetime, type(User().updated_at))

    def test_uid(self):
        """UID created at each instantiation"""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_email(self):
        """Pass email"""
        user1 = User()
        self.assertEqual(str, type(User.email))
        self.assertTrue(hasattr(user1, "email"))

    def test_password(self):
        """Pass password"""
        user1 = User()
        self.assertEqual(str, type(User.password))
        self.assertTrue(hasattr(user1, "password"))

    def test_first_name(self):
        """Pass first name"""
        user1 = User()
        self.assertEqual(str, type(User.first_name))
        self.assertTrue(hasattr(user1, "first_name"))

    def test_last_name(self):
        """Pass last name"""
        user1 = User()
        self.assertEqual(str, type(User.last_name))
        self.assertTrue(hasattr(user1, "last_name"))

    def test_instantiate_kwargs(self):
        """Single instantiate with kwargs"""
        dt = datetime.today()
        user1 = User(
                id="123",
                created_at=dt.isoformat(),
                updated_at=dt.isoformat()
        )
        self.assertEqual(user1.id, "123")
        self.assertEqual(user1.created_at, dt)
        self.assertEqual(user1.updated_at, dt)

    def test_str_rep(self):
        """Pass str representation"""
        user1 = User()
        str_rep = "[{}] ({}) {}".format(
            user1.__class__.__name__,
            user1.id,
            user1.__dict__
            )
        self.assertEqual(str_rep, str(user1))

    def test_save(self):
        """ save method """
        user1 = User()
        update = user1.updated_at
        user1.save()
        self.assertNotEqual(update, user1.updated_at)

    def test_to_dict(self):
        """Pass to_dict method"""
        user1 = User()
        self.assertTrue(dict, type(user1.to_dict))

    def test_to_dict_add_attr(self):
        """Add attribute to dict"""
        user1 = User()
        user1.age = "25"
        user1.state = "California"
        self.assertIn("age", user1.to_dict())
        self.assertIn("state", user1.to_dict())

    def test_to_dict_wrong_arg(self):
        """Add an undefined arg"""
        user1 = User()
        with self.assertRaises(NameError):
            user1.to_dict(hello)


if __name__ == "__main__":
    unittest.main()
