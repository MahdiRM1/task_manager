from app.services.Exceptions import *

def get_by_id(repo, entity_id):
    entity = repo.get_by_id(entity_id)
    if entity is None:
        raise IdNotFound(entity.__class__.__name__, entity_id)
    return entity

def get_by_name(repo, entity_name):
    entity = repo.get_by_name(entity_name)
    if entity is None:
        raise NameNotFound(entity.__class__.__name__, entity_name)
    return entity