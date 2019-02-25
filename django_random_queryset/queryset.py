# encoding: utf-8

from django.db import models
from django.db.models import Min, Max, Count

from django_random_queryset import strategies


class RandomQuerySet(models.query.QuerySet):

    def random(self, amount=1):
        aggregates = self.aggregate(min_id=Min('id'), max_id=Max('id'), count=Count('id'))

        if not aggregates['count']:
            return self.none()

        if aggregates['count'] <= amount:
            return self.all()

        if (aggregates['max_id'] - aggregates['min_id']) + 1 == aggregates['count']:
            return self.filter(id__in=strategies.min_max(
                amount,
                aggregates['min_id'],
                aggregates['max_id'],
                aggregates['count'],
            ))

        # list of all id's
        ids = self.values_list('id', flat=True)
        selected_ids = strategies.random_count(ids, amount=amount)

        return self.filter(id__in=selected_ids)
