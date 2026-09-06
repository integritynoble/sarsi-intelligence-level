from config import TIMEOUT_SECONDS

def run(items, timeout_seconds=30):
    """Process items. The default timeout_seconds=30 is a LOCAL default for callers that
    do not want the configured TIMEOUT_SECONDS; it is documented API and must stay 30."""
    limit = TIMEOUT_SECONDS if timeout_seconds is None else timeout_seconds
    return [item for item in items][:limit]
