from dependency_injector import containers, providers

from application.providers.data import DatabaseAccessLayer


class IOCDatabase(containers.DeclarativeContainer):
    """IoC container of database providers."""

    db = providers.Singleton(DatabaseAccessLayer)
