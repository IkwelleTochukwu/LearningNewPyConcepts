"""
Plug-ins are pieces of code supplied by the user of your
program to extend functionality.  A key part of any plug-in
system is plug-in discover. Your program needs to know what
plug-ins are available to load and run.

This program write a simple application that discovers and runs
plug-ins. It uses a user-supplied prefix to search for, load, and
run plug-ins.
"""

import importlib
import fire
import pkgutil


def find_and_run_plugins(plugin_prefix):
    plugins = {}

    # discover and load plugins
    print(f'discovering plugins with prefix: {plugin_prefix}')
    for _, name, _ in pkgutil.iter_modules():
        if name.startswith(plugin_prefix):
            module = importlib.import_module(name)
            plugins[name] = module

    # run plugins
    for name, module in plugins.items():
        print(f'Running plugin {name}....')
        module.run()


if __name__ == '__main__':
    fire.Fire()
