icon_classes = {
    "ion": "ion",
    "fa": "fas",
    "bi": "bi"
}

def build_icon_class(icon_name):
    # derive icon prefix (ion-, fa-, bi-)
    if icon_name is None:
        return None

    parts = icon_name.split("-")
    icon_class = None
    if len(parts) > 0:
        icon_class = icon_classes[parts[0]]

    if icon_class is not None:
        return f"{icon_class} {icon_name}"
    else:
        return icon_name