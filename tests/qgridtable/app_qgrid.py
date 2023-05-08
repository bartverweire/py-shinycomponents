import sys

sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
from shinywidgets import *
import pandas as pd

import shinycomponents.qgridtable as scq

app_ui = ui.page_fluid(
    scq.qgridtable_ui("qgrid_table")
)


def server(input, output, session):
    df = reactive.Value(pd.DataFrame({"x": [1, 2, 3, 4], "y": ["Apple","Banana","Pear","Lemon"]}))
    scq.qgridtable_server("qgrid_table", df)


app = App(app_ui, server)
