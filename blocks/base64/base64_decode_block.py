from base64 import b64decode

from nio.block.base import Block
from nio.block.mixins import EnrichSignals
from nio.properties import StringProperty, VersionProperty

class Base64Decode(EnrichSignals, Block):

    version = VersionProperty("0.1.0")
    input = StringProperty(title='Encoded String', default='{{ $myencodedstring }}')

    def process_signal(self, signal, input_id=None):
        self.notify_signals(self.get_output_signal({'decoded': b64decode(self.input(signal)) }))
