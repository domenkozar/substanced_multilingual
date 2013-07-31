# TODO: add a view that returns content based on route matching

from .resources import TranslatableContent
from .resources import TranslatableFolder


def add_multilingual_language(config,
                              language_code,
                              language_name):
    """
    TODO
    """

    def register():
        # setup routes
        config.add_route(language_code, '/{}*traverse'.format(language_code))

        # add language to registry
        if getattr(config.registry, 'languages', None) is None:
            config.registry.languages = []
        # TODO: pass in language_name and use it when adding new content
        config.registry.languages.append(language_code)
        #config.registry.registerUtility(languagecode,
        #                                IMultilingualLanguage,
        #                                name=name)

    discriminator = ('multilingual-language', language_code)
    intr = config.introspectable(
        'multilingual languages',
        discriminator,
        language_code,
        'multilingual language',
        )
    intr['language_code'] = language_code
    intr['language_name'] = language_name

    config.action(discriminator, callable=register, introspectables=(intr,))


def add_multilingual_content(config,
                             name,
                             folder_cls=TranslatableFolder,
                             content_cls=TranslatableContent,
                             sheets=tuple()):
    """
    TODO
    """
    def register():
        # TODO: register folder_cls

        for language_code in config.registry.languages:
            config.add_content_type(
                language_code + "_" + name,
                content_cls,
                icon='icon-flag',
                propertysheets=sheets,
            )

    discriminator = ('multilingual-content', name, content_cls)
    intr = config.introspectable(
        'multilingual language contents',
        discriminator,
        content_cls,
        'multilingual language content',
        )

    config.action(discriminator, callable=register,
                  introspectables=(intr,), order=1)


def includeme(config):
    """ This function returns a Pyramid WSGI application.
    """
    config.add_directive('add_multilingual_language',
                         add_multilingual_language)
    config.add_directive('add_multilingual_content',
                         add_multilingual_content)
    config.scan()
