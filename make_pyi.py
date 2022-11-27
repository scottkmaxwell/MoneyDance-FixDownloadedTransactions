# !/usr/bin/env python
# coding=utf-8
# Python script to be run in Moneydance to perform amazing feats of financial scripting

# TODO: Handle overloaded methods

import inspect
import os.path

# noinspection PyUnresolvedReferences
import com.infinitekind.moneydance.model.txtimport
# noinspection PyUnresolvedReferences
import com.infinitekind.moneydance.model
# noinspection PyUnresolvedReferences
import com.infinitekind.moneydance.online
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.bot
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.fileimport
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.olb
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.olb.ofx
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.sync
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.extensionapi
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.view
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.view.gui
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.view.gui.bot
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.view.gui.editlistdlg
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.view.resources
# noinspection PyUnresolvedReferences
import com.moneydance.apps.md.controller.sync
# noinspection PyUnresolvedReferences
import com.moneydance.security
# noinspection PyUnresolvedReferences
import com.moneydance.util
# noinspection PyUnresolvedReferences
import com.infinitekind.tiksync
# noinspection PyUnresolvedReferences
import com.infinitekind.util

modules = (
    com.infinitekind.tiksync,
    com.infinitekind.util,
    com.moneydance.security,
    com.infinitekind.moneydance.model,
    com.infinitekind.moneydance.online,
    com.infinitekind.moneydance.model.txtimport,
    com.moneydance.apps.md.extensionapi,
    com.moneydance.apps.md.controller,
    com.moneydance.apps.md.view,

    com.moneydance.apps.md.controller.fileimport,
    com.moneydance.apps.md.view.gui,
    com.moneydance.apps.md.view.gui.bot,
    com.moneydance.apps.md.view.gui.editlistdlg,
    com.moneydance.apps.md.view.resources,
    com.moneydance.util,
    com.moneydance.apps.md.controller.bot,
    com.moneydance.apps.md.controller.olb,
    com.moneydance.apps.md.controller.olb.ofx,
    com.moneydance.apps.md.controller.sync,
    com.moneydance.apps.md.view.gui.sync,
)
module_names = set([m.__name__ for m in modules])

root = os.path.dirname(__file__)
write_folder = root  # os.path.join(root, 'for_ide')


class MethodDetails:
    def __init__(self, result=None, params=''):
        self.result = result
        self.params = params


class_info = {
    'Account': {
        'adjustStartBalance': MethodDetails(params='adjust_amount: int'),
    }
}

typing = set('Callable, Dict, Iterator, Iterable, List, Set, Sequence'.split(', '))

type_conversions = {
    'void': 'None',
    'boolean': 'bool',
    'byte': 'int',
    'char': 'int',
    'double': 'float',
    'float': 'float',
    'int': 'int',
    'long': 'int',
    'java.math.BigInteger': 'int',
    'java.lang.Exception': 'Exception',
    'java.lang.Integer': 'int',
    'java.lang.Iterable': 'Iterable',
    'java.lang.Long': 'int',
    'java.lang.Object': 'object',
    'java.lang.Runnable': 'Callable',
    'java.lang.String': 'str',
    'java.util.ArrayList': 'list',
    'java.util.HashMap': 'dict',
    'java.util.Hashtable': 'dict',
    'java.util.Iterator': 'Iterator',
    'java.util.List': 'list',
    'java.util.Map': 'dict',
    'java.util.Set': 'set',
    'java.util.Vector': 'list',
    'org.python.core.PyObject': 'object',
}


class Builder:
    def __init__(self):
        self.indent = 0
        self.result = ''
        self.index = 0

    def add(self, line='', post_indent=0):
        self.index += 1
        if self.result:
            self.result += '\n'
        self.result += '{}{}'.format(' ' * (4*self.indent), line)
        self.indent += post_indent


