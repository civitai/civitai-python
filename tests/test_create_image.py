# test/test_create_image.py
import unittest
import civitai


class TestCreateImage(unittest.TestCase):
    def test_create_from_text_job(self):
        input = {
            "model": "urn:air:sd1:checkpoint:civitai:4201@130072",
            "params": {
                "prompt": "A cat",
                "negativePrompt": "A dog",
                "scheduler": "EulerA",
                "steps": 30,
                "cfgScale": 10,
                "width": 768,
                "height": 512,
                "seed": -1,
                "clipSkip": 1
            },
        }

        # Test case when wait=False
        # output = civitai_py.image.create(input, wait=False)
        # print("Response (wait=False):", output)

        # self.assertIsNotNone(output, "The output should not be None.")
        # self.assertIn("token", output, "The output should contain a 'token' key.")

        # Test case when wait=True
        output = civitai_py.image.create(input, wait=True)
        print("Response (wait=True):", output)

        self.assertIsNotNone(output, "The output should not be None.")
        self.assertIn("jobs", output, "The output should contain a 'jobs' key.")
        self.assertGreater(len(output["jobs"]), 0, "The 'jobs' list should not be empty.")
        self.assertIn("result", output["jobs"][0], "The job should have a 'result' key.")


if __name__ == '__main__':
    unittest.main()
