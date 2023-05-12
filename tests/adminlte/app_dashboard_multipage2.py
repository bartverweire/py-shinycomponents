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
            sca.menuItem("id_content1_tab", "Tab1", "id_content1"),
            sca.menuItem("id_content2_tab", "Tab2", "id_content2")
        ),
        sca.menuItemList(
            sca.menuItem("id_right_tab", "Tab3", "id_content3")
        ),
        title = "Shiny Dashboard",
    ),
    sca.dashboardBody(
        sca.dashboardContentHeader(
            ui.row(
                ui.column(
                    6,
                    ui.div(
                        "Dashboard v1",
                        class_="fs-3"
                    )
                ),
                class_="mb-2"
            )
        ),
        sca.dashboardTabContainer(
            sca.tabItem(
                "id_content1",
                sca.dashboardSidebar(
                    content=ui.tags.nav(
                        ui.tags.ul(
                            ui.tags.li(
                                ui.a(
                                    ui.tags.i(
                                        class_="nav-icon far fa-circle"
                                    ),
                                    ui.p(
                                        "Tab1 Element"
                                    ),
                                    href="#",
                                    class_="nav-link active"
                                ),
                                class_="nav-item"
                            ),
                            data_lte_toggle="treeview",
                            data_accordion="false",
                            role="menu",
                            class_="nav nav-pills nav-sidebar flex-column"
                        ),
                        class_="mt-2"
                    )
                ),
                "Tab 1 Content",
                selected=False
            ),
            sca.tabItem(
                "id_content2",
                sca.dashboardSidebar(
                    content=ui.tags.nav(
                        ui.tags.ul(
                            ui.tags.li(
                                ui.a(
                                    ui.tags.i(
                                        class_="nav-icon far fa-circle"
                                    ),
                                    ui.p(
                                        "Tab2 Element"
                                    ),

                                    href="#",
                                    class_="nav-link active"
                                ),
                                class_="nav-item"
                            ),
                            ui.tags.li(
                                ui.input_text("in_text", "Some input", width="100%"),
                            ),
                            data_lte_toggle="treeview",
                            data_accordion="false",
                            role="menu",
                            class_="nav nav-pills nav-sidebar flex-column"
                        ),
                        class_="mt-2"
                    )
                ),
                "Tab 2 Content",
                selected=True
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

