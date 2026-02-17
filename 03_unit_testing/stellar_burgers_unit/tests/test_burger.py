import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:
    """Юнит-тесты для класса Burger"""

    # === ИНИЦИАЛИЗАЦИЯ ===
    def test_new_burger_has_no_bun(self):
        burger = Burger()
        assert burger.bun is None


    def test_new_burger_has_empty_ingredients_list(self):
        burger = Burger()
        assert burger.ingredients == []

    # === SET_BUNS ===
    def test_set_buns_sets_bun(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    # === ADD_INGREDIENT ===
    def test_add_ingredient_adds_to_ingredients_list(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert len(burger.ingredients) == 1

    def test_added_ingredient_is_correct(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        assert burger.ingredients[0] == ingredient

    # === REMOVE_INGREDIENT ===
    def test_remove_ingredient_removes_from_list(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_remove_ingredient_with_invalid_index_raises_error(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.remove_ingredient(999)

    # === MOVE_INGREDIENT ===
    def test_move_ingredient_changes_order(self, bun):
        burger = Burger()
        burger.set_buns(bun)
        mock1, mock2 = Mock(), Mock()
        burger.add_ingredient(mock1)
        burger.add_ingredient(mock2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock2, mock1]

    def test_move_ingredient_with_invalid_index_raises_error(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)
        with pytest.raises(IndexError):
            burger.move_ingredient(999, 0)

    # === GET_PRICE ===
    @pytest.mark.parametrize("bun_price,ingredient_prices,expected", [
        (100, [50, 75], 325),
        (0, [10, 20, 30], 60),
        (250, [], 500),
        (150, [100], 400),
    ])
    def test_get_price_calculates_correctly(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        for price in ingredient_prices:
            mock = Mock()
            mock.get_price.return_value = price
            burger.add_ingredient(mock)

        assert burger.get_price() == expected

    def test_get_price_without_bun_raises_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_price()

    # === GET_RECEIPT ===
    def test_get_receipt_returns_correct_format(self, bun, ingredient):
        burger = Burger()
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        expected = (
            "(==== Тестовая булочка ====)\n"
            "= sauce Тестовый соус =\n"
            "(==== Тестовая булочка ====)\n\n"
            "Price: 250"
        )
        assert burger.get_receipt() == expected


    def test_get_receipt_without_bun_raises_error(self):
        burger = Burger()
        with pytest.raises(AttributeError):
            burger.get_receipt()

