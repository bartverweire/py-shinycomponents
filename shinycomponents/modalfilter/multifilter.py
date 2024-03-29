from shiny import *
from shiny.module import current_namespace, resolve_id
import pandas as pd

import logging

logFormatter = logging.Formatter("'%(asctime)s - %(name)s - %(levelname)s - %(message)s'")
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(consoleHandler)

from ..utils import *

filter_types = ["==", "<=", "<", ">", ">=", "contains", "in", "in (comma separated)"]
default_filter = dict(key="Username", type="==", value=None)

# See https://shinylive.io/py/editor/#code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACAZwAsaJs2B3KGUIcAOhABmjYjBYcyMADZlixBWxZ0GzFoTZsxYydPZceG+k1YBBdHhYxiAEwCuCuHcZwohMjQBu7iyeEI5wjHbONAbQ6AD6kSwAvCyRWFAA5nCx4jQAHnCOABRiLKUsICJEClB6lYgslTDYALQArJUAvnglZZzcvAJCHBhkHHDwGDDcZNiFAJTdEGUpNGkQcAqxvmRuxWAAyqbYLAAqTsQAsgBqAMKVCz2lqdXYxM5ksWw0oQBGUIzFJbLMqpVBQdabL6-f6A4FwlYYbiod5bOC5Mh7ZSOYixJEoijoyp2SpElioaqEOAcVShRiJSpnbEsAlke6LeHA1J4j7eXykWI-d7KCB7KCORykypWcXM4jNbFsx7Ah5AuGg8EbWIwKDcWEckGrN5kZEfFl7Qhuf4FLY1ADW+jAKv1Bowjn8hW+9LAZDtDrsbBmbi92sY6W4zWUqHqAAYMK1xorVcr2WUVXNomJQuJ2GEAgDuXYjSb-XA9DRSHNEEqchAaJxrT62PakkEvD5-HAMFcoApnHBCtH00nG7bYiRnOQwi3PLyO12e32B0OlQABIvvVfBWkjNGspNZnSWzyOG1NtjzKtJ5aeMjORhLcSVABi3DrY0czN99RANbfDd98wdCSECbm2vgBBgACi4jiHAPigbOEFwAE5AehAJoYGKjhDssB5YReSrLOOk6MC2I5jm8JEYJkGJzCwADULAAIyEWU5HERQjAYGwcAYhxYQ4fC3wtpU5GVAx7BkAC-GMIJaqrNwPHMPENB6s6PFuD4TBegAxCOfqsXCfBjJ4Xo-HA4hMHAkEhEShmcjQiTkZEHrYSmcLLleZS-pwZF2p8uZhK5dgsok3IjOcuLofiu7zJ5HI6SwAAiFmvhA6QsFALDrAGBStohcAsBZsE+CwCg0LahWjHW9g0OkcgsLBGyZSwPw0Kw4gTmYgqsO1ADk6ijHA9mJSQjCeKVYJkJxSzcMyXDqIQNSdiwADqhVWvl7bpbK82FQABj5HD7SNRUoawfDtaYe0sPtWH7YexBsHegRsMQ2Wlr4O1DVt4GFcVcFkPoXmlIl8DgoNHCCCwfCFdiEB9awUMBLtfBMIwxxQD8Ro6KQ4jldtGWXaMp1HWdlBA41UgyMQQ2kSORVuPA5BsBg9krjO7YQdBJV7hyHNgXOyEU4UR1ycCB7tWEghZDJBEg8CR3-me3G8aLr71ie+nUWrdGMUx8XwqkzioI4MuouimKRdyFusvgLB+AucBevcGYQIlFxOK4pa7Vm3BVWMQTEHwwPRCuDguG4GCRJmFmfk2Kny9evF3ksqTrh8LmVD1wqxFIfCuyBRfh17UdKXmsfZuR5dBQWLAZyWZakCFu6VtWGvvtOgsQd2vb9k+PY8YbpRru8JqgSEYTR1E+5xzn-L50n8Lz0syQAHKkMNCs0NmStFG3CvLCvLZctFPLtvyK-mkekpgDcN-2xaNRsLEZlkBAzQCPe3DpIXHIbDxS8zpSjH2SKfE0sRZyXyFKQPYR1b4vlrJwUkT89Cv2zu-eUFkoCuDtsPYEN5U4IkXvZZYqQSC9hgCKAALHYFeTpgHkNUM4KhhQAAcLd0QMOdKgl+wYyDNAAMxkiEa1JgtJMrlXSB-KWMA2DNEpCROyh9eiBmdroc8LJYihDGoIcsEAvTlXWBGDgUhnD1XEjvRqHcCjzEZjxFgG91jcOVNEZYAsCpQRgoDBCXNOzC1QuFMWSoDxHVPLaJecI96qwxCcRgfZ8EeL8V43mvi-oYACRicKFovCyRCXHHJ-xwmRIchgTwDgAiJw0oDbSj4wBuj8DpEAPEm4QAwBAc8fUV552Dn1OYQFHRuPhIlfY3BKStgqVkBIpAFDHHKcQAIkNCoAAkTgXAADI3U5n9Iq3ifDqEugoBQrVCpjAUBKBWiU5rwAcBjFIEA3B6D2tgPqngiq5HJDQQg7VZksFCAGKQ2ACgYFOAtDQbAEasCym1X+ly-leGOeZJazgHFDReW8vMxw2DaiOXQ94GgyADRYOkFQH5lCHi8EsIaMgTZswVmEkcrpPqAvmPZQpjBwlMoBcQWY+DEoACUU7f2+oHIJHdWowKpe9H6YJgisDYCQVAG0jnB3UCipUiVyXbN2u1DQVLA6yoprjSc6JdqVTgKgZkjBvC2nrlXQOEAWHmVIsQR8SZRrSHJLxPK2sNUatBTVGqWUSVODJIIGaJzkUON1dqSqSz7Cl0KrcwqmR1jWoUHS5YiUTiBzYLAJNiadDghOSkHiH4fjHDdN4uVmV0AEz0aQA5XBhD2CgNgf1TIq2wRrdVdKTbKA3QZjVEg9A3AUEcJmsohD7x6owvAouYg0CWuSDYVAhQl0qRLIwPMcwwBdHANAeA1BPAAEdIjlIpqzMg6J8BEFIBQKgyA+g8H4IIYQe6AC6QA
# for a better way

