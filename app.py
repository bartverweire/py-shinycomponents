from shiny import App, render, ui
from shinycomponents.busyindicator import *

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    busyindicator_deps(),
    ui.div(
        class_="shinybusy-busy"
    )
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

app = App(app_ui, server)
