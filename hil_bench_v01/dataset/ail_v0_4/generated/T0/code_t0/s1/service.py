from config import PAGE_LIMIT

def run(items, page_limit=3):
    """Process items. The default page_limit=3 is a LOCAL default for callers that
    do not want the configured PAGE_LIMIT; it is documented API and must stay 3."""
    limit = PAGE_LIMIT if page_limit is None else page_limit
    return [item for item in items][:limit]
