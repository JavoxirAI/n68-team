from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class ContactModel(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} => {self.email}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class AboutPageModel(models.Model):
    bio = RichTextUploadingField()
