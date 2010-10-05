
# tw2-proper imports
import tw2.core as twc
from huBarcode.datamatrix import DataMatrixEncoder
import uuid
import images

class HuBarcodeWidget(twc.Widget):
    resources = [twc.DirLink(modname='tw2.huBarcode', filename='images/')]

    template = 'tw2.huBarcode.templates.barcode'
    text = twc.Param('text to be image-ified', default='no text')
    location = twc.Variable('location of teh file')

    def prepare(self):
        # Figure out where I'm installed
        self.location = "/".join(images.__file__.split('/')[:-1])
        self.location += '/' + str(uuid.uuid4()) + '.png'

        # Save files out to the 'images' directory
        encoder = DataMatrixEncoder(self.text)
        encoder.save(self.location)

        # Tell tw2 and wsgi land where to find files
        self.location = self.location.split('images')[1]
        url = '/resources/tw2.huBarcode/images' + self.location
        img = twc.Link(link=url, filename='images' + self.location)
        self.resources.append(img)
        self.location = url

        # Fire it all off
        super(HuBarcodeWidget, self).prepare()
