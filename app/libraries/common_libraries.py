"""
Author: Saurabh Singh
"""
import importlib

class LoadModule():
    """Load Module"""
    def __init__(self, product, version) -> None:
        self.product = product
        self.version = version

    def load_module(self):
        """Load dynamic module"""
        module = importlib.import_module(
            f'app.services.{self.product}.{self.version}.{self.product}')
        my_class = getattr(module, self.product.capitalize())
        return my_class
