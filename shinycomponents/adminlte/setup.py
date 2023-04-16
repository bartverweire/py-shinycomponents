from shiny import ui
from htmltools import HTMLDependency

def use_adminlte_components():
    return ui.div(
        HTMLDependency(
            name="adminlte",
            version="v4",
            source={"package": "shinycomponents", "subdir": "www/adminlte"},
            script=[
                {"src": "js/adminlte.js"}
            ],
            stylesheet={"href": "css/adminlte.min.css"},
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
        )
    )