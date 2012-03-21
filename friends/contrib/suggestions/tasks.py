from celery.registry import tasks

from friends.contrib.suggestions.backends import importers
from friends.contrib.suggestions.backends.runners import AsyncRunner
from friends.contrib.suggestions.settings import RUNNER

if issubclass(RUNNER, AsyncRunner):
    tasks.register(importers.GoogleImporter)

