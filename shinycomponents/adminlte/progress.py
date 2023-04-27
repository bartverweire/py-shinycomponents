from shiny import ui, render
from shiny.module import resolve_id
from shiny.render import RenderUI

from htmltools import TagChildArg
from typing import overload, Awaitable, Callable, Optional, Union

from . import icons
import uuid

def output_progress(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")

def progress(title=ui.markdown("&nbsp;"), value: Union[int, float] = 50, unit: Optional[str] = "", max_value: Union[int, float] = None, color: str = "primary"):
    value_text = ui.tags.b(str(value))
    if max_value is not None:
        value_text.append("/", max_value)
    if unit is not None:
        value_text.append(unit)

    value_pct = value if max_value is None else int(100 * value / max_value)

    cmp = ui.div(
        title,
        ui.span(
            value_text,
            class_="float-end"
        ),
        ui.div(
            ui.div(
                class_=f"progress-bar bg-{color}",
                style=f"width: {value_pct}%;"
            ),
            class_="progress progress-sm"
        ),
        class_="progress-group"
    )

    return cmp


RenderProgressFunc = Callable[[], TagChildArg]
RenderProgressFuncAsync = Callable[[], Awaitable[TagChildArg]]

@overload
def render_progress(fn: Union[RenderProgressFunc, RenderProgressFuncAsync]) -> RenderUI:
    ...


@overload
def render_progress() -> Callable[[Union[RenderProgressFunc, RenderProgressFuncAsync]], RenderUI]:
    ...


def render_progress(
    fn: Optional[Union[RenderProgressFunc, RenderProgressFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderProgressFunc, RenderProgressFuncAsync]], RenderUI]]:
    """
    Reactively render Progress.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_progress
    """
    return render.ui(fn)

def callout(text, title=ui.markdown("&nbsp;"), icon=None, color="primary", dismissable=True, width=12):
    _callout = ui.div(

        class_=f'callout callout-{color}'
    )

    _title = ui.h5()
    if icon is not None:
        _icon = icons.icon(icon) if type(icon) == str else icon
        _icon.add_class("me-2")
        _title.append(_icon)

    _title.append(title)

    _callout.append(
        _title,
        text
    )

    return _callout


RenderCalloutFunc = Callable[[], TagChildArg]
RenderCalloutFuncAsync = Callable[[], Awaitable[TagChildArg]]

@overload
def render_callout(fn: Union[RenderCalloutFunc, RenderCalloutFuncAsync]) -> RenderUI:
    ...


@overload
def render_callout() -> Callable[[Union[RenderCalloutFunc, RenderCalloutFuncAsync]], RenderUI]:
    ...


def render_callout(
    fn: Optional[Union[RenderCalloutFunc, RenderCalloutFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderCalloutFunc, RenderCalloutFuncAsync]], RenderUI]]:
    """
    Reactively render Progress.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_progress
    """
    return render.ui(fn)