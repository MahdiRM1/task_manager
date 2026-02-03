from app.adapters.Exceptions import NameNotFound
from app.adapters.models.TagModel import TagModel
from app.core.entities.Tag import Tag
from app.domain.repositories.TagRepository import TagRepository


class SqlTagRepository(TagRepository):
    def __init__(self, session):
        self.session = session

    def add(self, tag: Tag) -> None:
        model = self.session.query(TagModel).filter_by(name=tag.name).first()
        if not model:
            model = TagModel(name=tag.name)
            self.session.add(model)
            self.session.flush()
            self.session.commit()
            tag._set_id(model.id)

    def remove(self, tag: Tag) -> None:
        model = self.session.get(TagModel, tag.id)
        if model:
            self.session.delete(model)
            self.session.commit()

    def get_by_name(self, tag_name:str) -> Tag:
        model = self.session.query(TagModel).filter_by(name=tag_name).first()

        if not model:
            raise NameNotFound(f'tag name {tag_name} not found.')

        tag = Tag(model.name, model.id)
        return tag