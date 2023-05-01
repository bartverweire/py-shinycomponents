import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)
from pathlib import Path

from shiny import *
import shinycomponents as sc
import shinycomponents.adminlte as sca

app_ui = sc.page_dashboard(
    sc.dashboardHeader(
        ui.TagList(
            sca.menuItem("id_content1_tab", "Tab1", "id_content1", selected=True),
            sca.menuItem("id_content2_tab", "Tab2", "id_content2")
        )
    ),
    sc.dashboardSidebar(
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
    sc.dashboardBody(
        ui.div(
            ui.div(
                "Tab 1 Content",
                id="id_content1",
                class_="tab-pane",
                role="tabpanel"
            ),
            ui.div(
                "Tab 2 Content",
                id="id_content2",
                class_="tab-pane",
                role="tabpanel"
            ),
            class_="tab-content",
            role="tablist"
        ),
        header=sc.dashboardContentHeader(
            ui.row(
                ui.column(
                    6,
                    ui.div(
                        "Dashboard v1",
                        class_="fs-3"
                    )
                ),
                ui.column(
                    6,
                    ui.tags.ol(
                        ui.tags.li(
                            ui.a(
                                "Home",
                                href="#"
                            ),
                            class_="breadcrumb-item"
                        ),
                        ui.tags.li(
                            "index",
                            class_="breadcrumb-item"
                        ),
                        class_="breadcrumb float-sm-end"
                    )
                ),
                class_="mb-2"
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

