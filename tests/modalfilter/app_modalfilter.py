import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import App, render, ui, reactive
import shinycomponents.modalfilter as scmf

app_ui = ui.page_fluid(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css"
    ),
    ui.h2("Shiny Modalfilter demo"),
    scmf.modalfilter_ui("mf_fruit", "Fruit", button_color="danger", clear_button_color="indigo"),
    ui.output_text_verbatim("out_selected_fruit"),
    scmf.modalfilter_ui("mf_music", "Music Instruments", clear_button_color="warning"),
    ui.output_text_verbatim("out_selected_instruments")
)


def server(input, output, session):
    selected_fruit = scmf.modalfilter_server("mf_fruit", "Fruit", reactive.Value(["Apple","Banana","Pear","Orange"]), init_selection=["Banana","Pear"])
    selected_instruments = scmf.modalfilter_server("mf_music", "Instruments", reactive.Value(["Piano","Guitar","Drums","Oboe","Dulcimer"]), init_selection=["Guitar","Dulcimer"])

    @output
    @render.text
    def out_selected_fruit():
        return selected_fruit()

    @output
    @render.text
    def out_selected_instruments():
        return selected_instruments()


app = App(app_ui, server)
