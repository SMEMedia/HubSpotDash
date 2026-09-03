import unittest

from src.refresh_time import current_refresh_timestamp, latest_refresh_text


class RefreshTimeTests(unittest.TestCase):
    def test_legacy_naive_utc_timestamp_displays_in_eastern_time(self):
        self.assertEqual(
            latest_refresh_text(["2026-09-03T15:36:00"]),
            "2026-09-03 11:36 AM",
        )

    def test_timezone_aware_timestamp_displays_in_eastern_time(self):
        self.assertEqual(
            latest_refresh_text(["2026-09-03T15:36:00+00:00"]),
            "2026-09-03 11:36 AM",
        )

    def test_new_timestamp_includes_timezone_offset(self):
        timestamp = current_refresh_timestamp()
        self.assertRegex(timestamp, r"[+-]\d\d:\d\d$")

    def test_invalid_values_return_none(self):
        self.assertIsNone(latest_refresh_text(["", None, "not a timestamp"]))


if __name__ == "__main__":
    unittest.main()
