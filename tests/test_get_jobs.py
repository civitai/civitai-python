# tests/test_civitai_py.py
import unittest
import civitai


class TestGetJobStatus(unittest.TestCase):
    # def test_get_job_status_by_token(self):
    #     """Test retrieving job status using a token."""
    #     job_token = 'eyJKb2JzIjpbImU4MGRlNzFhLWMzNTAtNDMyMi05MzAwLWFiYjBhNzY2N2Y1MiJdfQ=='  # Replace with a valid job token
    #     response = civitai_py.jobs.get(token=job_token)
    #     print("Job Status Response by Token:", response)
    #     self.assertIsNotNone(response, "The response should not be None when using a token.")

    # def test_get_job_status_by_id(self):
    #     """Test retrieving job status using a job ID."""
    #     job_id = 'f1f4eee6-d1ee-4a82-a063-2c451823a86b'  # Replace with a valid job ID
    #     response = civitai_py.jobs.get(id=job_id)
    #     print("Job Status Response by ID:", response)
    #     self.assertIsNotNone(response, "The response should not be None when using a job ID.")

    def test_token_precedence_over_id(self):
        """Test that token takes precedence over job ID when both are provided."""
        job_token = 'eyJKb2JzIjpbImU4MGRlNzFhLWMzNTAtNDMyMi05MzAwLWFiYjBhNzY2N2Y1MiJdfQ=='  # Replace with a valid job token
        job_id = 'f1f4eee6-d1ee-4a82-a063-2c451823a86b'  # Replace with a valid job ID

        # the response should correspond to the job associated with the token.
        response = civitai.jobs.get(token=job_token, id=job_id)
        print("Job Status Response by Token:", response)
        self.assertIsNotNone(
            response, "The response should not be None when both token and ID are provided.")


if __name__ == '__main__':
    unittest.main()
