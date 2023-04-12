from shiny import *
from htmltools import HTMLDependency


def busyindicator_deps() -> HTMLDependency:
    return HTMLDependency(
        name="busyindicator",
        version="0.0.1",
        source={"package": "shinycomponents", "subdir": ""},
        script=[
            {"src": "js/busy.js"}
        ],
        stylesheet={"href": "css/shinybusy.css"},
    )

def busyindicator():
    return ui.TagList(
        busyindicator_deps(),
        ui.div(
            class_="shinybusy-busy"
        )
    )

def busybar(centered=False, color="#112446", height="8px", type="auto"):
    classname="shinybusy-nanobar"
    if centered:
        classname="shinybusy-nanobar-centered"


    return ui.TagList(
        busyindicator_deps(),
        ui.tags.style(f".{classname} .bar {{background: {color} ; height: {height};}}"),
        ui.tags.script(
            f'{{"timeout":1000,"mode":"nanobar","classname":"{classname}","type":"{type}"}}',
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

async def update_busy_bar(value, session=session.get_current_session()):
    await session.send_custom_message(
        type="shinybusy-update-nanobar",
        message={
            "value": value
        }
    )
