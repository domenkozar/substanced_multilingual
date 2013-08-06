from pyramid.httpexceptions import HTTPFound

from substanced.form import FormView


class AddTranslationView(FormView):
    title = 'Add Translation'
    buttons = ('add',)

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.language_code = request.path.rsplit('_', 1)[1]
        content_type = self.request.registry.content.typeof(self.context)
        self.translated_content_type = "{}_{}".format(content_type, self.language_code)
        multilingual = request.registry.multilingual
        self.schema = multilingual.get_schema_for_content_type(self.translated_content_type)

    def add_success(self, appstruct):
        registry = self.request.registry
        ml = registry.content.create(self.translated_content_type, **appstruct)
        self.context[self.language_code] = ml
        return HTTPFound(
            self.request.sdiapi.mgmt_path(self.context, '@@contents')
        )

