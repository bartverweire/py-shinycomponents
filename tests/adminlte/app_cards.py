import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from shiny import *
from shinywidgets import *
import shinycomponents.adminlte as sca

app_ui = ui.page_fluid(
    sca.use_adminlte_components(),
    ui.h2("Cards Demo"),
    ui.p("Note, cards are called 'boxes' in shinydashboard for R"),
    ui.h4("Static Cards"),
    ui.row(
        ui.column(
            3,
            sca.card(
                "Simple Text",
                title="Expandable",
                color="primary",
                collapsable=True
            )
        ),
        ui.column(
            3,
            sca.card(
                ui.markdown(
                    """
                    # Hello World
            
                    This is **markdown** and here is some `code`:
            
                    ```python
                    print('Hello world!')
                    ```
                    """
                ),
                title="Multi",
                color="success",
                collapsable=True,
                removable=True,
                maximizable=True
            )
        ),
        ui.column(
            3,
            sca.card(
                ui.output_plot("out_plot"),
                title="Removable",
                color="warning",
                removable=True,
                maximizable=True
            )
        ),
        ui.column(
            3,
            sca.card(
                output_widget("out_plotly"),
                title="Maximizable",
                color="danger",
                maximizable=True
            )
        )
    ),
    ui.h4("Outline Cards"),
    ui.row(
        ui.column(
            3,
            sca.card(
                "Simple Text",
                title="Outline",
                color="primary",
                collapsable=True,
                outline=True
            )
        )
    ),
    ui.h4("Dynamic Cards"),
    ui.row(
        ui.column(
            3,
            sca.output_card("card1")
        ),
        ui.column(
            3,
            sca.output_card("card2")
        ),
        ui.column(
            3,
            sca.output_card("card3")
        ),
        ui.column(
            3,
            sca.output_card("card4")
        )
    )

)

def server(input, output, session):

    @output
    @sca.render_card
    def card1():
        return sca.card(
            title="Expandable",
            dynamic=True,
            collapsable=True
        )

    @output
    @sca.render_card
    def card2():
        return sca.card(
            title="Multi",
            color="success",
            dynamic=True,
            collapsable=True,
            removable=True,
            maximizable=True
        )

    @output
    @sca.render_card
    def card3():
        return sca.card(
            title="Removable",
            color="warning",
            dynamic=True,
            removable=True
        )

    @output
    @sca.render_card
    def card4():
        return sca.card(
            title="Maximizable",
            color="danger",
            dynamic=True,
            maximizable=True
        )

    @output
    @render.plot
    def out_plot():
        np.random.seed(19680801)
        x_rand = 100 + 15 * np.random.randn(437)
        fig, ax = plt.subplots()
        ax.hist(x_rand, 50, density=True)
        return fig

    @output
    @render_widget
    def out_plotly():
        df = px.data.tips()
        fig = go.FigureWidget(px.histogram(df, x="total_bill"))
        return fig



app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

