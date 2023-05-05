import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
import shinycomponents as sc

app_ui = sc.page_dashboard(
    sc.dashboardHeader(
        ui.TagList(
            sca.menuItem("id_content1_tab", "Tab1", "id_content1"),
            sca.menuItem("id_content2_tab", "Tab2", "id_content2")
        ),
        ui.tags.ul(
            ui.tags.li(
                ui.tags.a(
                    "Home",
                    href="#",
                    class_="nav-link"
                ),
                class_="nav-item d-none d-md-block"
            ),
            ui.tags.li(
                ui.tags.a(
                    "Contact",
                    href="#",
                    class_="nav-link"
                ),
                class_="nav-item d-none d-md-block"
            ),
            class_="navbar-nav"
        ),
        ui.tags.ul(
            ui.tags.li(
                ui.a(
                    ui.tags.i(
                        class_="far fa-bell"
                    ),
                    ui.span(
                        3,
                        class_="navbar-badge badge bg-danger"
                    ),
                    {
                        "data-bs-toggle": "dropdown"
                    },
                    href="#",
                    class_="nav-link"
                ),
                ui.div(
                    ui.span(
                        "15 Notifications",
                        class_="dropdown-item dropdown-header"
                    ),
                    ui.div(
                        class_="dropdown-divider"
                    ),
                    ui.a(
                        ui.tags.i(
                            class_="fas fa-envelope me-2"
                        ),
                        "4 new messages",
                        ui.span(
                            "3 mins",
                            class_="float-end text-muted fs-7"
                        ),
                        href="#",
                        class_="dropdown-item"
                    ),
                    ui.div(
                        class_="dropdown-divider"
                    ),
                    ui.a(
                        ui.tags.i(
                            class_="fas fa-users me-2"
                        ),
                        "8 friend requests",
                        ui.span(
                            "12 hours",
                            class_="float-end text-muted fs-7"
                        ),
                        href="#",
                        class_="dropdown-item"
                    ),
                    class_="dropdown-menu dropdown-menu-lg dropdown-menu-end"
                ),
                class_="nav-item dropdown"
            ),
            class_="navbar-nav ms-auto"
        )
    ),
    sc.dashboardSidebar(
        title="Shinydashboard",
        content=ui.tags.nav(
            ui.tags.ul(
                ui.tags.li(
                    ui.a(
                        sc.icon("fa-circle", "nav-icon"),
                        ui.p(
                            "Dashboard",
                            ui.tags.i(
                                class_="end fas fa-angle-right"
                            ),
                        ),
                        href="javascript:;",
                        class_="nav-link active"
                    ),
                    ui.tags.ul(
                        ui.tags.li(
                            ui.a(
                                ui.tags.i(
                                    class_="nav-icon far fa-circle"
                                ),
                                ui.p(
                                    "Dashboard v1"
                                ),
                                href="./index.html",
                                class_="nav-link active"
                            ),
                            class_="nav-item"
                        ),
                        ui.tags.li(
                            ui.a(
                                ui.tags.i(
                                    class_="nav-icon far fa-circle"
                                ),
                                ui.p(
                                    "Dashboard v2"
                                ),
                                href="./index2.html",
                                class_="nav-link"
                            ),
                            class_="nav-item"
                        ),
                        ui.tags.li(
                            ui.a(
                                ui.tags.i(
                                    class_="nav-icon far fa-circle"
                                ),
                                ui.p(
                                    "Dashboard v3"
                                ),
                                href="./index3.html",
                                class_="nav-link"
                            ),
                            class_="nav-item"
                        ),
                        class_="nav nav-treeview"
                    ),
                    class_="nav-item menu-open"
                ),
                ui.tags.li(
                    ui.a(
                        ui.tags.i(
                            class_="nav-icon fas fa-circle"
                        ),
                        ui.p(
                            "Widgets",
                            ui.tags.i(
                                class_="end fas fa-angle-right"
                            ),
                        ),
                        href="javascript:;",
                        class_="nav-link"
                    ),
                    ui.tags.ul(
                        ui.tags.li(
                            ui.a(
                                ui.tags.i(
                                    class_="nav-icon far fa-circle"
                                ),
                                ui.p(
                                    "Small Box"
                                ),
                                href="./pages/widgets/small-box.html",
                                class_="nav-link"
                            ),
                            class_="nav-item"
                        ),
                        class_="nav nav-treeview"
                    ),
                    class_="nav-item"
                ),
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
                "Content",
                class_="container-fluid"
            ),
            class_="content"
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



app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

