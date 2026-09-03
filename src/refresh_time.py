from __future__ import annotations

from datetime import datetime
from typing import Iterable
from zoneinfo import ZoneInfo

import pandas as pd


DASHBOARD_TIMEZONE = ZoneInfo("America/New_York")


def current_refresh_timestamp() -> str:
    """Return an unambiguous timestamp for the refresh log."""
    return datetime.now(DASHBOARD_TIMEZONE).isoformat(timespec="seconds")


def latest_refresh_text(values: Iterable[object]) -> str | None:
    """Format the latest refresh in dashboard time.

    Older cache rows contain timezone-less values written by a server running in
    UTC, so pandas is intentionally told to interpret naive values as UTC too.
    """
    timestamps = pd.to_datetime(list(values), errors="coerce", utc=True, format="mixed")
    valid = timestamps[~pd.isna(timestamps)]
    if len(valid) == 0:
        return None
    latest = valid.max().tz_convert(DASHBOARD_TIMEZONE)
    return latest.strftime("%Y-%m-%d %I:%M %p")
