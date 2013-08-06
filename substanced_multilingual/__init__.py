from pyramid.exceptions import ConfigurationError

from .interfaces import ITranslatableFolder
from .resources import TranslatableContent
from .views import AddTranslationView


def add_multilingual_language(config,
                              language_code,
                              language_name):
    """
    TODO
    """

    # setup routes
    # TODO: document how to use resource_url then
    config.add_route(language_code, '/{}*traverse'.format(language_code))

    # add language to registry
    if getattr(config.registry, 'languages', None) is None:
        config.registry.languages = []
    config.registry.languages.append((language_code, language_name))

    discriminator = ('multilingual-language', language_code)
    intr = config.introspectable(
        'multilingual languages',
        discriminator,
        language_code,
        'multilingual language',
        )
    intr['language_code'] = language_code
    intr['language_name'] = language_name

    config.action(discriminator, introspectables=(intr,))


class MultilingualRegistry(object):

    def __init__(self, registry):
        self.registry = registry
        self.schemas = {}

    def add_language_content_type(self, content_type, schema):
        self.schemas[content_type] = schema

    def get_schema_for_content_type(self, content_type):
        return self.schemas[content_type]


def add_multilingual_content(config,
                             content_type,
                             factory,
                             language_factory=TranslatableContent,
                             language_propertysheets=tuple(),
                             language_schema=None,
                             **meta):
    """
    TODO
    """

    config.add_content_type(
        content_type,
        factory,
        **meta)

    if not getattr(config.registry, 'languages', None):
        raise ConfigurationError("You have to define languages to register multilingual content")

    for language_code, language_name in config.registry.languages:
        language_content_type = "{}_{}".format(content_type, language_code)

        # TODO: register country flags for languages instead of using generic
        # register one addable content type per language
        config.registry.multilingual.add_language_content_type(language_content_type,
                                                               language_schema)
        config.add_content_type(
            language_content_type,
            language_factory,
            factory_type=language_content_type,
            name=language_name,
            icon='icon-flag',
            propertysheets=language_propertysheets,
            add_view="add_multilingual_content_{}".format(language_code),
        )

        # add addable view for the content type
        config.add_mgmt_view(
            AddTranslationView,
            context=ITranslatableFolder,
            name='add_multilingual_content_{}'.format(language_code),
            tab_title='Add Translation',
            permission='sdi.add-content',
            renderer='substanced.sdi:templates/form.pt',
            tab_condition=False,
        )

    discriminator = ('multilingual-content', content_type, factory)

    # TODO: see if we need other introspectables than content types
    #intr = config.introspectable(
    #    'multilingual language contents',
    #    discriminator,
    #    factory,
    #    'multilingual language content',
    #    )

    config.action(discriminator)


# TODO: declarative multilingual content
#class multilingual_content(content):
#    """
#    """


def includeme(config):
    """
    """
    config.registry.multilingual = MultilingualRegistry(config.registry)
    config.add_directive('add_multilingual_language',
                         add_multilingual_language)
    config.add_directive('add_multilingual_content',
                         add_multilingual_content)
    config.scan()
