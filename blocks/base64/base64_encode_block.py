from base64 import b64encode

from nio.block.base import Block
from nio.block.mixins import EnrichSignals
from nio.properties import StringProperty, VersionProperty

class Base64Encode(EnrichSignals, Block):

    version = VersionProperty("0.1.0")
    input = StringProperty(title='String to Encode', default='{{ $mystring }}')

    def process_signal(self, signal, input_id=None):
        self.notify_signals(self.get_output_signal({'encoded': b64encode(self.input(signal)) }))
