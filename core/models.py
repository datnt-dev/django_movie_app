from django.db import models


class Movie(models.Model):
    NOT_RATE = 0
    RATE_G = 1
    RATE_PG = 2
    RATE_R = 3
    RATINGS = (
        (NOT_RATE, 'NR - Not Rated'),
        (RATE_G, 'G - General Audiences'),
        (RATE_PG, 'PG - Parental Guidance'),
        (RATE_R, 'R - Restricted'),
    )

    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATE)
    runtime = models.PositiveIntegerField()
    website = models.URLField(
        blank=True
    )

    def __str__(self):
        return f'{self.title} ({self.year})'
