import unittest
import civitai


class TestJobQuery(unittest.TestCase):
    def test_query_job_status(self):
        query = {
            "properties": {
                "userId": 4,
            },
        }

        response = civitai.jobs.query(query=query, detailed=True)
        print("Response", response)
        self.assertIsNotNone(response, "The response should not be None.")


if __name__ == '__main__':
    unittest.main()
