from shiny import *
from datetime import date, datetime, timedelta
from datetime_truncate import truncate

import logging
logger = logging.getLogger(__name__)

from ..utils import *

@module.ui
def timerangefilter_ui(button_text, button_color="primary", width="100%", class_="me-2"):
    if not validate_color(button_color):
        button_color = "primary"

    button_class = f"btn-{button_color} {class_}"

    return ui.div(
        ui.input_action_button("in_show_modal", button_text, class_=button_class, width=width),
        class_="d-flex flex-row align-items-center my-3 col-sm-11"
    )


@module.server
def timerangefilter_server(input, output, session,
                           snapshot_range,
                           init_range=[datetime.now() - timedelta(days=1), datetime.now()],
                           step=timedelta(hours=1),
                           granularity="hour",
                           time_format="%d-%H:00",
                           width="800px",
                           modal_title=None, modal_size="l"):
    """
    The server part of a modal filter component.
    This function creates the reactive components that open a filter modal when the ui button is clicked.

    :param input: shiny input object (should not be explicitly specified)
    :param output: shiny output object (should not be explicitly specified)
    :param session: shiny session object (should not be explicitly specified)
    :param snapshot_range: range of allowed times
    :param init_range : initial selected range
    :param modal_title: The title of the modal
    :param modal_size: The size of the modal ("sm","m","l","xl")
    :return: a reactive value containing the list of selected items
    """
    selected_timerange = reactive.Value([truncate(item, granularity) for item in init_range])

    @reactive.Calc
    def normalized_snapshot_range():
        return [truncate(item, granularity) for item in snapshot_range()]


    @reactive.Effect
    @reactive.event(input.in_show_modal)
    def open_timerangefilter():
        req(normalized_snapshot_range())

        m = ui.modal(
            ui.panel_well(
                ui.row(
                    ui.column(2,
                              ui.h5("Min time"),
                              ui.output_text("out_start_time"),
                              style="text-align: center"
                              ),
                    ui.column(8,
                              ui.input_slider(id="in_timerange",
                                              label="Time Range",
                                              min=normalized_snapshot_range()[0],
                                              max=normalized_snapshot_range()[1],
                                              step=step,
                                              time_format=time_format,
                                              value=[selected_timerange()[0], selected_timerange()[1]],
                                              width=width,
                                              drag_range=True
                                              )
                              ),
                    ui.column(2,
                              ui.h5("Max time"),
                              ui.output_text("out_end_time"),
                              style="text-align: center"
                              ),
                ),
            ),
            title=modal_title,
            size=modal_size,
            easy_close=True,
            footer=ui.row(
                ui.column(6,
                          ui.input_action_button("in_apply", "Apply", class_="btn-success mr-1")
                          ),
                ui.column(6,
                          ui.modal_button("Cancel", class_="btn-warning")
                          )

            )
        )

        ui.modal_show(m)

    @reactive.Effect
    def update_timerange_input():
        req(normalized_snapshot_range())

        min_snapshot_time = normalized_snapshot_range()[0]
        max_snapshot_time = normalized_snapshot_range()[1]

        ui.update_slider("in_timerange",
                         min=min_snapshot_time,
                         max=max_snapshot_time,
                         time_format="%d-%H:00")

        if not selected_timerange():
            selected_timerange.set([min_snapshot_time, max_snapshot_time])



    @output
    @render.text
    def out_start_time():
        logger.debug("Start time changed {} ({})".format(input.in_timerange()[0], type(input.in_timerange()[0])))

        if granularity == "hour":
            return selected_timerange()[0].strftime("%Y-%m-%d %Hh")

        if granularity == "minute":
            return selected_timerange()[0].strftime("%Y-%m-%d %H:%M")

        return selected_timerange()[0].strftime("%Y-%m-%d %H:%M:%S")

    @output
    @render.text
    def out_end_time():
        logger.debug("End time changed {} ({})".format(input.in_timerange()[0], type(input.in_timerange()[0])))

        if granularity == "hour":
            return selected_timerange()[1].strftime("%Y-%m-%d %Hh")

        if granularity == "minute":
            return selected_timerange()[1].strftime("%Y-%m-%d %H:%M")

        return selected_timerange()[1].strftime("%Y-%m-%d %H:%M:%S")

    @reactive.Effect
    @reactive.event(input.in_apply)
    def update_selected_items():
        ui.modal_remove(session)

    @reactive.Effect
    def update_selected_timerange():
        logger.debug("Updating selected timerange to {}".format(input.in_timerange()))
        timerange = [t + (datetime.now() - datetime.utcnow()) for t in input.in_timerange()]
        selected_timerange.set(timerange)

    return selected_timerange