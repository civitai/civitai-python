# tests/test_civitai.py

import os
from dotenv import load_dotenv
import unittest
from civitai.civitai import Civitai

load_dotenv(dotenv_path=".env.test")


class TestCivitaiFromText(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up Civitai client for tests."""
        cls.civitai = Civitai({
            'auth': os.getenv('CIVITAI_API_TOKEN', ''),
            'env': 'dev'
        })

    def test_from_text_success(self):
        """Test successfully creating a FromText job."""
        input = {
            'model': 'urn:air:sd1:checkpoint:civitai:4201@130072',
            'params': {
                'prompt': 'A cat',
                'negativePrompt': 'A dog',
                'scheduler': 'EulerA',
                'steps': 30,
                'cfgScale': 10,
                'width': 768,
                'height': 512,
                'seed': -1,
                'clipSkip': 1,
            },
            'quantity': 1,
        }
        # Long polling as we pass in `wait` parameter
        output = self.civitai.from_text(input, True)
        print("Response:", output)
        self.assertIsNotNone(output)


if __name__ == '__main__':
    unittest.main()
