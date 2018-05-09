from dependency_injector import providers

from application.configuration import cfg

config = providers.Configuration('config', default=cfg.default_config)
