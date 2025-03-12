class TestCategoryEndpoints:
    endpoint = "api/category/"

    def test_category_get(self, category_factory):
        category_factory()
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

class TestBrandEndpoints:
    pass

class TestProductEndpoints:
    pass