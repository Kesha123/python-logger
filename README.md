# Python Logger

Python Logger makes it easy to initialize a logger within the application scope. The Logger provides colorization and multiple ways to present and persist logs, including file and database storage. It allows you to set different logging levels for various handlers.

## Install
```
pip install git+https://github.com/Kesha123/python-logger.git@v<latest-release-tag-number>
```

## Available Handlers

| Handler | HandlerLevel Argument Name | Description |
|---|---|---|
| **Stream Handler** | stream | Terminal and command line output |
| **File Handler** | file | Persist logs in specified file |
| **MongoDB Handler** | mongodb | Persist logs in specified Mongo database |


## Use

In order to use certain handler, pass it as an argument to ```HandlerLevel```

```python
import logging
from python_logger.Logger import Logger
from python_logger.handlers import *

handlers = HandlerLevel(stream=StreamHandler(level=logging.DEBUG))
logger = Logger(handlers=handlers)
logger.debug("Hello World!")
```

### Logger
| Argument | Type | Description | Default Value | Available Values |
|---|---|---|---|---|
| handlers | HandlerLevel | Defines available handlers | ```HandlerLevel(stream = StreamHandler())``` |  |
| **colored_message** | bool | Message is colored (green, cyan, e.t.c) | True | <ul> <li>`True`</li> <li>`False`</li> </ul> |

### HandlerLevel
| Argument | Type | Default Value |
|---|---|---|
| **stream** | StreamHandler | None |
| **file** | FileHandler | None |
| **mongodb** | FileHandler | None |

### StreamHandler
| Argument | Type | Description | Default Value | Available Values |
|---|---|---|---|---|
| **level** | int | Logging level | DEBUG | <ul> <li>`logging.DEBUG`</li> <li>`logging.INFO`</li> <li>`logging.WARNING`</li> <li>`logging.ERROR`</li> <li>`logging.CRITICAL`</li> </ul> |

### FileHandler
| Argument | Type | Description | Default Value | Available Values |
|---|---|---|---|---|
| **file** | str | Files where logs are stored. | logs.log |  |
| **level** | int | Logging level | DEBUG | <ul> <li>`logging.DEBUG`</li> <li>`logging.INFO`</li> <li>`logging.WARNING`</li> <li>`logging.ERROR`</li> <li>`logging.CRITICAL`</li> </ul> |

### MongoDBHandler
| Argument | Type | Description | Default Value | Available Values |
|---|---|---|---|---|
| **level** | int | Logging level | DEBUG | <ul> <li>`logging.DEBUG`</li> <li>`logging.INFO`</li> <li>`logging.WARNING`</li> <li>`logging.ERROR`</li> <li>`logging.CRITICAL`</li> </ul> |
| **connection_string** | str | Mongo Database connection string | None |  |
| **database** | str | Mongo Database Name | None |  |
| **collection** | str | Mongo Database Collection Name | None |  |


## Color Scheme
| Level | Text Colored| Text |
|---|---|---|
| <span style="color:white; background-color:cyan; font-weight:bold;">DEBUG</span> | <span style="color:blue;">debug</span> | debug |
| <span style="color:white; background-color:green; font-weight:bold;">INFO</span>  | <span style="color:green;">info</span> | info |
| <span style="color:black; background-color:yellow; font-weight:bold;">WARNING</span>  | <span style="color:yellow;">warning</span> | warning |
| <span style="color:white; background-color:red; font-weight:bold;">ERROR</span> | <span style="color:red;">error</span> | error |
| <span style="color:white; background-color:red; font-weight:bold;">CRITICAL</span>  | critical | critical |

## Logging Levels
| Level | Code |
|---|---|
| **NOTSET** | 0 |
| **DEBUG** | 10 |
| **INFO** | 20 |
| **WARNING** | 30 |
| **ERROR** | 40 |
| **CRITICAL** | 50 |
