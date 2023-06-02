from .model import OrderLine, Batch

class OutOfStock(Exception):
    ...

def allocate(line: OrderLine, batches: list[Batch]) -> str:
    
    # Order by eta
    try:
        batch_to_allocate = next(
            batch for batch in sorted(batches) 
            if batch.can_allocate(line)
        )
        batch_to_allocate.allocate(line)
    except StopIteration:
        raise OutOfStock(f'Out of stock for sku: {line.sku}')
    
    return batch_to_allocate.ref
