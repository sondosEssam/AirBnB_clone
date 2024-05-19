#!/usr/bin/python3
'''
file module
'''


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import patch, MagicMock, mock_open


class TestFileStorage(unittest.TestCase):
    '''
    file storage class
    '''

    def setUp(self):
        '''
        set up constructor
        '''
        self.ag = FileStorage()
        FileStorage._FileStorage__objects = {}

    def test_all_empty(self):
        '''
        test all method when objects are empty
        '''
        FileStorage._FileStorage__objects = {}
        result = self.ag.all()
        self.assertEqual(result, {})

    def test_all_oocupied(self):
        '''
        test all method when it's not empty
        '''
        FileStorage._FileStorage__objects = {'val': 3, 'val2': 2, 'val3': 1}
        res = self.ag.all()
        self.assertEqual(res, {'val': 3, 'val2': 2, 'val3': 1})

    @patch('models.base_model.BaseModel')
    def test_new(self, MockBaseModel):
        '''
        tests if new adds values to the class
        '''
        mock_obj = MagicMock()
        mock_obj.__class__.__name__ = "BaseModel"
        mock_obj.id = "1234"
        self.ag.new(mock_obj)
        expected_key = "BaseModel.1234"
        self.assertIn(expected_key, self.ag.all())
        self.assertEqual(self.ag.all()[expected_key], mock_obj)

    @patch('models.engine.file_storage.open', new_callable=mock_open)
    @patch('models.engine.file_storage.json.dump')
    def test_save(self, mock_json_dump, mock_open):
        '''
        test save method
        '''

        mock_obj = MagicMock()
        mock_obj.to_dict.return_value = {'id': '1234', 'name': 'Test'}
        FileStorage._FileStorage__objects = {'BaseModel.1234': mock_obj}
        self.ag.save()
        mock_open.assert_called_once_with(
            FileStorage._FileStorage__file_path, 'w', encoding='utf-8'
            )
        mock_json_dump.assert_called_once_with(
            {'BaseModel.1234': {'id': '1234', 'name': 'Test'}},
            mock_open())

    @patch('models.engine.file_storage.open',
           new_callable=mock_open,
           read_data='{"BaseModel.1234": {"id": "1234", "name": "Test"}}')
    @patch('models.engine.file_storage.json.load')
    def test_reload(self, mock_json_load, mock_open):
        '''
        test reload
        '''
        mock_json_load.return_value = {
            "BaseModel.1234": {"id": "1234", "name": "Test"}
            }
        with patch('models.base_model.BaseModel',
                   wraps=BaseModel) as MockBaseModel:
            self.ag.reload()
            MockBaseModel.assert_called_once_with(id="1234", name="Test")
            self.assertIn("BaseModel.1234", self.ag.all())
            self.assertIsInstance(self.ag.all()["BaseModel.1234"], BaseModel)
