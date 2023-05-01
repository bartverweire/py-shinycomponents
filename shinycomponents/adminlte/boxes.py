from shiny.module import resolve_id
from shiny.render import RenderUI

from htmltools import TagChildArg
from typing import overload, Awaitable, Callable, Optional, Union

from ._utils import *

from shinycomponents.adminlte.icons import *
import uuid

def output_info_box(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")

def output_value_box(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")

def output_card(id, width=12):
    return ui.output_ui(resolve_id(id), class_=f"col-sm-{width}")


def value_box(value, unit="", subtitle=ui.markdown("&nbsp;"), icon=None, color="primary", href=None, href_text="", target="blank_", width=12):
    boxContent = ui.div(
        ui.div(
            ui.h3(
                value,
                ui.tags.sup(unit, class_="fs-5")
            ),
            ui.p(subtitle),
            ui.div(
                ui.tags.i(
                    class_=f'inner-icon {build_icon_class(icon)}'
                ),
                class_="icon"
            ),
            class_="inner"
        ),
        class_=f'small-box bg-{color}'
    )

    if href is not None:
        boxContent.append(
            ui.a(
                href_text,
                ui.tags.i(
                    class_="fas fa-arrow-circle-right ms-1"
                ),
                href=href,
                target=target,
                class_="small-box-footer"
            )
        )

    return ui.div(
        boxContent,
        class_=f'col-sm-{width}'
    )

def info_box(value, unit, title="Title", icon="fa-cog", color="primary", bg_color=False, progress=None, width=12):
    boxContent = ui.div(
        ui.span(
            title,
            class_="info-box-text"
        ),
        ui.span(
            value,
            ui.tags.small(unit),
            class_="info-box-number"
        ),
        class_="info-box-content "
    )

    if progress is not None and type(progress) == int and progress >= 0 and progress <= 100:
        boxContent.append(
            ui.div(
                ui.div(
                    class_="progress-bar",
                    style=f"width: {progress}%;"
                ),
                class_="progress"
            )
        )

    box = ui.div(
        ui.span(
            ui.tags.i(
                class_=build_icon_class(icon)
            ),
            class_="info-box-icon shadow-sm " + (f"bg-{color}" if not bg_color else "")
        ),
        boxContent,
        class_="info-box " + (f"bg-{color}" if bg_color else "")
    )

    return ui.div(
        box,
        class_=f'col-sm-{width}'
    )

card_tools = {
    "collapse": {
        "icon": "fa-minus",
        "property": "data-lte-toggle",
        "command": "card-collapse",
        "js-command": "toggle()"
    },
    "remove": {
        "icon": "fa-times",
        "property": "data-lte-dismiss",
        "command": "card-remove",
        "js-command": "remove()"
    },
    "maximize": {
        "icon": "fa-expand",
        "property": "data-lte-toggle",
        "command": "card-maximize",
        "js-command": "toggleMaximize()"
    }
}

def card_tool(tool, dynamic):
    if dynamic:
        btn_id = str(uuid.uuid4())

        btn = ui.tags.button(
            ui.tags.i(
                class_=build_icon_class(card_tools[tool]["icon"])
            ),
            {
                card_tools[tool]["property"]: card_tools[tool]["command"]
            },
            id=btn_id,
            type="button",
            class_="btn btn-tool"
        )

        btn.append(
            ui.tags.script(
                # current script tag is the last
                f"""
                    var btn = document.getElementById('{btn_id}'); 
                    btn.addEventListener('click', event => {{
                        event.preventDefault();
                        const target = event.target;
                        const data = new adminlte.CardWidget(target, adminlte.Default);
                        data.{card_tools[tool]["js-command"]};
                    }});
                """
            ),
        )
    else:
        btn = ui.tags.button(
            ui.tags.i(
                class_=build_icon_class(card_tools[tool]["icon"])
            ),
            {
                card_tools[tool]["property"]: card_tools[tool]["command"]
            },
            type="button",
            class_="btn btn-tool"
        )

    return btn

def card(*args, title="Title", color="primary", collapsable=False, maximizable=False, removable=False, dynamic=False, outline=False):
    tools = []
    if collapsable:
        tools.append(card_tool("collapse", dynamic))

    if removable:
        tools.append(card_tool("remove", dynamic))

    if maximizable:
        tools.append(card_tool("maximize", dynamic))

    card_class = f"card card-{color}"
    if outline:
         card_class += " card-outline"

    header = ui.div(
        ui.h3(
            title,
            class_="card-title"
        ),
        ui.div(
            *tools,
            class_="card-tools"
        ),
        class_="card-header"
    )

    content = ui.div(
        *args,
        class_="card-body",
        style="box-sizing: border-box; display: block;"
    )

    return ui.div(
        header,
        content,
        class_=card_class
    )

@overload
def render_card(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_card() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_card(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
    """
    Reactively render Card.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_info_box
    """
    return render.ui(fn)




@overload
def render_info_box(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_info_box() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_info_box(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
    """
    Reactively render info Box.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_info_box
    """
    return render.ui(fn)


@overload
def render_value_box(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_value_box() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_value_box(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
    """
    Reactively render Value Box.
    This is just a wrapper around render.ui

    Returns
    -------
    The result of a call to render.ui

    See Also
    --------
    ~shinycomponents.output_value_box
    """
    return render.ui(fn)


