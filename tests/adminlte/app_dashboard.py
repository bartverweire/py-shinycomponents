import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
import shinycomponents as sc

app_ui = sc.page_dashboard(
    ui.div(
        ui.tags.nav(
            ui.div(
                ui.tags.ul(
                    ui.tags.li(
                        ui.tags.a(
                            ui.tags.i(
                                class_="fas fa-bars"
                            ),
                            {
                                "data-lte-toggle": "sidebar-full"
                            },
                            class_="nav-link",
                            href="#",
                            role="button",

                        ),
                        class_="nav-item"
                    ),
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
                ),
                class_="container-fluid"
            ),
            class_="main-header navbar navbar-expand navbar-light"
        ),
        # Aside Sidebar
        ui.tags.aside(
            # Brand Container
            ui.div(
                ui.a(
                    ui.span(
                        "Shinydashboard",
                        class_="brand-text fw-light"
                    ),
                    href="javascript:;",
                    class_="brand-link"
                ),
                ui.a(
                    ui.tags.i(
                        class_="fas fa-angle-double-left"
                    ),
                    {
                        "data-lte-toggle": "sidebar-mini"
                    },
                    href="javascript:;",
                    class_="pushmenu mx-1",
                    role="button"
                ),
                class_="brand-container"
            ),
            # End Brand Container
            # Sidebar div
            ui.div(
                ui.div(
                    ui.div(
                        class_="os-resize-observer",
                        style="left: 0px; right: auto;"
                    ),
                    class_="os-resize-observer-host observed"
                ),
                ui.div(
                    ui.div(
                        class_="os-resize-observer"
                    ),
                    class_="os-size-auto-observer observed",
                    style="height: calc(100% + 1px); float: left;"
                ),
                ui.div(
                    class_="os-content-glue",
                    style="margin: -8px;"
                ),
                ui.div(
                    ui.div(
                        ui.div(
                            ui.tags.nav(
                                ui.tags.ul(
                                    ui.tags.li(
                                        ui.a(
                                            ui.tags.i(
                                                class_="nav-icon fas fa-circle"
                                            ),
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
                                        "data-lte-toggle":"treeview",
                                        "data-accordion": "false"
                                    },
                                    role="menu",
                                    class_="nav nav-pills nav-sidebar flex-column"
                                ),
                                class_="mt-2"
                            ),
                            class_="os-content",
                            style="padding: 8px; height: 100%; width: 100%;"
                        ),
                        class_="os-viewport os-viewport-native-scrollbars-invisible"
                    ),
                    class_="os-padding"
                ),
                ui.div(
                    ui.div(
                        ui.div(
                            class_="os-scrollbar-handle",
                            style="width: 100%; transform: translate(0px, 0px);"
                        ),
                        class_="os-scrollbar-track"
                    ),
                    class_="os-scrollbar os-scrollbar-horizontal os-scrollbar-unusable os-scrollbar-auto-hidden"
                ),
                ui.div(
                    ui.div(
                        ui.div(
                            class_="os-scrollbar-handle",
                            style="height: 100%; transform: translate(0px, 0px);"
                        ),
                        class_="os-scrollbar-track"
                    ),
                    class_="os-scrollbar os-scrollbar-vertical os-scrollbar-unusable os-scrollbar-auto-hidden"
                ),
                class_="sidebar os-host os-theme-light os-host-resize-disabled os-host-scrollbar-horizontal-hidden os-host-transition os-host-scrollbar-vertical-hidden"
            ), # End Sidebar div
            class_="main-sidebar sidebar-bg-dark sidebar-color-primary shadow"
        ), # End Aside Sidebar
        ui.tags.main(
            # ui.div(
            #     ui.div(
            #         ui.div(
            #             ui.div(
            #                 ui.div(
            #                     "Dashboard",
            #                     class_="fs-3"
            #                 ),
            #                 class_="col-sm-6"
            #             ),
            #             class_="row mb-2"
            #         ),
            #         class_="content-fluid"
            #     ),
            #     class_="content-header"
            # ),
            # ui.div(
            #     ui.div(
            #         "Content",
            #         class_="container-fluid"
            #     ),
            #     class_="content"
            # ),
            class_="content-wrapper",
        ),
        ui.tags.footer(
            ui.div(
                "Anything you want",
                class_="float-end d-none d-sm-inline"
            ),
            class_="main-footer"
        ),
        class_="wrapper"
    )

)

def server(input, output, session):

    pass



app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
