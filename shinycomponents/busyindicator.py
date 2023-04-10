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
