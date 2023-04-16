import sys
sys.path.insert(0, "../..")

from shiny import *
from shinycomponents import *

app_ui = ui.page_fluid(
    use_adminlte_components(),
    ui.h2("Info Boxes Demo"),
    ui.h4("Info Boxes"),
    ui.row(
        ui.column(
            3,
            output_info_box("infobox1")
        ),
        ui.column(
            3,
            output_info_box("infobox2")
        ),
        ui.column(
            3,
            output_info_box("infobox3")
        ),
        ui.column(
            3,
            output_info_box("infobox4")
        )
    ),
    ui.h4("Info boxes with background"),
    ui.row(
        ui.column(
            3,
            output_info_box("infobox5")
        ),
        ui.column(
            3,
            output_info_box("infobox6")
        ),
        ui.column(
            3,
            output_info_box("infobox7")
        ),
        ui.column(
            3,
            output_info_box("infobox8")
        )
    ),
)

def server(input, output, session):

    @output
    @render_info_box
    def infobox1():
        return info_box(
            value="10",
            unit="%",
            title="CPU Traffic",
            color="primary",
            icon="fa-cog"
        )

    @output
    @render_info_box
    def infobox2():
        return info_box(
            value="760",
            unit="",
            title="Sales",
            color="success",
            icon="fa-shopping-cart"
        )

    @output
    @render_info_box
    def infobox3():
        return info_box(
            value="2,000",
            unit="",
            title="New Members",
            color="warning",
            icon="fa-users"
        )

    @output
    @render_info_box
    def infobox4():
        return info_box(
            value="41,410",
            unit="",
            title="Likes",
            color="danger",
            icon="fa-thumbs-up"
        )

    @output
    @render_info_box
    def infobox5():
        return info_box(
            value="41,410",
            unit="%",
            title="Bookmarks",
            color="primary",
            bg_color=True,
            icon="fa-bookmark"
        )

    @output
    @render_info_box
    def infobox6():
        return info_box(
            value="41,410",
            unit="",
            title="Likes",
            color="success",
            bg_color=True,
            icon="fa-thumbs-up"
        )

    @output
    @render_info_box
    def infobox7():
        return info_box(
            value="41,410",
            unit="",
            title="Events",
            color="warning",
            bg_color=True,
            progress=40,
            icon="fa-calendar-alt"
        )

    @output
    @render_info_box
    def infobox8():
        return info_box(
            value="41,410",
            unit="",
            title="Comments",
            color="danger",
            bg_color=True,
            progress=90,
            icon="fa-comments"
        )

app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

