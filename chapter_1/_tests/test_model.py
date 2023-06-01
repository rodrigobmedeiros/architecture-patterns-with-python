from datetime import date
from chapter_1.model import Batch
from chapter_1.model import OrderLine

def make_batch_and_line(sku, batch_qty, line_qty):

    return (
        Batch('batch-001', sku, batch_qty, eta=date.today()),
        OrderLine('order-001', sku, line_qty)
    )

def test_allocate_to_a_batch_reduces_the_avaiable_quantity():
    batch, line = make_batch_and_line("SMALL-TABLE", 20, 2)
    batch.allocate(line)

    assert batch.avaiable_quantity == 18

def test_can_allocate_if_avaiable_greater_than_required():
    large_batch, small_line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    assert large_batch.can_allocate(small_line)

def test_cannot_allocate_if_avaiable_less_than_required():
    small_batch, large_line = make_batch_and_line('ELEGANT-LAMP', 2, 20)
    assert small_batch.can_allocate(large_line) is False

def test_can_allocate_if_avaiable_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch('order-001', 'UNCOMFORTABLE-CHAIR', 100, eta=None)
    different_sku_line = OrderLine('order-001', 'EXPENSIVE-TOASTER', 10)
    assert batch.can_allocate(different_sku_line) is False

def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = make_batch_and_line('DECORATIVE-TRINKET', 20, 2)
    batch.deallocate(unallocated_line)
    assert batch.avaiable_quantity == 20

def test_allocation_is_idempontent():
    batch, line = make_batch_and_line('ELEGANT-LAMP', 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.avaiable_quantity == 18

def test_raises_out_of_stock_exception_if_cannot_allocate(today):
    ...