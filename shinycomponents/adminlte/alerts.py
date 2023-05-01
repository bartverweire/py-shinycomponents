from shiny import ui, render
from shiny.module import resolve_id
from shiny.render import RenderUI

from htmltools import TagChildArg
from typing import overload, Awaitable, Callable, Optional, Union

from ._utils import *

from . import icons
import uuid

def output_alert(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")

def output_callout(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")



def alert(text, title=ui.markdown("&nbsp;"), icon=None, color="primary", dismissable=True, dynamic=False):
    _alert = ui.div()

    _class = f'alert alert-{color} card'
    if dismissable:
        _class += " alert-dismissible"

        btn_id = str(uuid.uuid4())
        btn = ui.tags.button(
            {
                "data-lte-dismiss": "card-remove",
                "aria-hidden": "true"
            },
            id=btn_id,
            type="button",
            class_="btn-close"
        )

        if dynamic:
            btn.append(
                ui.tags.script(
                    # current script tag is the last
                    f"""
                        var btn = document.getElementById('{btn_id}'); 
                        btn.addEventListener('click', event => {{
                            event.preventDefault();
                            const target = event.target;
                            const data = new adminlte.CardWidget(target, adminlte.Default);
                            data.remove();
                        }});
                    """
                ),
            )
        _alert.append(
            btn
        )

    _alert.add_class(_class)

    _title = ui.h5()
    if icon is not None:
        _icon = icons.icon(icon) if type(icon) == str else icon
        _icon.add_class("me-2")
        _title.append(_icon)

    _title.append(title)

    _alert.append(
        _title,
        text
    )

    return _alert


@overload
def render_alert(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_alert() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_alert(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
    """
    Reactively render Alert.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_alert
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


@overload
def render_callout(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_callout() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_callout(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
    """
    Reactively render Alert.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_alert
    """
    return render.ui(fn)