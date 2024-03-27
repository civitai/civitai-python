# tests/test_civitai.py
import unittest
import civitai


class TestCivitaiJobStatus(unittest.TestCase):
    def test_get_job_status(self):
        """Test retrieving job status using a token."""
        # Replace 'your_job_token' with a valid job token
        job_token = 'eyJKb2JzIjpbIjdmODQ5NzJmLTRlMmEtNDkyNC1iMzI0LTA4YTI2MTI3YWIyMCJdfQ=='

        # Use the exposed 'jobs' attribute to retrieve job status
        response = civitai.jobs.get(token=job_token)

        print("Job Status Response:", response)
        self.assertIsNotNone(response, "The response should not be None.")


if __name__ == '__main__':
    unittest.main()
