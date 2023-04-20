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
from shiny.ui._html_dependencies import bootstrap_deps

from .setup import adminlte_components

def page_dashboard(
    *args: Any, title: Optional[str] = None, lang: Optional[str] = None
) -> Tag:
    """
    Create an AdminLTE4 Dashboard Page

    Parameters
    ----------

    args
        UI elements.
    title
        The browser window title (defaults to the host URL of the page). Can also be set as
        a side effect via :func:`~shiny.ui.panel_title`.
    lang
        ISO 639-1 language code for the HTML page, such as ``"en"`` or ``"ko"``. This will
        be used as the lang in the ``<html>`` tag, as in ``<html lang="en">``. The default,
        `None`, results in an empty string.

    Returns
    -------
    A UI element.

    See Also
    -------
    :func:`~shiny.ui.page_fluid`
    :func:`~shiny.ui.page_navbar`
    """

    page = TagList(*args)
    head = TagList(*adminlte_components(), tags.title(title) if title else None)
    # head = tags.title(title) if title else None
    return tags.html(
        tags.head(head),
        tags.body(
            page,
            class_="layout-fixed sidebar-open"
        ),
        lang=lang
    )

def dashboardHeader(*args: Any,
                    width: Optional[str] = "250px"):
    return ui.tags.nav(
            ui.div(
                ui.tags.ul(
                    ui.tags.li(
                        ui.tags.a(
                            ui.tags.i(
                                class_="fas fa-bars"
                            ),
                            {
                                "data-lte-toggle": "sidebar-full"
                            },
                            class_="nav-link",
                            href="#",
                            role="button",

                        ),
                        class_="nav-item"
                    ),
                    ui.tags.li(
                        ui.tags.a(
                            "Home",
                            href="#",
                            class_="nav-link"
                        ),
                        class_="nav-item d-none d-md-block"
                    ),
                    ui.tags.li(
                        ui.tags.a(
                            "Contact",
                            href="#",
                            class_="nav-link"
                        ),
                        class_="nav-item d-none d-md-block"
                    ),
                    class_="navbar-nav"
                ),
                class_="container-fluid"
            ),
            class_="main-header navbar navbar-expand navbar-light"
        )

def dashboardSidebar():
    pass

def dashboardBody():
    pass

