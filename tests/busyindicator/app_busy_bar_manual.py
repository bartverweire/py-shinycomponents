from shiny import App, ui
import sys
from shinycomponents.busyindicator.busyindicator import *

import time

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_action_button("calculate", label="Long Calculation"),
    busybar(color="#FF0000", type="manual")
)


def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.calculate)
    async def start_busy_bar():
        await update_busy_bar(0, session)
        for i in range(10):
            print(f"Waiting step {i} ")
            time.sleep(1)
            await update_busy_bar((i + 1) * 10, session)

    # @output
    # @render.text
    # def txt():
    #     input.calculate()
    #     time.sleep(5)
    #     return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
