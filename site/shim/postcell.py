"""Offline stand-in for the `postcell` classroom magic.

The real postcell package POSTs cell contents to postcell.io so an instructor
can collect student answers during a live class. That is exactly wrong for a
published book: it would send every reader's keystrokes to the instructor's
account, and it requires a server the reader has no access to.

This module registers the same magic name and does neither. `%%postcell <id>`
simply runs the cell like any other code cell, so exercises stay live and
editable in the browser while nothing leaves the page.

Registering the same name is what lets the lecture notebooks be published
completely unmodified — no preprocessing step, no second copy to keep in sync.
"""

from IPython.core.magic import Magics, magics_class, line_cell_magic


@magics_class
class PostCell(Magics):
    @line_cell_magic
    def postcell(self, line, cell=None):
        if cell is None:
            # Line form, e.g. `%postcell register`. Nothing to do offline.
            return
        self.shell.run_cell(cell)


def load_ipython_extension(ipython):
    ipython.register_magics(PostCell)
