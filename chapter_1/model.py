from dataclasses import dataclass
from typing import Optional
from typing import Set
from datetime import date

@dataclass(frozen=True)
class OrderLine():
    orderid: str 
    sku: str
    qty: int

class Batch():

    def __init__(self, ref: str, sku: str, qty: int, eta: Optional[date]):
        self.ref = ref
        self.sku = sku 
        self._purchase_quantity = qty
        self._allocations: Set[OrderLine] = set()
        self.eta = eta
    
    def allocate(self, line: OrderLine):
        if self.can_allocate(line):
            self._allocations.add(line)

    def deallocate(self, line: OrderLine):
        if line in self._allocations:
            self._allocations.remove(line)

    @property 
    def allocated_quantity(self):
        return sum(line.qty for line in self._allocations)

    @property
    def avaiable_quantity(self):
        return self._purchase_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine):

        return self.sku == line.sku and self.avaiable_quantity >= line.qty