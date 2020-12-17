"""
The isdir, files and file defs make sure that nobody uses ..
in the path name to break out of the defined filesystem area.
"""

from django.db import models
import mimetypes
import os


class Filesystem(models.Model):
    name = models.CharField(max_length=64)
    path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self, name):
        self.path = os.path.abspath(os.path.realpath(name))
        return self.path

    def isdir(self, path):
        # Check whether a given path below the filesystem is a directory or not
        p = os.path.realpath(os.path.join(self.path, path))
        if not p.startswith(self.path):
            raise ValueError(path)
        return os.path.isdir(p)

    def files(self, path=''):
        # Returns the files of the given path below the filesystems base path
        p = os.path.realpath(os.path.join(self.path, path))

        if not p.startswith(self.path):
            raise ValueError(path)

        dirs = os.listdir(p)
        if path:
            dirs.insert(0, '..')
            return [
                (f, os.path.isdir(os.path.join(p, f)),
                 mimetypes.guess_type(f)[0] or
                 'application/octetstream')
                for f in dirs]

    def file(self, path):
        # return the real pathname and the mimetype of a given file below the
        # filesystems base path
        p = os.path.realpath(os.path.join(self.path, path))
        if p.startswith(self.path):
            (t, e) = mimetypes.guess_type(p)
            return p, t or 'application/octetstream'
        else:
            raise ValueError(path)
