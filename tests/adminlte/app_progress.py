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
        )
    ),
)

def server(input, output, session):
    pass





app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

