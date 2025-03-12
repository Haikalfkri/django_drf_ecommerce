import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory()
        # Assert
        assert x.__str__() == "test_category"

class TestBrandModel:
    pass

class TestProductModel:
    pass