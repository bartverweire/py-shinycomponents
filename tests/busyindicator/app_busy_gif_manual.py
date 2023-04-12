import os, sys
from pathlib import Path, PureWindowsPath
sys.path.append(str(PureWindowsPath(Path(__file__).parent.parent.parent)))
print(sys.path)

from shiny import *
from shinycomponents import *

import time

app_ui = ui.page_fluid(
    busygif(src="https://jeroen.github.io/images/banana.gif",
            height="70px", width="70px",
            type="manual"),
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.input_action_button("play", label="Play"),
    ui.input_action_button("stop", label="Stop"),
)


def server(input, output, session):
    @reactive.Effect
    @reactive.event(input.play)
    async def play():
        await play_gif(session)

    @reactive.Effect
    @reactive.event(input.stop)
    async def stop():
        await stop_gif(session)


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()
