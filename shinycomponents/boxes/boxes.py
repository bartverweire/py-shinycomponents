from shiny import *
from shiny.module import resolve_id

@module.ui
def output_value_box(width):
    return ui.output_ui(id="out_value_box", class_=f"col-sm-{width}")

@module.server
def render_value_box(input, output, session, value_box_data):
    @output
    @render.ui
    def out_value_box():
        vbdata = value_box_data()

        boxContent = ui.div(
            ui.div(
                ui.h3(vbdata["value"]),
                ui.p(vbdata["subtitle"]),
                ui.div(
                    ui.tags.i(
                        class_=f'inner-icon bi {vbdata["icon_class"]}'
                    ),
                    class_="icon"
                ),
                class_="inner"
            ),
            class_=f'small-box bg-{vbdata["color"]}'
        )

        if "href" in vbdata:
            boxContent = ui.a(
                boxContent,
                href=vbdata["href"]
            )

        return ui.div(
            boxContent,
            class_=f'col-sm-{vbdata["width"]}'
        )

