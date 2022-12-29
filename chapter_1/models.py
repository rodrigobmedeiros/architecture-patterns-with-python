from dataclasses import dataclass
from datetime import date
from typing import Optional

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
        self.avaiable_quantity = qty
        self.eta = eta 
    
    def allocate(self, order_line: OrderLine):

        self.avaiable_quantity -= order_line.qty


