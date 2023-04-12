# py-shinycomponents
Demo project to learn how to create shared components for Shiny. Not ready for production !

# Tests
Tests are sample Shiny applications.
To run them without running into a ModuleNotFoundError, I suggest the [solution from Stackoverflow](https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143)

```
pip install -e .
```

Then run the shiny test applications, e.g.
```
shiny run tests/busyindicator/app_busy_bar_manual.py
```
