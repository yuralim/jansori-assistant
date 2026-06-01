import logging
from contextvars import ContextVar

request_id: ContextVar[str | None] = ContextVar("request_id", default=None)

_LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s [req=%(request_id)s] - %(message)s"

_configured = False


class RequestIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = request_id.get() or "-"
        return True


def configure_logging(level: int = logging.INFO) -> None:
    global _configured
    if _configured:
        return

    logging.basicConfig(level=level, format=_LOG_FORMAT)
    filt = RequestIdFilter()
    for handler in logging.getLogger().handlers:
        handler.addFilter(filt)
    _configured = True
