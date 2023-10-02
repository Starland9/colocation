from django.db import models

from django.contrib.gis.db import models as gis_models


# Create your models here.
class Room(models.Model):
    """Model definition for Room."""

    title = models.CharField(max_length=255)
    description = models.TextField()
    location = gis_models.PointField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    posted_by = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, null=True, blank=True
    )
    images = models.ManyToManyField(
        "rooms.RoomImage",
        related_name="rooms",
    )

    class Meta:
        """Meta definition for Room."""

        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        """Unicode representation of Room."""
        return self.title.__str__()


class RoomImage(models.Model):
    """Model definition for RoomImages."""

    room = models.ForeignKey(
        "rooms.Room", on_delete=models.CASCADE, null=True, blank=True
    )

    image = models.ImageField("Image", upload_to="room_images", null=True, blank=True)

    class Meta:
        """Meta definition for RoomImages."""

        verbose_name = "RoomImage"
        verbose_name_plural = "RoomImages"

    def __str__(self):
        return self.image.url