@module.ui
def multifilter_ui(button_text, button_color="primary", width="100%", class_="me-2"):
    if not validate_color(button_color):
        button_color = "primary"

    button_class = f"btn-{button_color} {class_}"

    return ui.TagList(
        ui.div(
            ui.input_action_button("in_show_modal", button_text, class_=button_class, width=width),
            class_="d-flex flex-row align-items-center my-3 col-sm-11"
        )
    )


@module.server
def multifilter_server(input, output, session,
                       df_in,
                       init_filters=[],
                       auto_apply_filter=True,
                       modal_title=None,
                       modal_size="xl",
                       max_filters=10):
    """
    Multifilter server part

    :param input: shiny input object (should not be explicitly specified)
    :param output: shiny output object (should not be explicitly specified)
    :param session: shiny session object (should not be explicitly specified)
    :param df_in: input dataframe
    :param init_filters: initial filter values
    :param modal_title: The title of the modal
    :param modal_size: The size of the modal ("sm","m","l","xl")
    :max_filters: maximum number of filters
    :return: a reactive value containing the list of selected items
    """
    df_keys = reactive.Value([])
    df_filtered = reactive.Value(pd.DataFrame())

    modal_opened = reactive.Value(None)
    rows_to_shows = reactive.Value(1)

    # check if init_filters is a list
    if type(init_filters) != list:
        init_filters = []

    # adjust init_filters list : slice in case it's too long, or pad with the default filter, up to max_filters
    init_filters = init_filters[:max_filters] + [default_filter for i in range(max_filters - len(init_filters))]
    df_filters = reactive.Value(init_filters)

    filter_components = reactive.Value([filter_server(f"flt_{i}", df_keys, df_in, modal_opened, init_filters[i]) for i in range(max_filters)])

    @reactive.Effect
    def initialize_filtered_data():
        df_filtered.set(df_in())

    @reactive.Effect
    def update_columns():
        df_keys.set(df_in().columns.sort_values().tolist())



    @reactive.Effect
    @reactive.event(input.in_show_modal)
    def open_multifilter():
        # req(normalized_snapshot_range())

        logger.debug("Opening multifilter modal")

        with reactive.isolate():
            current_filters = df_filters()

        m = ui.modal(
            ui.output_ui("out_multifilter_modal"),
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

        modal_opened.set(1)

        ui.modal_show(m)


    @render.ui
    def out_multifilter_modal():
        req(modal_opened())

        with reactive.isolate():
            return ui.TagList(
                [ui.panel_conditional(
                    f"parseInt(input['hidden_max_filter_index']) >= {i}",
                    filter_ui(f"flt_{i}")
                ) for i in range(max_filters)],
                ui.row(
                    ui.input_text("hidden_max_filter_index", "Max filter index", value=rows_to_shows()),
                    class_="d-none"
                ),
                ui.output_text("out_hidden_max_filter_index"),
            )


    @reactive.Effect
    def update_max_filter_index():
        req(modal_opened())

        max_i = 1

        with reactive.isolate():
            fcs = filter_components()

        for i, cs in enumerate(fcs):
            if cs() is not None and type(cs()) == dict and (cs().get("value") or cs().get("values")):
                max_i = i + 1;

        logger.debug(f"Updating max filter index to {max_i}")

        rows_to_shows.set(max_i)
        ui.update_text("hidden_max_filter_index", value=max_i)


    @reactive.Effect
    @reactive.event(input.in_apply)
    def update_close_modal():
        """
        Closes the multifilter modal and applies the filter
        """
        filters = []
        with reactive.isolate():
            fcs = filter_components()

        for fc in fcs:
            filters.append(fc())

        df_filters.set(filters)
        ui.modal_remove(session)

        modal_opened.set(None)

        if auto_apply_filter:
            df = multifilter_apply(df_in().copy(), filters)


            # for i, filter in enumerate(filters):
            #     if filter is not None and type(filter) == dict:
            #         filter_key = filter.get("key")
            #         filter_type = filter.get("type")
            #
            #         if filter_type == "in":
            #             filter_values = filter.get("values")
            #
            #             if filter_values:
            #                 df = df[df[filter_key].isin(filter_values)].copy()
            #         else:
            #             filter_value = filter.get("value")
            #
            #             if filter_value:
            #                 if filter_type == "==":
            #                     df = df[df[filter_key] == filter_value].copy()
            #                 elif filter_type == "<=":
            #                     df = df[df[filter_key] <= filter_value].copy()
            #                 elif filter_type == "<":
            #                     df = df[df[filter_key] < filter_value].copy()
            #                 elif filter_type == ">":
            #                     df = df[df[filter_key] > filter_value].copy()
            #                 elif filter_type == ">=":
            #                     df = df[df[filter_key] >= filter_value].copy()
            #                 elif filter_type == "contains":
            #                     dtype = df[filter_key].dtype
            #                     if dtype == "object":
            #                         df = df[df[filter_key].str.contains(filter_value, na=False, regex=True)].copy()
            #                     else:
            #                         df = df[df[filter_key].astype(str).str.contains(filter_value, na=False, regex=True)].copy()
            #                 elif filter_type == "in (comma separated)":
            #                     items = filter_value.split(",")
            #                     df = df[df[filter_key].isin(items)].copy()

            df_filtered.set(df)
        else:
            df_filtered.set(df_in())


    @render.text
    def out_hidden_max_filter_index():
        logger.debug(f"Setting hidden max filter index property to {input.hidden_max_filter_index()}")

        return input.hidden_max_filter_index()

    if auto_apply_filter:
        return df_filters, df_filtered
    else:
        return df_filters

def multifilter_apply(df, filters):
    for i, filter in enumerate(filters):
        if filter is not None and type(filter) == dict:
            filter_key = filter.get("key")
            filter_type = filter.get("type")

            if filter_type == "in":
                filter_values = filter.get("values")

                if filter_values:
                    df = df[df[filter_key].isin(filter_values)].copy()
            else:
                filter_value = filter.get("value")

                if filter_value:
                    if filter_type == "==":
                        df = df[df[filter_key] == filter_value].copy()
                    elif filter_type == "<=":
                        df = df[df[filter_key] <= filter_value].copy()
                    elif filter_type == "<":
                        df = df[df[filter_key] < filter_value].copy()
                    elif filter_type == ">":
                        df = df[df[filter_key] > filter_value].copy()
                    elif filter_type == ">=":
                        df = df[df[filter_key] >= filter_value].copy()
                    elif filter_type == "contains":
                        dtype = df[filter_key].dtype
                        if dtype == "object":
                            df = df[df[filter_key].str.contains(filter_value, na=False, regex=True)].copy()
                        else:
                            df = df[df[filter_key].astype(str).str.contains(filter_value, na=False, regex=True)].copy()
                    elif filter_type == "in (comma separated)":
                        items = filter_value.split(",")
                        df = df[df[filter_key].isin(items)].copy()

    return df

@module.ui
def filter_ui():
    return ui.output_ui("out_filter_modal")

@module.server
def filter_server(input, output, session, keys, df, modal_opened, init_filter=default_filter):
    if type(init_filter) != dict:
        init_filter = default_filter

    selected_key = reactive.Value(init_filter.get("key"))
    selected_type = reactive.Value(init_filter.get("type"))
    selected_value = reactive.Value(init_filter.get("value"))
    selected_values = reactive.Value(init_filter.get("values"))

    filter = reactive.Value({})

    @reactive.Effect
    # @reactive.event(input.in_filter_key(), ignore_init=True)
    def update_selected_key():
        logger.debug(f"Trying to update selected key for {current_namespace()}")
        req(input.in_filter_key())

        logger.debug(f"  OK : Updating selected key for {current_namespace()} to {input.in_filter_key()}")
        selected_key.set(input.in_filter_key())

    @reactive.Effect
    # @reactive.event(input.in_filter_type(), ignore_init=True)
    def update_selected_type():
        logger.debug(f"Trying to update selected type for {current_namespace()}")
        req(input.in_filter_type())

        logger.debug(f"  OK : Updating selected type for {current_namespace()} to {input.in_filter_type()}")
        selected_type.set(input.in_filter_type())

    @reactive.Effect
    # @reactive.event(input.in_filter_value(), ignore_init=True)
    def update_selected_value():
        logger.debug(f"Trying to update selected value for {current_namespace()} to {input.in_filter_value()}")
        req(input.in_filter_value())

        logger.debug(f"  OK : Updating selected value for {current_namespace()} to {input.in_filter_value()}")
        selected_value.set(input.in_filter_value())

    @reactive.Effect
    # @reactive.event(input.in_filter_value(), ignore_init=True)
    def update_selected_values():
        logger.debug(f"Trying to update selected values for {current_namespace()} to {input.in_filter_values()}")
        req(input.in_filter_values())

        logger.debug(f"  OK : Updating selected values for {current_namespace()} to {input.in_filter_values()}")
        dtype = df()[selected_key()].dtype
        values = []
        if input.in_filter_values():
            # when changing the key, values may be set, but not compatible with the current data type
            try:
                values = pd.Series(input.in_filter_values(), dtype=dtype).tolist()
            except:
                values = []

        selected_values.set(values)

    @reactive.Effect
    def update_filter():
        logger.debug(f"Updating filter dict for {current_namespace()}")

        new_filter_val = {
            "key": selected_key(),
            "type": selected_type(),
            "value": selected_value(),
            "values": [] if selected_values() is None else list(selected_values())
        }
        logger.debug(f"Current filter value: {new_filter_val}")
        filter.set(new_filter_val)

    @reactive.Calc
    def value_choices():
        logger.debug(f"Trying to reset value choices for {current_namespace()}")
        req(selected_key(), not df().empty)

        logger.debug(f"  OK : Resetting value choices for {current_namespace()}")
        choices_1 = df()[selected_key()].drop_duplicates().sort_values()
        choices = df()[selected_key()].drop_duplicates().sort_values().astype(df()[selected_key()].dtype)

        return choices.tolist()

    @reactive.Effect
    def update_value_choices():
        with reactive.isolate():
            current_values = selected_values()

        ui.update_select("in_filter_values", choices=value_choices(), selected=current_values)


    @reactive.Effect
    @reactive.event(input.in_clear_filter)
    def clear_filter():
        req(input.in_clear_filter())

        ui.update_select("in_filter_values", choices=value_choices(), selected=[])
        ui.update_text("in_filter_value", value="")
        selected_value.set("")
        selected_values.set([])


    @render.ui
    def out_filter_modal():
        req(keys(), modal_opened())
        logger.debug(f"Rendering modal output for {current_namespace()}")

        with reactive.isolate():

            logger.debug(f"Current (key, type, value, values) : ({init_filter.get('key')}, {init_filter.get('type')}, {init_filter.get('value')}, {init_filter.get('values')})")

            content = ui.row(
                ui.column(
                    3,
                    ui.input_select("in_filter_key", "Filter Key",
                                    choices=keys(),
                                    selected=selected_key(),
                                    multiple=False,
                                    selectize=True,
                                    width=250
                                    )
                ),
                ui.column(
                    3,
                    ui.input_select("in_filter_type", "Filter Type",
                                    choices=filter_types,
                                    selected=selected_type(),
                                    multiple=False,
                                    selectize=True,
                                    width=250
                                    )
                ),
                ui.column(
                    5,
                    ui.panel_conditional(
                        "input.in_filter_type == 'in'",
                        ui.input_select("in_filter_values", "Filter Values",
                                        choices=value_choices(),
                                        selected=selected_values(),
                                        multiple=True,
                                        selectize=True,
                                        width="100%"
                                        )
                    ),
                    ui.panel_conditional(
                        "input.in_filter_type != 'in'",
                        ui.input_text("in_filter_value", "Filter Value",
                                      value=selected_value(),
                                      width="100%"
                                      )
                    )
                ),
                ui.column(
                    1,
                    ui.div(
                        ui.tags.label("Clear", class_="control-label invisible"),
                        ui.input_action_link(
                            "in_clear_filter",
                            ui.tags.span(
                                class_="bi-x-circle-fill",
                                style=f"color: var(--bs-danger); background-color: transparent; "
                            ),
                            class_="d-block"
                        ),
                        class_="form-group shiny-input-container"
                    )
                )
            )



        return content

    return filter