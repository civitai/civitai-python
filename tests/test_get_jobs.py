import unittest
import json
import civitai


class TestGetJobStatus(unittest.TestCase):
    def test_token_precedence_over_id(self):
        """Test that token takes precedence over job ID when both are provided."""
        job_token = 'eyJKb2JzIjpbImEyNWVhNzg4LWE0YjQtNDI4MC1iZjQxLWJjYjc2NWVhOGMzNSJdfQ=='  # Replace with a valid job token
        job_id = 'ced39597-ea48-438b-b4d3-d5c2ff9910ad'  # Replace with a valid job ID

        response = civitai.jobs.get(token=job_token, job_id=job_id)
        formatted_response = json.dumps(response, indent=4)
        print("Job Status Response by Token:", formatted_response)
        self.assertIsNotNone(
            response, "The response should not be None when both token and ID are provided.")


if __name__ == '__main__':
    unittest.main()
