from shiny import *
from datetime import date, datetime, timedelta

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
                           modal_title=None, modal_size="l"):
    """
    The server part of a modal filter component.
    This function creates the reactive components that open a filter modal when the ui button is clicked.
    The modal consists of an include filter, an exclude filter, a group of checkboxes, and buttons to apply or cancel

    :param input: shiny input object (should not be explicitly specified)
    :param output: shiny output object (should not be explicitly specified)
    :param session: shiny session object (should not be explicitly specified)
    :param item_type: Item type, displayed above the checkboxes
    :param items: Reactive value containing the list of items to choose from
    :param init_selection: The initial list of selected items, if any
    :param modal_title: The title of the modal
    :param modal_size: The size of the modal ("sm","m","l","xl")
    :return: a reactive value containing the list of selected items
    """
    selected_timerange = reactive.Value(init_range)

    # @reactive.Effect
    # def init_selected_timerange():
    #     selected_timerange.set([snapshot_range()[0], snapshot_range()[1]])

    @reactive.Effect
    @reactive.event(input.in_show_modal)
    def open_timerangefilter():
        req(snapshot_range())

        m = ui.modal(
            ui.panel_well(
                ui.row(
                    ui.column(1,
                              ui.h5("Min time"),
                              ui.output_text("out_start_time"),
                              style="text-align: center"
                              ),
                    ui.column(10,
                              ui.input_slider(id="in_timerange",
                                              label="Time Range",
                                              min=snapshot_range()[0],
                                              max=snapshot_range()[1],
                                              step=timedelta(hours=1),
                                              time_format="%d-%H:00",
                                              value=[selected_timerange()[0], selected_timerange()[1]],
                                              width="800px",
                                              drag_range=True
                                              )
                              ),
                    ui.column(1,
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
        req(snapshot_range())

        min_snapshot_time = snapshot_range()[0]
        max_snapshot_time = snapshot_range()[1]

        ui.update_slider("in_timerange",
                         min=min_snapshot_time,
                         max=max_snapshot_time,
                         time_format="%d-%H:00")

    @output
    @render.text
    def out_start_time():
        logger.debug("Start time changed {} ({})".format(input.in_timerange()[0], type(input.in_timerange()[0])))
        return input.in_timerange()[0].strftime("%Y-%m-%d %H:00")

    @output
    @render.text
    def out_end_time():
        return input.in_timerange()[1].strftime("%Y-%m-%d %H:00")

    @reactive.Effect
    @reactive.event(input.in_apply)
    def update_selected_items():
        ui.modal_remove(session)

    @reactive.Effect
    def update_selected_timerange():
        logger.debug("Updating selected timerange to {}".format(input.in_timerange()))
        selected_timerange.set(input.in_timerange())

    return selected_timerange