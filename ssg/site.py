from os import mkdir
from pathlib import Path

class Site:

    def Site(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = Path(self.dest + '/' + relative_to(path))
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        (self.dest).mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
