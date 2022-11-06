from typing import Any, SupportsRound


class RoundErrorWarning(SupportsRound['RoundErrorWarning']):

    def __round__(self: 'RoundErrorWarning', ndigits: int = 0) -> 'RoundErrorWarning':
        return self


def test_tmp() -> None:
    x = RoundErrorWarning()
    result: RoundErrorWarning

    result = round(x, 0)
    assert type(result) == RoundErrorWarning
    result = round(x)
    assert type(result) == RoundErrorWarning

