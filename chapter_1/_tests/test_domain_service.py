

from chapter_1.domain_service import allocate
from chapter_1.model import Batch, OrderLine


def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch('in-stock-batch', "RETRO CLOCK", 100, eta=None)
    shipment_batch = Batch('in-stock-batch', "RETRO CLOCK", 100, eta='tomorrow')
    line = OrderLine('oref', "RETRO CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])

    assert in_stock_batch.avaiable_quantity == 90
    assert shipment_batch.avaiable_quantity == 100

def test_prefers_earlier_batches():
    earliest = Batch('speedy-batch', "MINIMALIST-SPOON", 100, eta='today')
    medium = Batch('normal-batch', "MINIMALIST-SPOON", 100, eta='tomorrow')
    latest = Batch('slow-batch', "MINIMALIST-SPOON", 100, eta='later')
    line = OrderLine('order1', "MINIMALIST-SPOON", 10)


    allocate(line, [latest, medium, earliest])

    assert earliest.avaiable_quantity == 90
    assert medium.avaiable_quantity == 100
    assert latest.avaiable_quantity == 100

def test_returns_allocate_batch_ref():
    in_stock_batch = Batch('in-stock-batch', "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch('in-stock-batch', "HIGHBROW-POSTER", 100, eta='tomorrow')
    line = OrderLine('oref', "HIGHBROW-POSTER", 10)

    allocation = allocate(line, [in_stock_batch, shipment_batch])

    assert allocation == in_stock_batch.ref