from shiny import *
from shinycomponents import output_value_box, render_value_box
from htmltools import HTMLDependency

import time

app_ui = ui.page_fluid(
    ui.h2("Value Box Demo"),
    HTMLDependency(
        name="adminlte",
        version="v4",
        source={"package": "shinycomponents", "subdir": "www/boxes"},
        script=[
            {"src": "js/adminlte.min.js"}
        ],
        stylesheet={"href": "css/adminlte.min.css"},
    ),
    ui.tags.link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css"
    ),
    output_value_box("valuebox1", 4)
)

def server(input, output, session):
    value_box_data = reactive.Value({
        "value": 10,
        "color": "warning",
        "subtitle": "Subtitle",
        "icon_class": "bi-back",
        "width": 6
    })

    render_value_box("valuebox1", value_box_data)


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
