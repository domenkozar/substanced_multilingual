from zope.interface import (
    implementer,
)

from substanced.folder import Folder

from persistent import Persistent
from pyramid.threadlocal import get_current_registry

from .interfaces import ITranslatableFolder, ITranslatableContent


@implementer(ITranslatableContent)
class TranslatableContent(Persistent):

    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)


@implementer(ITranslatableFolder)
class TranslatableFolder(Folder):

    def __sdi_addable__(self, context, introspectable):
        """Add languages as addable content with schema defined for the content type"""
        registry = get_current_registry()
        content_type = registry.content.typeof(context)
        for language_code, language_name in registry.languages:
            if content_type + "_" + language_code == introspectable['content_type']:
                return True

    def get_translated_content(self):
        """Returns content in language supplied by traversal info"""
        import pdb;pdb.set_trace()
