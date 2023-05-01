import sys
sys.path.insert(0, ".")
sys.path.insert(0, "../..")
print(sys.path)
from pathlib import Path

from typing import List

from shiny import *
from shiny.types import NavSetArg
from shiny.ui import h4


def nav_controls(prefix: str) -> List[NavSetArg]:
    return [
        ui.nav("a", prefix + ": tab a content"),
        ui.nav("b", prefix + ": tab b content"),
        ui.nav_control(
            ui.a(
                "Shiny",
                href="https://github.com/rstudio/shiny",
                target="_blank",
            )
        ),
        ui.nav_spacer(),
        ui.nav_menu(
            "Other links",
            ui.nav("c", prefix + ": tab c content"),
            "----",
            "Plain text",
            "----",
            ui.nav_control(
                ui.a(
                    "RStudio",
                    href="https://rstudio.com",
                    target="_blank",
                )
            ),
            align="right",
        ),
    ]


app_ui = ui.page_navbar(
    *nav_controls("page_navbar"),
    title="page_navbar()",
    bg="#0062cc",
    inverse=True,
    id="navbar_id",
    footer=ui.div(
        {"style": "width:80%;margin: 0 auto"},
        ui.tags.style(
            """
            h4 {
                margin-top: 3em;
            }
            """
        ),
        h4("Bootstrap tabs"),
        ui.a("Bootstrap static tabs", href="html/bootstrap_tabs.html"),
        h4("navset_tab()"),
        ui.navset_tab(*nav_controls("navset_tab()")),
        h4("navset_pill()"),
        ui.navset_pill(*nav_controls("navset_pill()")),
        h4("navset_tab_card()"),
        ui.navset_tab_card(*nav_controls("navset_tab_card()")),
        h4("navset_pill_card()"),
        ui.navset_pill_card(*nav_controls("navset_pill_card()")),
        h4("navset_pill_list()"),
        ui.navset_pill_list(*nav_controls("navset_pill_list()")),
    )
)


def server(input: Inputs, output: Outputs, session: Session):
    @reactive.Effect
    def _():
        print("Current navbar page: ", input.navbar_id())


app = App(app_ui, server, static_assets=Path.joinpath(Path(__file__).parent.parent.parent, "assets"))