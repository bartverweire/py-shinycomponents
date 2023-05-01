from shiny import ui, render
from shiny.module import resolve_id
from shiny.render import RenderUI

from ._utils import *

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


@overload
def render_progress(fn: Union[RenderUIFunc, RenderUIFuncAsync]) -> RenderUI:
    ...


@overload
def render_progress() -> Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]:
    ...


def render_progress(
    fn: Optional[Union[RenderUIFunc, RenderUIFuncAsync]] = None
) -> Union[RenderUI, Callable[[Union[RenderUIFunc, RenderUIFuncAsync]], RenderUI]]:
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

