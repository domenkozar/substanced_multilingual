from pyramid.httpexceptions import HTTPFound

from substanced.sdi import mgmt_view
from substanced.form import FormView
from substanced.interfaces import IFolder

from .interfaces import ITranslatableFolder


@mgmt_view(
    context=ITranslatableFolder,
    name='add_multilingual_content',
    tab_title='Add Translation',
    permission='sdi.add-content',
    renderer='substanced.sdi:templates/form.pt',
    tab_condition=False,
)
class AddTranslationView(FormView):
    title = 'Add Translation'
    #schema = BlaSchema()
    # TODO: dynamically get correct schema
    buttons = ('add',)

    def add_success(self, appstruct):
        registry = self.request.registry
        import pdb;pdb.set_trace()
        name = appstruct.pop('number')
        document = registry.content.create('..', **appstruct)
        self.context[name] = document
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
        )
