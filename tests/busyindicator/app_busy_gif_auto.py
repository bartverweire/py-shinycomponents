import os, sys
from pathlib import Path, PureWindowsPath
sys.path.append(str(PureWindowsPath(Path(__file__).parent.parent.parent)))
print(sys.path)

from shiny import *
from shinycomponents import busygif

import time

app_ui = ui.page_fluid(
    busygif(src="https://jeroen.github.io/images/banana.gif",
            height="70px", width="70px"),
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_action_button("calculate", label="Long Calculation"),
)


def server(input, output, session):
    @output
    @render.text
    def txt():
        input.calculate()
        time.sleep(5)
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
