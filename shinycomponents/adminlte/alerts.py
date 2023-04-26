from shiny import ui
from shiny.module import resolve_id
from shiny.render import RenderUI

from htmltools import TagChildArg
from typing import overload, Awaitable, Callable, Optional, Union

from . import icons
import uuid

def output_alert(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")

def callout(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")



def alert(text, title=ui.markdown("&nbsp;"), icon=None, color="primary", dismissable=True, width=12):
    _alert = ui.div()

    _class = f'alert alert-{color} card'
    if dismissable:
        _class += " alert-dismissible"

        _alert.append(
            ui.tags.button(
                {
                    "data-lte-dismiss": "card-remove",
                    "aria-hidden": "true"
                },
                type="button",
                class_="btn-close"
            )
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


RenderAlertFunc = Callable[[], TagChildArg]
RenderAlertFuncAsync = Callable[[], Awaitable[TagChildArg]]

@overload
def render_alert(fn: Union[RenderAlertFunc, RenderAlertFuncAsync]) -> RenderUI:
    ...


@overload
def render_alert() -> Callable[[Union[RenderAlertFunc, RenderAlertFuncAsync]], RenderUI]:
    ...


def render_alert(
    fn: Optional[Union[RenderAlertFunc, RenderAlertFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderAlertFunc, RenderAlertFuncAsync]], RenderUI]]:
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


