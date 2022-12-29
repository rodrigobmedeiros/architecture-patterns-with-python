from datetime import date
from typing import Tuple
from models import Batch
from models import OrderLine

def make_batch_and_line(
    sku: str, 
    batch_qty: int, 
    line_qty: int
) -> Tuple[Batch, OrderLine]:
    """Return batch and line objects to be used into other tests without 
    duplicate code.

    Args:
        sku (str): item unique identifier.
        batch_qty (int): quantity of item avaible into a bacth.
        line_qty (int): quantity of item required for a order line.

    Returns:
        Tuple[Batch, OrderLine]: instances of Batch and OrderLine ready to use.
    """

    return (
        Batch('batch-001', sku, batch_qty),
        OrderLine('order-123', sku, line_qty)
    )


def test_allocating_to_a_batch_reduces_the_avaiable_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.avaiable_quantity == 18

def test_can_allocate_if_avaiablae_greater_than_required():
    large_batch, small_line = make_batch_and_line('ELEGANT-LAMP', 20,2)
    assert large_batch.can_allocate(small_line)