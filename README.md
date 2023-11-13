## Example

```
from python_logger import Logger

class TestClassA:
    def __init__(self) -> None:
        self.logger = Logger.Logger()

    def test(self):
        self.logger.debug("test A")

class TestClassB:
    def __init__(self) -> None:
        self.logger = Logger.Logger()
    def test(self):
        self.logger.debug("test B")

a = TestClassA()
b = TestClassB()
a.test()
b.test()
```