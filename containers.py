from dependency_injector import providers, containers
from RandomAgent import RandomAgent

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Agents(containers.DeclarativeContainer):
    random_agent = providers.Singleton(RandomAgent, Configs.config)
    # other clients 