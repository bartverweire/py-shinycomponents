import sys

sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
import shinycomponents.adminlte as sca

app_ui = ui.page_fluid(
    sca.use_adminlte_components(),
    ui.h2("Progress Bars"),
    ui.row(
        ui.column(
            6,
            sca.progress(
                "Progress",
                value=80,
                unit="%"
            ),
            sca.progress(
                ui.tags.b("Progress"),
                value=80,
                max_value=160,
                unit="%",
                color="warning"
            )
        ),
        class_="mb-5"
    ),
    ui.h2("Reactive progress bars"),
    ui.row(
        ui.column(
            6,
            ui.input_slider(
                "in_progress_slider",
                "Just Slide!",
                min=0,
                max=150,
                step=5,
                value=20,
                animate=ui.AnimationOptions({"interval": 100, "loop": True}),
            ),
            sca.output_progress("out_progress_dynamic")
        ),
    ),
)

def server(input, output, session):

    @output
    @sca.render_progress
    def out_progress_dynamic():
        val = input.in_progress_slider()
        if val < 40:
            color="danger"
        elif val < 80:
            color="warning"
        elif val < 130:
            color="primary"
        else:
            color="success"

        return sca.progress(
            "Result from slider",
            value=val,
            color=color,
            max_value=150
        )





app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

