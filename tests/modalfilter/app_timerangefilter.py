import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import App, render, ui, reactive, run_app
import shinycomponents.modalfilter as scmf
from datetime import datetime, timedelta

app_ui = ui.page_fluid(
    ui.h2("Shiny Timefilter demo"),
    scmf.timerangefilter_ui("cmp_timerange_hours", "Time Range - Hours", class_="col-sm-10"),
    scmf.timerangefilter_ui("cmp_timerange_minutes", "Time Range - Minutes", class_="col-sm-10"),
    scmf.timerangefilter_ui("cmp_timerange_minutes_noinit", "Time Range - Minutes", class_="col-sm-10"),

    ui.output_text_verbatim("out_selected_timerange_hours"),
    ui.output_text_verbatim("out_selected_timerange_minutes"),
    ui.output_text_verbatim("out_selected_timerange_minutes_noinit")
)


def server(input, output, session):
    dim_timerange = reactive.Value([datetime.now() - timedelta(days=2), datetime.now()])

    flt_timerange_hours = scmf.timerangefilter_server(
        "cmp_timerange_hours", dim_timerange,
        init_range=[datetime.now() - timedelta(days=1), datetime.now()],
        time_format="%d/%m %Hh",
        modal_title="Time Range (Hours)", modal_size="xl"
    )

    flt_timerange_minutes = scmf.timerangefilter_server(
        "cmp_timerange_minutes", dim_timerange,
        init_range=[datetime.now() - timedelta(days=1), datetime.now()],
        step=timedelta(minutes=1),
        granularity="minute",
        time_format="%d/%m %H:%M",
        modal_title="Time Range (Minutes)", modal_size="xl"
    )

    flt_timerange_minutes_noinit = scmf.timerangefilter_server(
        "cmp_timerange_minutes_noinit", dim_timerange,
        init_range=None,
        step=timedelta(minutes=5),
        granularity="minute",
        time_format="%d/%m %H:%M",
        modal_title="Time Range (Seconds)", modal_size="xl"
    )

    @output
    @render.text
    def out_selected_timerange_hours():
        return [x.strftime("%y-%m-%d %H:%M:%S") for x in flt_timerange_hours()]

    @output
    @render.text
    def out_selected_timerange_minutes():
        return [x.strftime("%y-%m-%d %H:%M:%S") for x in flt_timerange_minutes()]

    @output
    @render.text
    def out_selected_timerange_minutes_noinit():
        return [x.strftime("%y-%m-%d %H:%M:%S") for x in flt_timerange_minutes_noinit()]


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()