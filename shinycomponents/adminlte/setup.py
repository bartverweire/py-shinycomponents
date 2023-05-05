from shiny import ui
from htmltools import HTMLDependency, TagList
from typing import List

def use_adminlte_components():
    return ui.div(
        TagList(*adminlte_components())
        # HTMLDependency(
        #     name="adminlte",
        #     version="v4",
        #     source={"package": "shinycomponents", "subdir": "www/adminlte"},
        #     script=[
        #         {"src": "js/adminlte.js"}
        #     ],
        #     stylesheet=[{"href": "css/adminlte.min.css"}, {"href": "css/callout.css"}],
        # ),
        # ui.tags.link(
        #     rel="stylesheet",
        #     href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css"
        # ),
        # ui.tags.link(
        #     rel="stylesheet",
        #     href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css"
        # ),
        # ui.tags.link(
        #     rel="stylesheet",
        #     href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/all.min.css"
        # )
    )

def adminlte_components() -> List[HTMLDependency]:
    return [
        HTMLDependency(
            name="adminlte",
            version="v4",
            source={"package": "shinycomponents", "subdir": "www/adminlte"},
            script=[
                {"src": "js/adminlte.js"}
            ],
            stylesheet=[{"href": "css/adminlte.min.css"}, {"href": "css/callout.css"}, {"href": "css/adminlte-mods.css"}],
        ),
        ui.tags.link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css"
        ),
        ui.tags.link(
            rel="stylesheet",
            href="https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css"
        ),
        ui.tags.link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/all.min.css"
        ),
        ui.tags.link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/overlayscrollbars@1.13.1/css/OverlayScrollbars.min.css"
        ),
        ui.tags.script(
            src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js",
            crossorigin="anonymous"
        )
    ]