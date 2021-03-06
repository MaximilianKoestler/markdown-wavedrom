import re
import xml.etree.ElementTree as etree

from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension


class WavedromProcessor(BlockProcessor):
    _start = re.compile(r"^wavedrom\s*\(\s*\n")

    def __init__(self, parser):
        super().__init__(parser)

    def test(self, parent, block):
        return self._start.match(block)

    def run(self, parent, blocks):
        diag_blocks = []

        for block in blocks:
            block = block.strip()
            diag_blocks.append(block)
            if block.endswith(")"):
                break

        lines = [line.strip() for block in diag_blocks for line in block.splitlines()]
        content = "\n".join(lines[1:-1])
        del blocks[: len(diag_blocks)]

        script = etree.SubElement(parent, "script")
        script.attrib["type"] = "WaveDrom"
        script.text = content


class WavedromExtension(Extension):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        md.parser.blockprocessors.register(WavedromProcessor(md.parser), "wavedrom", 100)
        md.registerExtension(self)
