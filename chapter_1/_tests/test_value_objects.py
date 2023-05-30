from ..examples_value_objects import Money, Line, Name

def test_equality():

    assert Money('brz', 10) == Money('brz', 10)
    assert Name('rodrigo', 'medeiros') != Name('renata', 'teixeira')
    assert Line('CHAIR', 2) == Line('CHAIR', 2)