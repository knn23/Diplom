# statistics/apps.py

from django.apps import AppConfig


class StatisticsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stats'

    def ready(self):
        import stats.signals
