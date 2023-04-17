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

    page = TagList(*bootstrap_deps(), *adminlte_components(), *args)
    head = tags.title(title) if title else None
    return tags.html(
        tags.head(head),
        tags.body(
            page,
            class_="layout-fixed sidebar-open"
        ),
        lang=lang
    )