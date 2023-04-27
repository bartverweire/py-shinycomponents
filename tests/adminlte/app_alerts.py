import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
import shinycomponents.adminlte as sca

app_ui = ui.page_fluid(
    sca.use_adminlte_components(),
    ui.h2("Alerts & Callouts Demo"),
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
            sca.output_alert("out_alert_success"),
            sca.output_alert("out_alert_danger"),

        ),
        ui.column(
            6,
            sca.callout(
                "There is a problem that we need to fix. A wonderful serenity has taken possession of my entire soul, like these sweet mornings of spring which I enjoy with my whole heart.",
                title="I am a danger callout!",
                color="danger",
                icon="fa-ban"
            ),
            sca.callout(
                "Some informational text",
                title="I am an info callout!",
                color="info",
                icon="fa-info"
            ),
            sca.output_callout("out_callout_warning"),
            sca.output_callout("out_callout_success")
        )
    ),
)

def server(input, output, session):
    pass

    @output
    @sca.render_alert
    def out_alert_success():
        return sca.alert(
            "Success alert preview. This alert is dismissable",
            title="Alert!",
            color="success",
            icon="fa-check",
            dynamic=True
        )

    @output
    @sca.render_alert
    def out_alert_danger():
        return sca.alert(
            "Danger alert preview. This alert is dismissable",
            title="Alert!",
            color="danger",
            icon="fa-check",
            dynamic=True
        )

    @output
    @sca.render_callout
    def out_callout_warning():
        return sca.callout(
            "This is a yellow callout",
            title="I am a warning callout!",
            color="warning",
            icon="fa-exclamation-triangle"
        )

    @output
    @sca.render_callout
    def out_callout_success():
        return sca.callout(
            "This is a green callout",
            title=ui.TagList(sca.icons.icon("fa-check", "me-2"), "I am a success callout!"),
            color="success"
        )





app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

