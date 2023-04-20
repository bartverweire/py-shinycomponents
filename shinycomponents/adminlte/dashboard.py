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
    *args: Any
) -> Tag:
    """
    Create an AdminLTE4 Dashboard Page

    Parameters
    ----------

    args
        UI elements.
    Returns
    -------
    A UI element.
    """
    page = TagList(*args)
    head = TagList(*adminlte_components())
    return tags.html(
        tags.head(head),
        tags.body(
            ui.div(
                page,
                class_="wrapper"
            ),
            class_="layout-fixed sidebar-open"
        )
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
                class_="navbar-nav"
            ),
            TagList(*args),
            class_="container-fluid"
        ),
        class_="main-header navbar navbar-expand navbar-light"
    )

def dashboardSidebar(title: Any, content: Union[TagList, TagChildArg]):
    return ui.tags.aside(
        ui.div(
            dashboardTitle(title) if type(title) == str else title,
            ui.a(
                ui.tags.i(
                    class_="fas fa-angle-double-left"
                ),
                {
                    "data-lte-toggle": "sidebar-mini"
                },
                href="javascript:;",
                class_="pushmenu mx-1",
                role="button"
            ),
            class_="brand-container"
        ),
        ui.div(
            ui.div(
                ui.div(
                    class_="os-resize-observer",
                    style="left: 0px; right: auto;"
                ),
                class_="os-resize-observer-host observed"
            ),
            ui.div(
                ui.div(
                    class_="os-resize-observer"
                ),
                class_="os-size-auto-observer observed",
                style="height: calc(100% + 1px); float: left;"
            ),
            ui.div(
                class_="os-content-glue",
                style="margin: -8px;"
            ),
            ui.div(
                ui.div(
                    ui.div(
                        content,
                        class_="os-content",
                        style="padding: 8px; height: 100%; width: 100%;"
                    ),
                    class_="os-viewport os-viewport-native-scrollbars-invisible"
                ),
                class_="os-padding"
            ),
            ui.div(
                ui.div(
                    ui.div(
                        class_="os-scrollbar-handle",
                        style="width: 100%; transform: translate(0px, 0px);"
                    ),
                    class_="os-scrollbar-track"
                ),
                class_="os-scrollbar os-scrollbar-horizontal os-scrollbar-unusable os-scrollbar-auto-hidden"
            ),
            ui.div(
                ui.div(
                    ui.div(
                        class_="os-scrollbar-handle",
                        style="height: 100%; transform: translate(0px, 0px);"
                    ),
                    class_="os-scrollbar-track"
                ),
                class_="os-scrollbar os-scrollbar-vertical os-scrollbar-unusable os-scrollbar-auto-hidden"
            ),
            class_="sidebar os-host os-theme-light os-host-resize-disabled os-host-scrollbar-horizontal-hidden os-host-transition os-host-scrollbar-vertical-hidden"
        ),  # End Sidebar div
        class_="main-sidebar sidebar-bg-dark sidebar-color-primary shadow"
    ),  # End Aside Sidebar

def dashboardBody(*args, header: Any):
    return ui.tags.main(
        dashboardContentHeader(header) if type(header) == str else header,
        TagList(*args),
        class_ = "content-wrapper"
    )


def dashboardTitle(title, href="#"):
    return ui.a(
        ui.span(
            title,
            class_="brand-text fw-light"
        ),
        href=href,
        class_="brand-link"
    )

def dashboardContentHeader(header: Union[TagList, TagChildArg]):
    return ui.div(
        ui.div(
            header,
            class_="container-fluid"
        ),
        class_="content-header"
    )
