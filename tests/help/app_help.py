import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import App, render, ui, reactive
import shinycomponents.help as sch
from help_messages import *

app_ui = ui.page_fluid(
    ui.tags.link(
            rel="stylesheet",
            type="text/css",
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css"
    ),
    ui.navset_tab(
        ui.nav(
            "Tab a",
            ui.TagList(
                sch.help_ui("help_tab_a", color="primary", nav_level=True)
            ),
            sch.help_ui("help_tab_a_2", color="secondary", inline=True, size=3)
        ),
        ui.nav(
            "Tab b",
            ui.TagList(
                sch.help_ui("help_tab_b_left", color="success", nav_level=False, align="left", inline=True, size=4),
                sch.help_ui("help_tab_b_right", color="success", nav_level=False, inline=True, size=4)
            )
        ),
        ui.nav(
            "Tab c",
            ui.TagList(
                sch.help_ui("help_tab_c", color="danger", nav_level=False, inline=False, size=1)
            )
        )

    )
)


def server(input, output, session):
    sch.help_server("help_tab_a", ui.markdown(help_tab_a_text))
    sch.help_server("help_tab_a_2", ui.markdown(help_tab_a_2_text))
    sch.help_server("help_tab_b_left", ui.HTML(help_tab_b_text))
    sch.help_server("help_tab_b_right", ui.HTML(help_tab_b_text))
    sch.help_server("help_tab_c", ui.HTML(help_tab_c_text))


app = App(app_ui, server)
