from shiny import *

import re
import numpy as np

@module.ui
def modalfilter_ui(button_text, class_="col-8 btn-primary me-2"):
    return ui.div(
        ui.input_action_button("in_show_modal", button_text, class_=class_),
        ui.input_action_link(
          "in_clear_filter",
          ui.tags.i(
              class_="bi-x-circle-fill",
              style="color: darkblue; background-color: transparent; "
          )
        ),
        class_="d-flex flex-row align-items-center my-1"
    )


@module.server
def modalfilter_server(input, output, session, item_type, items, init_selection=[], modal_title=None, modal_size="l"):
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
    selected_items = reactive.Value(init_selection)
    print(type(items))
    # @reactive.Effect
    # def notify_items_change():
    #     print("items for item type {} changed: {} items.".format(item_type, len(items())))


    @reactive.Effect
    @reactive.event(input.in_show_modal)
    def open_modal_filter_username():
        if items():

            m = ui.modal(
                ui.row(
                    ui.column(
                        3,
                        "Include pattern:",
                        class_="fw-bold"
                    ),
                    ui.column(
                        4,
                        ui.input_text("in_include", label=None),
                    ),
                    ui.column(
                        4,
                        ui.input_action_button("in_include_apply", "Update", class_="btn-success"),
                    ),
                    class_="align-items-center"
                ),
                ui.row(
                    ui.column(
                        3,
                        "Exclude pattern:",
                        class_="fw-bold"
                    ),
                    ui.column(
                        4,
                        ui.input_text("in_exclude", label=None),
                    ),
                    ui.column(
                        4,
                        ui.input_action_button("in_exclude_apply", "Update", class_="btn-success"),
                    ),
                    class_="align-items-center"
                ),
                ui.row(
                    ui.column(
                        2,
                        ui.input_action_link(
                            "in_select_all",
                            ui.tags.i(
                                class_="bi-check-square",
                            ),
                            class_="btn-outline-dark"
                        ),
                        ui.input_action_link(
                            "in_unselect_all",
                            ui.tags.i(
                                class_="bi-square ",
                            ),
                            class_="btn-outline-dark"
                        ),
                    )
                ),
                ui.row(
                    ui.input_checkbox_group(
                        "in_chk_selected",
                        ui.tags.div(f"Selected {item_type}", class_="fw-bold my-2"),
                        choices=selected_items(),
                        selected=selected_items(),
                    ),
                    style="width: 100%; max-height: 40vh; overflow-y: auto;",
                    class_="wide_form_container"
                ),
                ui.row(
                    ui.input_checkbox_group(
                        "in_chk_nonselected",
                        ui.tags.div(f"Available {item_type}", class_="fw-bold my-2"),
                        choices=non_selected(),
                        selected=[],
                    ),
                    style="width: 100%; max-height: 40vh; overflow-y: auto;",
                    class_="wide_form_container"
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
        else:
            m = ui.modal(
                """
                Cannot filter on {}". Perhaps there are no items, or you need to reduce the selected items
                in other filters
                """.format(item_type),
                title="Filter disabled"
            )

        ui.modal_show(m)



    @reactive.Effect
    @reactive.event(input.in_include_apply, input.in_exclude_apply)
    def update_filter_modal():
        current_selection = list(input.in_chk_selected()) + list(input.in_chk_nonselected())
        current_selection.sort()

        if input.in_include():
            current_selection = np.unique(current_selection + [u for u in items() if re.search(input.in_include(), u, flags=re.IGNORECASE)]).tolist()
        # logger.debug("Selected items after include filter: {}".format(current_selection))

        if input.in_exclude():
            current_selection = [u for u in current_selection if not re.search(input.in_exclude(), u, flags=re.IGNORECASE)]
        # logger.debug("Selected items after exclude filter: {}".format(current_selection))

        current_selection.sort()
        # logger.debug("Selected items after processing: {}".format(current_selection))
        print("Current selection {}".format(current_selection))

        current_available = [item for item in items() if not item in current_selection]

        ui.update_checkbox_group(
            "in_chk_selected",
            choices=current_selection,
            selected=current_selection
        )
        ui.update_checkbox_group(
            "in_chk_nonselected",
            choices=current_available,
            selected=[]
        )

    @reactive.Effect
    @reactive.event(input.in_select_all)
    def select_all():
        """
        Updates selected and non-selected checkbox groups when the "select-all" checkbox is clicked
        :return:
        """
        ui.update_checkbox_group(
            "in_chk_selected",
            choices=items(),
            selected=items()
        )
        ui.update_checkbox_group(
            "in_chk_nonselected",
            choices=[],
            selected=[]
        )

    @reactive.Effect
    @reactive.event(input.in_unselect_all)
    def unselect_all():
        """
        Updates selected and non-selected checkbox groups when the "unselect-all" checkbox is clicked
        :return:
        """

        ui.update_checkbox_group(
            "in_chk_selected",
            choices=[],
            selected=[]
        )
        ui.update_checkbox_group(
            "in_chk_nonselected",
            choices=items(),
            selected=[]
        )


    @reactive.Effect
    @reactive.event(input.in_apply)
    def update_selected_items():
        """
        Updates the list of selected items from the checkbox groups "selected" and "non-selected"
        :return:
        """
        input_selected = list(input.in_chk_selected()) + list(input.in_chk_nonselected())
        input_selected.sort()

        print("Apply selection {}".format(input_selected))
        selected_items.set(input_selected)

        ui.modal_remove(session)

    @reactive.Effect
    @reactive.event(input.in_clear_filter)
    def clear_selected_items():
        """
        Clears the list of selected items
        :return:
        """
        selected_items.set([])

    @reactive.Calc
    def non_selected():
        """
        Calculates the non-selected items
        :return:
        """
        return [item for item in items() if not item in selected_items()]

    return selected_items