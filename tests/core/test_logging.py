import logging

from core.logging import RequestIdFilter, request_id


def test_filter_uses_context_var():
    record = logging.LogRecord("x", logging.INFO, __file__, 1, "msg", None, None)
    token = request_id.set("abc123")
    try:
        assert RequestIdFilter().filter(record) is True
        assert record.request_id == "abc123"
    finally:
        request_id.reset(token)


def test_filter_defaults_to_dash_when_unset():
    record = logging.LogRecord("x", logging.INFO, __file__, 1, "msg", None, None)
    assert RequestIdFilter().filter(record) is True
    assert record.request_id == "-"
