from shiny import *
from htmltools import HTMLDependency


def busyindicator_deps() -> HTMLDependency:
    return HTMLDependency(
        name="busyindicator",
        version="0.0.1",
        source={"package": "shinycomponents", "subdir": "www/busyindicator"},
        script=[
            {"src": "js/busy.js"}
        ],
        stylesheet={"href": "css/shinybusy.css"},
    )

def busybar(timeout=1000, centered=False, color="#112446", height="8px", type="auto"):
    classname="shinybusy-nanobar"
    if centered:
        classname="shinybusy-nanobar-centered"


    return ui.TagList(
        busyindicator_deps(),
        ui.tags.style(f".{classname} .bar {{background: {color} ; height: {height};}}"),
        ui.tags.script(
            f'{{"timeout":{timeout},"mode":"nanobar","classname":"{classname}","type":"{type}"}}',
            {
                "type":"application/json",
                "data-for": "shinybusy"
            },
            _add_ws=False
        ),
        ui.div(
            class_="shinybusy-busy"
        )
    )

def busygif(src, timeout=100, type="auto", position="top-right", height="50px", width="50px", margins=["10px", "10px"], overlay_color="rgba(0, 0, 0, 0.5)", overlay_css=None):
    style_templates = {
        "top-right": f"top:{margins[0]}; right: {margins[1]}; height: {height}; width: {width};",
        "top-left": f"top:{margins[0]}; left: {margins[1]}; height: {height}; width: {width};",
        "bottom-right": f"bottom:{margins[0]}; right: {margins[1]}; height: {height}; width: {width};",
        "bottom-left": f"bottom:{margins[0]}; left: {margins[1]}; height: {height}; width: {width};",
        "full-page": f"top: 0; bottom: 0; right: 0; left: 0; margin: auto;",
        "free": "height: {height}; width: {width};"
    }
    img_class = "freezeframe freezeframe-responsive shinybusy-freezeframe"
    gif_tag = ui.div(
            ui.img(
                src=src,
                class_=img_class
            ),
            style=style_templates[position],
            class_="shinybusy"
        )

    if position == "full-page":
        img_class += "shinybusy-full-page"
        gif_tag = ui.div(
            gif_tag,
            style=f"background-color: {overlay_color};",
            class_="shinybusy shinybusy-overlay"
        )

    return ui.TagList(
        busyindicator_deps(),
        ui.tags.script(
            f'{{"timeout":{timeout},"mode":"gif","position":"{position}","type":"{type}"}}',
            {
                "type": "application/json",
                "data-for": "shinybusy"
            },
            _add_ws=False
        ),
        gif_tag
    )

async def update_busy_bar(value, session=session.get_current_session()):
    await session.send_custom_message(
        type="shinybusy-update-nanobar",
        message={
            "value": value
        }
    )

async def play_gif(session=session.get_current_session()):
    await session.send_custom_message(
        type="shinybusy-play-gif",
        message={
            "value": "play"
        }
    )

async def stop_gif(session=session.get_current_session()):
    await session.send_custom_message(
        type="shinybusy-stop-gif",
        message={
            "value": "stop"
        }
    )