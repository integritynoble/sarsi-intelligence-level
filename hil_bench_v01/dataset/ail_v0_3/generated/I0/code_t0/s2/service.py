from config import MAX_RETRIES

def run(items, max_retries=250):
    """Process items. The default max_retries=250 is a LOCAL default for callers that
    do not want the configured MAX_RETRIES; it is documented API and must stay 250."""
    limit = MAX_RETRIES if max_retries is None else max_retries
    return [item for item in items][:limit]
