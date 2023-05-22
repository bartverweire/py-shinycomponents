import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
from shinycomponents import busybar, update_busy_bar

import time

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_action_button("calculate", label="Long Calculation"),
    busybar(color="#FF0000", type="auto")
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
