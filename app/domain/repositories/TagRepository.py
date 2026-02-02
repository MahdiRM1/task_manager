from abc import ABC, abstractmethod

from app.core.entities.Tag import Tag


class TagRepository(ABC):

    @abstractmethod
    def add(self, tag: Tag) -> None:
        pass

    @abstractmethod
    def remove(self, tag: Tag) -> None:
        pass

    @abstractmethod
    def get_by_name(self, tag_name:str) -> Tag | None:
        pass