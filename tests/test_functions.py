from typing import Any, SupportsRound


class RoundErrorWarning(SupportsRound['RoundErrorWarning']):
    """
    Testing for flagged issue regarding rounding error for the
    final metric values once the class ReportMetric has been initalised.
    """

    def __round__(self: 'RoundErrorWarning', ndigits: int = 0) -> 'RoundErrorWarning':
        return self


def test_tmp() -> None:
    x = RoundErrorWarning()
    result: RoundErrorWarning

    result = round(x, 0)
    assert type(result) == RoundErrorWarning
    result = round(x)
    assert type(result) == RoundErrorWarning
