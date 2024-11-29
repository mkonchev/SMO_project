from src.source_dir.source import Sourse


class SourceList(object):
    source_list = list[Sourse]

    def __init__(self, source_count: int, a: int, b: int):
        self.source_list = [Sourse(i, a, b) for i in range(source_count)]

    def get_source_by_id(self, id_: int) -> Sourse:
        for source in self.source_list:
            if source.get_id() == id_:
                return source
