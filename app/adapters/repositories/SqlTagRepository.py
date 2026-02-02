from app.adapters.Models.TagModel import TagModel
from app.core.entities.Tag import Tag
from app.domain.repositories.TagRepository import TagRepository


class SqlTagRepository(TagRepository):
    def __init__(self, session):
        self.session = session

    def add(self, tag: Tag) -> None:
        tag_model = self.session.query(TagModel).filter_by(name=tag.name).first()
        if not tag_model:
            tag_model = TagModel(name=tag.name)
            self.session.add(tag_model)
            self.session.flush()
            self.session.commit()
            tag.id = tag_model.id

    def remove(self, tag: Tag) -> None:
        tag_model = self.session.get(TagModel, tag.id)
        if tag_model:
            self.session.delete(tag_model)
            self.session.commit()

    def get_by_name(self, tag_name:str) -> Tag | None:
        tag_model = self.session.query(TagModel).filter_by(name=tag_name).first()

        if not tag_model:
            return None

        tag = Tag(tag_model.name)
        tag.id = tag_model.id
        return tag