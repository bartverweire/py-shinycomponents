import sys
sys.path.insert(0, ".")
sys.path.insert(0, "../..")
print(sys.path)
from pathlib import Path

from typing import List

from shiny import *
from shiny.types import NavSetArg
from shiny.ui import h4

import shinycomponents.adminlte as sca

app_ui = ui.page_navbar(
    ui.nav("a", "tab a content"),
    ui.nav("b", "tab b content"),
    ui.nav_menu(
        "Other links",
        ui.nav("c", "tab c content"),
        "----",
        ui.nav("d", "tab d content"),
        align="left",
    ),
    title="page_navbar()",
    bg="#0062cc",
    inverse=True,
    id="navbar_id",
    header=sca.setup.adminlte_components(),
    footer=ui.div(
        {"style": "width:80%;margin: 0 auto"},
        ui.tags.style(
            """
            h4 {
                margin-top: 3em;
            }
            """
        ),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Effect
    def _():
        print("Current navbar page: ", input.navbar_id())


app = App(app_ui, server, static_assets=Path.joinpath(Path(__file__).parent.parent.parent, "assets"))