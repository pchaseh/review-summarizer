from abc import ABC, abstractmethod


class ReviewQuerier(ABC):
    @abstractmethod
    def reviews(self, name: str) -> list[str]:
        """Fetch reviews for a product

        Args:
            name (str): The product name to query

        Returns:
            list[str]: RA list of reviews for the product
        """
        pass
