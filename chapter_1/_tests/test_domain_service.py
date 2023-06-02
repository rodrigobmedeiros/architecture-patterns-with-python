import pytest
from chapter_1.domain_service import OutOfStock, allocate
from chapter_1.model import Batch, OrderLine
from datetime import datetime, timedelta

@pytest.fixture
def today():
    return datetime.today()

@pytest.fixture
def tomorrow():
    return datetime.today() + timedelta(1)

@pytest.fixture
def later():
    return datetime.today() + timedelta(7)

def test_prefers_current_stock_batches_to_shipments(tomorrow):
    in_stock_batch = Batch('in-stock-batch', "RETRO CLOCK", 100, eta=None)
    shipment_batch = Batch('in-stock-batch', "RETRO CLOCK", 100, eta=tomorrow)
    line = OrderLine('oref', "RETRO CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.avaiable_quantity == 90
    assert shipment_batch.avaiable_quantity == 100

def test_prefers_earlier_batches(today, tomorrow, later):
    earliest = Batch('speedy-batch', "MINIMALIST-SPOON", 100, eta=today)
    medium = Batch('normal-batch', "MINIMALIST-SPOON", 100, eta=tomorrow)
    latest = Batch('slow-batch', "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine('order1', "MINIMALIST-SPOON", 10)


    allocate(line, [latest, medium, earliest])

    assert earliest.avaiable_quantity == 90
    assert medium.avaiable_quantity == 100
    assert latest.avaiable_quantity == 100

def test_returns_allocate_batch_ref(tomorrow):
    in_stock_batch = Batch('in-stock-batch', "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch('in-stock-batch', "HIGHBROW-POSTER", 100, eta=tomorrow)
    line = OrderLine('oref', "HIGHBROW-POSTER", 10)

    allocation = allocate(line, [in_stock_batch, shipment_batch])

    assert allocation == in_stock_batch.ref


def test_raises_out_of_stock_exception_if_cannot_allocate(today):
    batch = Batch('batch1', 'SMALL-FORK', 10, eta=today)
    allocate(OrderLine('order1', 'SMALL-FORK',10), [batch])

    with pytest.raises(OutOfStock, match='SMALL-FORK'):
        allocate(OrderLine('order2', 'SMALL-FORK', 1), [batch])