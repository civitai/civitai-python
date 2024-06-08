import unittest
import json
import civitai


class TestCreateImage(unittest.TestCase):
    def test_create_from_text_job(self):
        input_data = {
            "model": "urn:air:sdxl:checkpoint:civitai:101055@128078",
            "params": {
                "prompt": "RAW photo, face portrait photo of 26 y.o woman, wearing black dress, happy face, hard shadows, cinematic shot, dramatic lighting",
                "negativePrompt": "(deformed, distorted, disfigured:1.3)",
                "scheduler": "EulerA",
                "steps": 20,
                "cfgScale": 7,
                "width": 512,
                "height": 512,
                "clipSkip": 2
            }
        }

        output = civitai.image.create(input_data, wait=True)
        formatted_output = json.dumps(output, indent=4)
        print("Response: ", formatted_output)

        self.assertIsNotNone(output, "The output should not be None.")
        self.assertIn("jobs", output,
                      "The output should contain a 'jobs' key.")
        self.assertGreater(len(output["jobs"]), 0,
                           "The 'jobs' list should not be empty.")


if __name__ == '__main__':
    unittest.main()
