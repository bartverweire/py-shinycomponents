import sys
sys.path.insert(0, "../..")
sys.path.insert(0, ".")
print(sys.path)

from shiny import *
import shinycomponents as sc

app_ui = sc.page_dashboard(
    ui.div(
        class_="wrapper"
    )

)

def server(input, output, session):

    pass



app = App(app_ui, server)

def main():
    run_app(app)

if __name__ == "__main__":
    main()

