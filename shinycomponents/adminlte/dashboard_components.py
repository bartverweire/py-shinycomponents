import sys
from typing import Any, Optional, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

# Tagifiable isn't used directly in this file, but it seems to necessary to import
# it somewhere for Sphinx to work cleanly.
from htmltools import Tagifiable  # pyright: ignore[reportUnusedImport] # noqa: F401
from htmltools import Tag, TagChildArg, TagList, div, tags
from shiny import *

from .icons import icon

def dropdownMenu():
    pass

def menuItem(id: str, title: str, icon: icon, children: list):
    if children is not None and len(children) > 0:
        child_items = ui.tags.ul()
        for item in children:
            child_items.append(
                ui.tags.li(
                    item
                )
            )
    return ui.a(
        icon,
        ui.p(
            title,
            ui.tags.i(
                class_="end fas fa-angle-right"
            ),
        ),
        href="javascript:;",
        class_="nav-link active"
    ),

