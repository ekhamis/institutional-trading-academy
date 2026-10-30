"""Deterministic checks for arithmetic explicitly taught in v0.12."""
from decimal import Decimal

def test_index_multipliers():
    assert Decimal('8') * Decimal('50') == Decimal('400')
    assert Decimal('25') * Decimal('20') == Decimal('500')

def test_tick_grids():
    assert Decimal('6200.10') % Decimal('0.25') != 0
    assert Decimal('2750.05') % Decimal('0.10') != 0

def test_micro_scale_examples():
    assert Decimal('50') / Decimal('5') == 10
    assert Decimal('100') / Decimal('10') == 10

if __name__ == '__main__':
    test_index_multipliers(); test_tick_grids(); test_micro_scale_examples()
    print('instrument arithmetic tests: 3 passed')
