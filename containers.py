from dependency_injector import providers, containers
from agents.random_agents import RandomAgent

class Configs(containers.DeclarativeContainer):
    config = providers.Configuration('config')
    # other configs
    
class Agents(containers.DeclarativeContainer):
    agent = providers.Singleton(RandomAgent, Configs.config)
    # other clients 