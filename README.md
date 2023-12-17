# Powerful Python Logger

Power Python Logger allows you easily initialize loger within the application scope. Logger provides coloring and data persistance in file.

## Install
```
pip install git+https://github.com/Kesha123/python-logger.git@v3.0.0
```

## Use

```
logger = Logger()
logger.debug("Hellow World")
```

See `example.py` for more examples.

## Available Parameters
| Argument | Type | Description | Default Value |
|---|---|---|---|
| **file** | str | Files where logs are stored. | logs.log |
| **colored_message** | bool | Message is colored (green, cyan, e.t.c) | True |
| **warning_yellow** | bool  | Wrning default color is brown | False |

## Color Scheme
| Level | Text Colored| Text |
|---|---|---|
| <span style="color:white; background-color:cyan; font-weight:bold;">DEBUG</span> | <span style="color:blue;">debug</span> | debug |
| <span style="color:white; background-color:green; font-weight:bold;">INFO</span>  | <span style="color:green;">info</span> | info |
| <span style="color:black; background-color:yellow; font-weight:bold;">WARNING</span>  | <span style="color:yellow;">warning</span> | warning |
| <span style="color:white; background-color:red; font-weight:bold;">ERROR</span> | <span style="color:red;">error</span> | error |
| <span style="color:white; background-color:red; font-weight:bold;">CRITICAL</span>  | critical | critical |
