from substanced.folder import Folder
from substanced.schema import (
    Schema,
    NameSchemaNode
)

from persistent import Persistent


# TODO: add interfaces


class TranslatableContent(Persistent):

    def __init__(self, **kw):
        for k, v in kw.iteritems():
            setattr(self, k, v)


class TranslatableFolder(Folder):

    def __sdi_addable__(self, context, introspectable):
        # TODO: add languages as addable content with schema defined for the content type
        import pdb;pdb.set_trace()

    def get_translated_content(self):
        """Returns content in language supplied by traversal info"""
        import pdb;pdb.set_trace()
