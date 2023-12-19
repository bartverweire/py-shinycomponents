from shiny import *

import re
import numpy as np

from ..utils import *

@module.ui
def help_ui(color="info", class_="", style="", icon_class="bi-question-circle-fill", nav_level=False, inline=True, align="right", size=6):
    style = None
    if nav_level:
        style = "margin-top: calc(var(--bs-body-line-height) * var(--bs-body-font-size) * -2); margin-bottom: calc(var(--bs-body-line-height) * var(--bs-body-font-size));"

    class_ += f" fs-{size}"
    if inline:
        class_ += " d-inline"

    if align == "left":
        class_ += " float-start"
    elif align == "right":
        class_ += " float-end"


    return ui.input_action_link(
        "show_help",
        ui.tags.span(
            class_=icon_class,
            style=f"color: var(--bs-{color}); background-color: transparent; ",
        ),
        class_=class_,
        style=style
    )


@module.server
def help_server(input, output, session, help_text, title=None, modal_size="l"):
    """
    Shows a help text. You need to prepare the layout of the help text yourself
    :param input: shiny input object (should not be explicitly specified)
    :param output: shiny output object (should not be explicitly specified)
    :param session: shiny session object (should not be explicitly specified)
    :param title for the help dialog
    :param help_text: help text to show
    :param modal_size: The size of the modal ("sm","m","l","xl")
    :return: a reactive value containing the list of selected items
    """
    @reactive.Effect
    @reactive.event(input.show_help)
    def show_help():
        """
        Show help for Info tab
        :return:
        """
        m = ui.modal(
            help_text,
            title=title,
            size=modal_size,
            easy_close=True
        )

        ui.modal_show(m)