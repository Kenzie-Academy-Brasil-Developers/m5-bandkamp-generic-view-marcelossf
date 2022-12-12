from django.db import models

# 1 Album pode ter várias Songs (1:N - ALBUM : SONGS)
class Song(models.Model):
    class Meta:
        ordering = ("id",)

    title = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)

    album = models.ForeignKey(
        "albums.Album",
        on_delete=models.CASCADE,
        related_name="songs",
    )
