import os, sys
import importlib


def indexer_exports():
    """ Indexer files should export these, for use as __all__"""
    return ['pre_process', 'post_process']


def htmlifier_exports():
    """ Htmlifier files should export these, for use as __all__"""
    return ['htmlify', 'load']


def load_indexers(tree):
    """ Load indexers for a given tree """
    # Allow plugins to load from the plugin folder
    sys.path.append(tree.config.plugin_folder)
    plugins = []
    for name in tree.enabled_plugins:
        path = os.path.join(tree.config.plugin_folder, name)
        spec = importlib.machinery.PathFinder.find_spec("indexer", [path])
        plugin = importlib.util.module_from_spec(spec)
        sys.modules['dxr.plugins.' + name + "_indexer"] = plugin
        spec.loader.exec_module(plugin)
        plugins.append(plugin)
    return plugins


def load_htmlifiers(tree):
    """ Load htmlifiers for a given tree """
    # Allow plugins to load from the plugin folder
    sys.path.append(tree.config.plugin_folder)
    plugins = []
    for name in tree.enabled_plugins:
        path = os.path.join(tree.config.plugin_folder, name)
        spec = importlib.machinery.PathFinder.find_spec("htmlifier", [path])
        plugin = importlib.util.module_from_spec(spec)
        sys.modules['dxr.plugins.' + name + "_htmlifier"] = plugin
        spec.loader.exec_module(plugin)
        plugins.append(plugin)
    return plugins
