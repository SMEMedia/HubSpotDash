from datetime import date
import unittest

from src.hubspot_client import HubSpotClient


class MarketingEmailDiscoveryTests(unittest.TestCase):
    def test_filters_by_publish_date_instead_of_creation_date(self):
        client = HubSpotClient("token")
        requests = []

        def fake_get_json(path, params=None):
            requests.append((path, dict(params or {})))
            return {"results": []}

        client._get_json = fake_get_json

        client.marketing_emails(published_after=date(2026, 8, 23))

        self.assertEqual(
            requests[0][1]["publishedAfter"],
            "2026-08-23T00:00:00Z",
        )
        self.assertNotIn("createdAfter", requests[0][1])

    def test_email_date_prefers_publish_date_over_old_creation_date(self):
        email = {
            "createdAt": "2026-01-10T12:00:00Z",
            "publishedAt": "2026-08-25T14:30:00Z",
        }

        self.assertEqual(HubSpotClient.email_date(email), date(2026, 8, 25))


if __name__ == "__main__":
    unittest.main()
