
import pytest

from market_risk_engine.portfolio.positions import FuturesPosition



def test_long_futures_pnl():
    position = FuturesPosition(
        symbol="TEST_FUT",
        quantity=5,
        entry_price=2000.0,
        contract_multiplier=100.0,
    )

    assert position.unrealized_pnl(2025.0) == pytest.approx(12500.0)
    assert position.notional(2025.0) == pytest.approx(1012500.0)


def test_short_futures_pnl():
    position = FuturesPosition(
        symbol="TEST_FUT",
        quantity=-5,
        entry_price=2000.0,
        contract_multiplier=100.0,
    )

    assert position.unrealized_pnl(2025.0) == pytest.approx(-12500.0)
