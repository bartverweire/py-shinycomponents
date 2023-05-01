from htmltools import TagChildArg
from typing import overload, Awaitable, Callable, Optional, Union

RenderUIFunc = Callable[[], TagChildArg]
RenderUIFuncAsync = Callable[[], Awaitable[TagChildArg]]

