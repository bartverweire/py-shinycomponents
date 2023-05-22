import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)
from pathlib import Path

from shiny import *
import shinycomponents as sc
import shinycomponents.adminlte as sca

app_ui = sca.page_dashboard(
    sca.dashboardHeader(
        ui.TagList(
            sca.menuItem("id_content1_tab", "Tab1", "id_content1", selected=True),
            sca.menuItem("id_content2_tab", "Tab2", "id_content2")
        )
    ),
    sca.dashboardSidebar(
        title="Shinydashboard",
        content=ui.tags.nav(
            ui.tags.ul(
                {
                    "data-lte-toggle": "treeview",
                    "data-accordion": "false"
                },
                role="menu",
                class_="nav nav-pills nav-sidebar flex-column"
            ),
            class_="mt-2"
        )
    ),
    sca.dashboardBody(
        sca.dashboardTabContainer(
            sca.tabItem(
                "id_content1",
                "Tab 1 Content",
                selected=True
            ),
            sca.tabItem(
                "id_content2",
                "Tab 2 Content"
            )
        )
    )
)

def server(input, output, session):

    pass



app = App(app_ui, server, static_assets=Path.joinpath(Path(__file__).parent.parent.parent, "assets"))

def main():
    run_app(app)

if __name__ == "__main__":
    main()