class ModulePYIWriter(object):
    def __init__(self, module):
        assert module in modules
        self.module = module
        classes = [(name, member) for name, member in inspect.getmembers(module) if inspect.isclass(member) and member.__module__ == module.__name__]
        self.classes_dict = {name: member for name, member in classes}
        self.classes = [member for name, member in classes]
        self.class_local_bases = {}
        self.class_external_bases = {}
        self.started_output_classes = set()
        self.completed_output_classes = set()
        self.builder = Builder()
        self.unknown_types = set()
        self.other_modules = set()
        self.typings = set()
        self.has_generic = False
        self.lines = []

        self.register_bases_in_module(inspect.getclasstree(self.classes, False))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.lines:
            parts = self.module.__name__.split('.')
            path = write_folder
            if not os.path.exists(path):
                os.makedirs(path)
            for part in parts:
                path = os.path.join(path, part)
                if not os.path.exists(path):
                    os.makedirs(path)
                    with open(os.path.join(path, '__init__.pyi'), 'w'):
                        pass
            filename = os.path.join(path, '__init__.pyi')
            # print 'Writing {}'.format(filename)
            with open(filename, 'w') as f:
                if self.has_generic:
                    self.typings.add('TypeVar')
                if self.typings:
                    f.write('from typing import {}\n'.format(', '.join(sorted(self.typings))))
                for other in sorted(self.other_modules):
                    f.write('import {}\n'.format(other))
                f.write('\n')
                if self.has_generic:
                    f.write('T = TypeVar("T")\n\n')
                f.write('\n')
                for line in self.lines:
                    f.write(line)
                    f.write('\n')

    def add(self, line='', post_indent=0):
        # type: (str, int) -> None
        self.builder.add(line, post_indent)

    def _write(self, line):
        self.lines.append(line)

    def write_all(self):
        for c in self.classes:
            self.write_class(c)

    def convert_parameter_type(self, p, used_names):
        # type: (str, set[str]) -> str
        full_type = self.convert_type(p)
        t = full_type.replace("'", '')
        if 'A' <= t[0] <= 'Z':
            proposed_name = t[0].lower() + t[1:]
        else:
            proposed_name = t[0]
        proposed_name = proposed_name.partition('[')[0]
        name = proposed_name
        next_index = 2
        while proposed_name in used_names:
            proposed_name = '{}{}'.format(name, next_index)
            next_index += 1
        used_names.add(proposed_name)

        return '{}: {}'.format(proposed_name, full_type)

    def convert_type(self, p):
        # type: (str) -> str
        p = p.strip()
        if '<' in p:
            container, contents = p.partition('<')[::2]
            contents = contents[:-1]
            if container in ('java.util.Map', 'java.util.HashMap', 'java.util.Hashtable'):
                parts = contents.split(',')
                if len(parts) != 2:
                    raise Exception('Expected {} to have 2 parts'.format(parts))
                self.typings.add('Dict')
                return 'Dict[{},{}]'.format(self.convert_type(parts[0]), self.convert_type(parts[1]))
            if container in ('java.util.List', 'java.util.ArrayList'):
                self.typings.add('List')
                return 'List[{}]'.format(self.convert_type(contents))
            if container == 'java.util.Collection':
                self.typings.add('Sequence')
                return 'Sequence[{}]'.format(self.convert_type(contents))
            if container == 'java.util.Set':
                self.typings.add('Set')
                return 'Set[{}]'.format(self.convert_type(contents))
            if container == 'java.util.Iterator':
                self.typings.add('Iterator')
                return 'Iterator[{}]'.format(self.convert_type(contents))
            if container == 'java.lang.Iterable':
                self.typings.add('Iterable')
                return 'Iterable[{}]'.format(self.convert_type(contents))
            if container in ('java.util.Comparable', 'java.util.Comparator'):
                self.typings.add('Callable')
                return 'Callable[[{0}, {0}], int]'.format(self.convert_type(contents))
            self.typings.add('Any')
            return 'Any'
            # raise NotImplementedError('Conversion for {}'.format(p))
        if p.endswith('[]'):
            p = self.convert_type(p[:-2])
            self.typings.add('List')
            return 'List[{}]'.format(p)
        if '$' in p:
            return 'str'
        if p and p.startswith('com.'):
            if p.startswith(self.module.__name__ + '.'):
                type_name = p[len(self.module.__name__) + 1:]
                if '.' in type_name:
                    sub_module = type_name.rpartition('.')[0]
                    if '{}.{}'.format(self.module.__name__, sub_module) in module_names:
                        self.other_modules.add(sub_module)
                        return type_name
                    else:
                        return "'{}'".format(type_name)
                return type_name if type_name in self.completed_output_classes else "'{}'".format(type_name)
            else:
                for m in modules:
                    other_module = p.rpartition('.')[0]
                    if m.__name__ == other_module:
                        self.other_modules.add(other_module)
                        return p  # if modules.index(m) > modules.index(self.module) else "'{}'".format(type_name)
        result = type_conversions.get(p)
        if result is not None:
            if result in typing:
                self.typings.add(result)
            return result
        if p == 'T':
            self.has_generic = True
        else:
            self.unknown_types.add(p)
        return "'{}'".format(p)

    @staticmethod
    def fixup_container_strings(params):
        i = params.find('<')
        while i >= 0:
            e = params.find('>', i + 1)
            params = params[:i] + params[i:e].replace(' ', '') + params[e:]
            i = params.find('<', e)
        return params

    def parse_return_type(self, method):
        result = self.fixup_container_strings(str(method.annotatedReturnType))
        return self.convert_type(result)

    def parse_parameters(self, method):
        if method.parameterCount == 0:
            return ''
        used_names = set()
        params = self.fixup_container_strings(str(method.annotatedParameterTypes).partition('[')[2][:-2])
        if method.parameterCount == 1:
            return self.convert_parameter_type(params, used_names)
        params = params.split(', ')
        if len(params) != method.parameterCount:
            raise Exception('{} should have {} entries'.format(params, method.parameterCount))
        return ', '.join(self.convert_parameter_type(param, used_names) for param in params)

    def register_bases_in_module(self, items):
        for item in items:
            if isinstance(item, tuple):
                cls, bases = item
                if cls.__module__ == self.module.__name__:
                    bases = tuple(filter(lambda x: x.__module__ == self.module.__name__, item[1]))
                    if bases:
                        self.class_local_bases[cls] = bases
                    bases = tuple(filter(lambda x: x.__module__ != self.module.__name__ and x.__name__ != 'Object', item[1]))
                    if bases:
                        self.class_external_bases[cls] = bases
            elif isinstance(item, list):
                self.register_bases_in_module(item)

    def write_class(self, c):
        if c not in self.started_output_classes:
            self.started_output_classes.add(c)
            bases = self.class_local_bases.get(c, [])
            for base in bases:
                self.write_class(base)
            name = c.__name__
            self.build_class(name, c, bases, self.class_external_bases.get(c, []))
            self._write(self.builder.result)
            self.builder = Builder()
            self.completed_output_classes.add(name)

    def build_class(self, class_name, c, bases=None, external_bases=None):
        # type: (str, type, list[type], list[type]) -> None

        bases = bases or []
        external_bases = external_bases or []
        class_method_info = class_info.get(class_name, {})

        base = ''
        if bases or external_bases:
            internal_parts = [bc.__name__ for bc in bases]
            external_parts = [self.convert_type('.'.join([bc.__module__, bc.__name__])) for bc in external_bases]
            base = '(' + ', '.join(internal_parts + external_parts) + ')'
        self.add('class {}{}:'.format(class_name, base), post_indent=1)
        def_index = self.builder.index

        start_index = self.builder.index
        try:
            for name, value in inspect.getmembers(c, lambda k: not inspect.isclass(k) and not inspect.ismethod(k) and not inspect.isroutine(k)):
                if name == '__doc__' and value is None:
                    continue
                if not value or isinstance(value, (int, float, unicode, str, bool)):
                    v = repr(value)
                else:
                    v = repr(str(value))
                self.add('{} = {}'.format(name, v))
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        start_index = self.builder.index
        try:
            for name, method in inspect.getmembers(c, lambda k: (inspect.ismethod(k) or inspect.isroutine(k)) and not inspect.ismethoddescriptor(k)):
                self.build_method(c, class_method_info, name, method)
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        start_index = self.builder.index
        try:
            for name, cls in inspect.getmembers(c, lambda k: inspect.isclass(k) and k.__module__ == self.module.__name__):
                if '{}${}'.format(class_name, name) in str(cls):
                    self.build_class(name, cls)
        except TypeError:
            pass
        if start_index != self.builder.index:
            self.add()

        if def_index == self.builder.index:
            self.add('pass')
            self.add()

        self.builder.indent -= 1

    def build_method(self, cls, class_method_info, name, method):
        if name in ('__new__', '__subclasshook__'):
            return
        arg_list = method.argslist[0] if hasattr(method, 'argslist') else None
        comment = ''
        selfer = 'self'
        returner = ''
        paramer = ''
        staticer = ''
        method_info = class_method_info.get(name)
        if arg_list:
            m = arg_list.method
            if arg_list.declaringClass != cls:
                return
            paramer = method_info.params if method_info else self.parse_parameters(m)
            selfer = 'self, ' if paramer else 'self'
            if name != '__init__':
                if hasattr(arg_list, 'isStatic') and arg_list.isStatic:
                    selfer = ''
                    staticer = '@staticmethod'
                returner = ' -> {}'.format(self.parse_return_type(m))

        if staticer:
            self.add(staticer)
        self.add('def {}({}{}){}: ...'.format(name, selfer, paramer, returner))
        if comment:
            self.add(comment)
        self.add()


# noinspection PyTypeChecker
def main():
    all_unknown_types = set()
    for module in modules:
        with ModulePYIWriter(module) as writer:
            writer.write_all()
            all_unknown_types.update(writer.unknown_types)
    with open(os.path.join(write_folder, 'moneydance.pyi'), 'w') as f:
        module_names = [module.__name__ for module in modules]
        for module in sorted(module_names):
            f.write('import {}\n'.format(module))
        f.write('\n')
        f.write('moneydance = com.moneydance.apps.md.controller.Main()\n')
        f.write('moneydance_data = com.infinitekind.moneydance.model.AccountBook()\n')
        f.write('moneydance_ui = com.moneydance.apps.md.view.gui.MoneydanceGUI()\n')
        f.write('moneybot = com.moneydance.apps.md.view.gui.bot.PythonInterface()\n')

    if all_unknown_types:
        print('Unknown:')
        for u in sorted(all_unknown_types):
            print ' ', u


main()
