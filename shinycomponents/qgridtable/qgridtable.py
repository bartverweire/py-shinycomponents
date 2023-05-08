from shiny import *
from shinywidgets import *

import qgrid

import utils.logging as app_logging
logger = app_logging.get_logger(__name__)


qgridtable_gradient = """
<div style="display: none;">{content}</div><div class="w-100" style="background:linear-gradient(90deg,
        {grad_color} 0%,
        {grad_color} {grad_value}%,
        {bg_color} {grad_value}%,
        {bg_color} 100%)">
    {content}
</div>
"""

qgridtable_default_grad_color = "blue"
qgridtable_default_bg_color = "white"


@module.ui
def qgridtable_ui():
    return output_widget("out_qgrid_table")


@module.server
def qgridtable_server(input, output, session,
                      df: reactive.Value,
                      *,
                      number_precision=2,
                      column_definitions: dict = dict(),
                      grid_options: dict = {
                          "editable": False
                      },
                      interactive: bool = True,
                      gradient_columns=[],
                      gradient_colors=[],
                      bg_colors=[],
                      ):
    selected_rows = reactive.Value()

    @reactive.Calc
    def df_with_gradients():
        dfg = df().copy()

        if type(gradient_columns) == str or type(gradient_columns) == list:
            _gradient_columns = gradient_columns
        elif isinstance(gradient_columns, reactive._reactives.Value):
            _gradient_columns = gradient_columns()
        else:
            raise ValueError("gradient_columns must be a String, list or reactive.Value")

        logger.debug("Gradient columns: {}".format(_gradient_columns))

        for i, col_spec in enumerate(_gradient_columns):
            color = get_color(i, gradient_colors)
            bg_color = get_color(i, bg_colors, qgridtable_default_bg_color)
            if type(col_spec) == tuple and len(col_spec) == 2:
                logger.debug("Gradient columns specified as tuple")
                grad_disp_col = col_spec[0]
                grad_val_col = col_spec[1]

                logger.debug("Setting gradient colors for column {} to {}/{}".format(grad_disp_col, color, bg_color))

                ref_val = dfg[grad_val_col].max()/100

                dfg[grad_disp_col] = dfg.apply(
                    lambda x: qgridtable_gradient.format(grad_color=color, bg_color=bg_color,
                                                         grad_value=x[grad_val_col]/ref_val,
                                                         content=("{:>21." + str(number_precision) + "f}").format(x[grad_disp_col]).rjust(21, ' ')
                                                         ),
                    axis=1
                    )

                dfg = dfg.drop(columns=grad_val_col)
            elif type(col_spec) == str:
                logger.debug("Gradient columns specified as string")
                grad_disp_col = col_spec
                grad_val_col = col_spec

                ref_val = dfg[grad_val_col].max() / 100

                logger.debug("Setting gradient colors for column {} to {}/{}".format(grad_disp_col, color, bg_color))

                dfg[grad_disp_col] = dfg.apply(
                    lambda x: qgridtable_gradient.format(grad_color=color, bg_color=bg_color,
                                                         grad_value=x[grad_val_col]/ref_val,
                                                         content=("{:>21." + str(number_precision) + "f}").format(x[grad_disp_col]).rjust(21, ' ')
                                                         ),
                    axis=1
                )
            else:
                logger.debug("Gradient columns specification unknown")
                pass

        logger.debug("Data frame with gradients, first rows")
        logger.debug(dfg.head())

        return dfg

    @output
    @render_widget
    def out_qgrid_table():
        req(not df_with_gradients().empty)

        qt = qgrid.show_grid(
            df_with_gradients(),
            precision=number_precision,
            show_toolbar=False,
            column_definitions=column_definitions,
            grid_options=grid_options
        )

        if interactive:
            qt.on("selection_changed", qgrid_select_handler)

        return qt

    def qgrid_select_handler(event, widget):
        # Get the data frame that is displayed. This may differ from the original data frame
        # because of filtering, sorting, ...
        dfw = widget.get_changed_df()
        # Get the selected rows. This is an array of row indexes (after filtering, sorting, ...)
        sel = event["new"]

        # Set the value of the selected_rows reactive.Value to the data frame obtained by applying the index
        selected_rows.set(dfw.iloc[sel, :])

    return selected_rows


def get_color(i, colors, default_color=qgridtable_default_grad_color):
    if i < len(colors):
        color = colors[i]
    elif len(colors) == 1:
        color = colors[0]
    else:
        color = default_color

    return color