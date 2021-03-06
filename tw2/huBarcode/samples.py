"""
Here you can create samples of your widgets by providing default parameters,
inserting them in a container widget, mixing them with other widgets, etc...
These samples will appear in the WidgetBrowser

See http://toscawidgets.org/documentation/WidgetBrowser for more information
"""

from widgets import HuBarcodeWidget

class DemoHuBarcodeWidget(HuBarcodeWidget):
    text = 'This is the encoded text'
    ## Eventually, we want this to be fed by text input field via a form
