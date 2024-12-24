from review_summarizer.query.review_querier import ReviewQuerier

import requests
import json


class BestBuyCAReviewQuerier(ReviewQuerier):
    def __init__(self) -> None:
        self.base_url = "https://www.bestbuy.ca/api"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0"
        }

    def find_product(self, name: str) -> dict[str, any]:
        """Find a product by its name

        Args:
            name (str): The product name

        Returns:
            dict[str, any]: The product found
        """

        params = {
            "query": name,
            "lang": "en-CA",
            "hasConsent": True,
            "sortBy": "relevance",
            "sortDir": "desc",
        }
        url = f"{self.base_url}/v2/json/search"
        resp = requests.get(url, params=params, headers=self.headers)
        products = resp.json()["products"]
        # Assume that the first result is the best
        return products[0]

    def paginated(
        self,
        items_key: str,
        url: str,
        headers: dict[str, any] = {},
        params: dict[str, any] = {},
    ) -> list[any]:
        """Make a request to a paginated URL and fetch all items

        Args:
            items_key (str): The field name containing the items in each paginated response
            url (str): Request URL to use
            headers (dict[str, any], optional): Request headers to use. Defaults to {}.
            params (dict[str, any], optional): Request parameters to send. Defaults to {}.

        Returns:
            list[any]: A list of results
        """

        first_page = requests.get(url, params=params, headers=headers).json()
        items = first_page[items_key]

        total_pages = first_page["totalPages"]

        for page in range(1, total_pages + 1):
            params["page"] = page
            next_page = requests.get(url, params=params, headers=headers).json()
            items.extend(next_page[items_key])

        return items

    def reviews(self, name: str) -> list[str]:
        product = self.find_product(name)
        product_id = product["sku"]
        params = {
            "source": "all",
            "lang": "en-CA",
            "sortBy": "relevancy",
        }
        url = f"{self.base_url}/reviews/v2/products/{product_id}/reviews"
        reviews = self.paginated("reviews", url, params=params, headers=self.headers)
        return [review["comment"] for review in reviews if "comment" in review]
