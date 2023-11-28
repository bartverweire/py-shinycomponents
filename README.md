# py-shinycomponents

This project aims to port Shiny extensions for R to python.

Currently, the project focuses on 
  * Busyindicator [(Shinybusy)](https://dreamrs.github.io/shinybusy/)
  * [Shinydashboard](https://rstudio.github.io/shinydashboard/)

# Tests
Tests are sample Shiny applications.
To run them without running into a ModuleNotFoundError, I suggest the [solution from Stackoverflow](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143)

```
pip install -e .
```

or, as proposed on [the Shiny project page](https://github.com/rstudio/py-shiny/)
```
pip install -e ".[dev,test]"
```

Then run the shiny test applications, e.g.
```
shiny run tests/busyindicator/app_busy_bar_manual.py
```

