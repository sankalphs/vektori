from datetime import datetime

from benchmarks.locomo.locomo_runner import LoCoMoConfig, _parse_date


def test_locomo_defaults_disable_retrieval_gate():
    config = LoCoMoConfig()

    assert config.enable_retrieval_gate is False


def test_parse_date_supports_locomo_native_format():
    parsed = _parse_date("9:55 am on 22 October, 2023")

    assert parsed == datetime(2023, 10, 22, 9, 55)


def test_parse_date_supports_locomo_native_short_month_format():
    parsed = _parse_date("1:56 pm on 8 May, 2023")

    assert parsed == datetime(2023, 5, 8, 13, 56)
