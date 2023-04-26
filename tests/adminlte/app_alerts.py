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
from shinycomponents import *
import shinycomponents.adminlte as sca

app_ui = ui.page_fluid(
    sca.use_adminlte_components(),
    ui.h2("Alerts Demo"),
    ui.row(
        ui.column(
            6,
            sca.alert(
                "Info alert preview. This alert is dismissable",
                title="Alert!",
                color="info",
                icon=sca.icon("fa-info")
            ),
            sca.alert(
                "Warning alert preview. This alert is dismissable",
                title="Alert!",
                color="warning",
                icon="fa-exclamation-triangle"
            ),
            sca.alert(
                "Success alert preview. This alert is dismissable",
                title="Alert!",
                color="success",
                icon="fa-check"
            ),
            sca.alert(
                "Danger alert preview. This alert is dismissable",
                title="Alert!",
                color="danger",
                icon="fa-check"
            )
        ),
        ui.column(
            6,
            value_box(
                value=150,
                unit="",
                subtitle="New Orders",
                color="primary",
                icon="ion-bag",
                href="http://www.google.be",
                href_text="More info",
                target="blank_"
            )
        )
    ),
)

def server(input, output, session):
    pass
    # @output
    # @render_card
    # def card1():
    #     return card(
    #         title="Expandable",
    #         dynamic=True,
    #         collapsable=True
    #     )





app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

