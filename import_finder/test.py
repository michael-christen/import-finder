from unittest import TestCase

from .import_finder import get_import_module_from_line


TEST_INPUT = '''
import x
import x as z

import x.y
import x.y as z.hi
(
from x import y
from x import y as z

from x.hi import y
from x.bye import y as z

import .local
import .local as z

import .local.hello
import .local.hello as z.fellow

from .local import y
from .local import y as z

from .local.hey import y
from .local.hey import y as z

import ..back_local.hi
from ..back_local import hi

import __future__
from __future__ import six

try:
    import x
    import x as z

    import x.y
    import x.y as z.hi

    from x import y
    from x import y as z

    from x.hi import y
    from x.bye import y as z

    import .local
    import .local as z

    import .local.hello
    import .local.hello as z.fellow

    from .local import y
    from .local import y as z

    from .local.hey import y
    from .local.hey import y as z

    import ..back_local.hi
    from ..back_local import hi

    import __future__
    from __future__ import six
except ImportError:
    pass
'''


class TestGetImportModuleFromLine(TestCase):
    def test_extensive(self):
        import_modules = [get_import_module_from_line(line)
                          for line in TEST_INPUT.split('\n')]
        import_modules = [line for line in import_modules if line]
        self.assertEquals([
            'x', 'x', 'x.y', 'x.y', 'x.y', 'x.y', 'x.hi.y', 'x.bye.y',
            '.local', '.local', '.local.hello', '.local.hello', '.local.y',
            '.local.y', '.local.hey.y', '.local.hey.y', '..back_local.hi',
            '..back_local.hi', '__future__', '__future__.six',
            'x', 'x', 'x.y', 'x.y', 'x.y', 'x.y', 'x.hi.y', 'x.bye.y',
            '.local', '.local', '.local.hello', '.local.hello', '.local.y',
            '.local.y', '.local.hey.y', '.local.hey.y', '..back_local.hi',
            '..back_local.hi', '__future__', '__future__.six',
            ], import_modules)
