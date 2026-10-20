
from dataclasses import dataclass


@dataclass(frozen=True)
class FuturesPosition:
    symbol: str
    quantity: int
    entry_price: float
    contract_multiplier: float
    currency: str = "USD"

    def notional(self, market_price: float) -> float:
        """Calculate signed futures notional exposure."""
        return (
            self.quantity
            * self.contract_multiplier
            * market_price
        )

    def unrealized_pnl(self, market_price: float) -> float:
        """Calculate unrealized futures P&L in quote currency."""
        return (
            self.quantity
            * self.contract_multiplier
            * (market_price - self.entry_price)
        )
