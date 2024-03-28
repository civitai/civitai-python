# test/test_query_jobs.py
import unittest
import civitai_py as civitai
import json


class TestJobQuery(unittest.TestCase):
    def test_query_job_status(self):
        query = {
            "properties": {
                "userId": 4,
                "modelId": 359773,
            },
        }

        # Perform the query.
        response = civitai.jobs.query(
            detailed=True,
            query_jobs_request=query
        )

        print("Response", response)
        self.assertIsNotNone(response, "The response should not be None.")


if __name__ == '__main__':
    unittest.main()
