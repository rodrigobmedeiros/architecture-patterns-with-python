from dataclasses import dataclass
from datetime import date
from typing import Optional
from typing import Set

__all__ = [
    'Batch',
    'OrderLine'
]

@dataclass(frozen=True)
class OrderLine:
    order_id: str
    sku: str
    qty: int

class Batch:

    def __init__(self, reference: str, sku: str, qty: int, eta: Optional[date]):

        self.reference = reference
        self.sku = sku
        self.eta = eta 
        self._purchased_quantity = qty
        self._allocations: Set[OrderLine] = set()
    
    @property
    def allocated_quantity(self) -> int:
        return sum(line.qty for line in self._allocations)

    @property
    def avaiable_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity
    
    def allocate(self, order_line: OrderLine):
        if self.can_allocate(order_line):
            self._allocations.add(order_line)

    def deallocate(self, order_line: OrderLine):
        if order_line in self._allocations:
            self._allocations.remove(order_line)

    def can_allocate(self, order_line: OrderLine) -> bool:

        same_sku: bool = self.sku == order_line.sku
        has_avaiable_quantity: bool = self.avaiable_quantity >= order_line.qty

        return same_sku & has_avaiable_quantity


