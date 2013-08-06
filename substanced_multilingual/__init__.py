from pyramid.exceptions import ConfigurationError

from .resources import TranslatableContent


def add_multilingual_language(config,
                              language_code,
                              language_name):
    """
    TODO
    """

    # setup routes
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


def add_multilingual_content(config,
                             content_type,
                             factory,
                             language_factory=TranslatableContent,
                             language_propertysheets=tuple(),
                             **meta):
    """
    TODO
    """

    config.add_content_type(
        content_type,
        factory,
        **meta)

    if not getattr(config.registry, 'languages', None):
        raise ConfigurationError("You have to define languages to have multilingual content")

    for language_code, language_name in config.registry.languages:
        language_content_type = content_type + "_" + language_code
        config.add_content_type(
            language_content_type,
            language_factory,
            factory_type=content_type + "_" + language_code,
            name=language_name,
            icon='icon-flag',
            propertysheets=language_propertysheets,
            add_view="add_multilingual_content",
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
    config.add_directive('add_multilingual_language',
                         add_multilingual_language)
    config.add_directive('add_multilingual_content',
                         add_multilingual_content)
    config.scan()
