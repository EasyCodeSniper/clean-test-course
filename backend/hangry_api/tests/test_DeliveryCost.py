from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel


def test_high_volume_long_distance_delivery_fee():
    order = MockSet()
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))
    order.add(MockModel(quantity=5))

    assert Delivery.calculate(order, distance=6) == 7.50


def test_medium_volume_delivery_fee():
    order = MockSet()
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))
    order.add(MockModel(quantity=2))

    assert Delivery.calculate(order, distance=4) == 5.00


def test_default_delivery_fee_is_3_50():
    order = MockSet()
    order.add(MockModel(quantity=3))
    order.add(MockModel(quantity=1))

    assert Delivery.calculate(order, distance=2) == 3.50
