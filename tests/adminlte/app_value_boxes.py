import sys
sys.path.insert(0, "../..")

from shiny import *
from shinycomponents import *

app_ui = ui.page_fluid(
    use_adminlte_components(),
    ui.h2("Value Boxes Demo"),
    ui.h4("Value boxes (Small boxes)"),
    ui.row(
        ui.column(
            3,
            output_value_box("valuebox1")
        ),
        ui.column(
            3,
            output_value_box("valuebox2")
        ),
        ui.column(
            3,
            output_value_box("valuebox3")
        ),
        ui.column(
            3,
            output_value_box("valuebox4")
        )
    ),
    ui.h4("Value boxes with limited info"),
    ui.row(
        ui.column(
            6,
            output_value_box("valuebox5")
        ),
        ui.column(
            6,
            output_value_box("valuebox6")
        )
    )
)

def server(input, output, session):

    @output
    @render_value_box
    def valuebox1():
        return value_box(
            value=150,
            unit="",
            subtitle="New Orders",
            color="primary",
            icon="ion-bag",
            href="http://www.google.be",
            href_text="More info",
            target="blank_"
        )


    @output
    @render_value_box
    def valuebox2():
        return value_box(
            value=53,
            unit="%",
            subtitle="Bounce Rate",
            color="green",
            icon="ion-stats-bars",
            href="http://www.google.be",
            href_text="More info",
            target="blank_"
        )

    @output
    @render_value_box
    def valuebox3():
        return value_box(
            value=44,
            unit="",
            subtitle="User Registrations",
            color="warning",
            icon="ion-person-add",
            href="http://www.google.be",
            href_text="More info",
            target="blank_"
        )


    @output
    @render_value_box
    def valuebox4():
        return value_box(
            value=65,
            subtitle="Unique Visitors",
            color="danger",
            icon="ion-pie-graph",
            href="http://www.google.be",
            href_text="More info",
            target="blank_"
        )

    @output
    @render_value_box
    def valuebox5():
        return value_box(
            value="50",
        )

    @output
    @render_value_box
    def valuebox6():
        return value_box(
            value="50",
            href="#"
        )


    @output
    @render_value_box
    def valuebox7():
        return value_box(
            value=65,
            href="http://www.google.be"
        )


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

