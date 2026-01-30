from django.db import models


# About model to store information about the website
class About(models.Model):
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


# Contact model to store messages from users
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"


# FAQ model to store frequently asked questions
class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)  # for ordering questions

    def __str__(self):
        return self.question

    class Meta:
        ordering = ['order']  # ensures questions display in order


# NewsletterSubscriber model to store newsletter subscriptions
class NewsletterSubscriber(models.Model):
    name = models.CharField(max_length=100)       # <- add this
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
