Example
-------

.. code-block:: python

from python_logger import Logger

class TestClass:
    def __init__(self) -> None:
        self.logger = Logger.Logger(class_name=self.__class__.__name__)

    def test(self):
        self.logger.debug("test")

a = TestClass()
a.test()