import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import App, render, ui, reactive, run_app, req
import shinycomponents.modalfilter as scmf
import pandas as pd

app_ui = ui.page_fluid(
    ui.tags.link(
        rel="stylesheet",
        href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.4/font/bootstrap-icons.css"
    ),
    ui.h2("Shiny Multifilter demo"),

    scmf.multifilter_ui("mf_test", "Filter", button_color="danger"),
    ui.output_text_verbatim("out_filters"),
    ui.output_table("out_filtered")
)


def server(input, output, session):
    # df = pd.read_pickle("tests/modalfilter/ash.pkl")
    try:
        df_pkl = pd.read_pickle("tests/data/ash.pkl")
    except:
        df_pkl = pd.read_pickle("../data/ash.pkl")

    df = reactive.Value(df_pkl)


    # df_filters, df_filtered = scmf.multifilter_server("mf_test", df, [
    #     {'key': 'Username', 'type': 'in', 'value': None, 'values': ['COBRHA_PRD', 'CONSRN_PRD']},
    #     {'key': 'Sql Opname', 'type': '==', 'value': "SELECT", 'values': []}
    # ], max_filters=3)

    df_filters = scmf.multifilter_server("mf_test", df, [
        {'key': 'Username', 'type': 'in', 'value': None, 'values': ['COBRHA_PRD', 'CONSRN_PRD']},
        {'key': 'Sql Opname', 'type': '==', 'value': "SELECT", 'values': []}
    ], max_filters=3, auto_apply_filter=False)

    @reactive.Calc
    def df_filtered():
        df_f = scmf.multifilter_apply(df(), df_filters())

        return df_f

    # @render.table
    # def out_filtered():
    #     return df_filtered()

    @render.text
    def out_filters():
        return [f"{filter}\n" for filter in df_filters()]


    @render.table
    def out_filtered():
        req(not df_filtered().empty)

        return df_filtered().iloc[0:100,]


app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()