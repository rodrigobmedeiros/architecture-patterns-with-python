from .model import OrderLine, Batch

def allocate(line: OrderLine, batches: list[Batch]) -> int:
    
    # Order by eta
    etas = [None, 'today', 'tomorrow', 'later']
    
    batch_to_allocate = next(
        batch for batch in sorted(batches, key=lambda batch: etas.index(batch.eta)) 
        if batch.can_allocate(line)
    )
    batch_to_allocate.allocate(line)

    return batch_to_allocate.ref
