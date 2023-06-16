from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"Grade: {self.value} for user {self.user.username}"

    def add_to_group(self, group_name):
        group, created = Group.objects.get_or_create(name=group_name)
        self.group = group
        self.save()

    def remove_from_group(self):
        if self.group:
            self.group = None
            self.save()

    @staticmethod
    def create_group(name):
        Group.objects.create(name=name)

    @staticmethod
    def delete_group(name):
        Group.objects.filter(name=name).delete()

    def save(self, *args, **kwargs):
        if not self.pk:
            send_mail(
                'New Grade',
                f'You have a new grade: {self.value}',
                settings.EMAIL_HOST_USER,
                [self.user.email],
                fail_silently=False,
            )

        super(Grade, self).save(*args, **kwargs)


class LessonPlan(models.Model):
    teacher = models.ForeignKey(
        User,
        limit_choices_to={'is_staff': True},
        on_delete=models.CASCADE
    )
    date = models.DateField()
    time = models.TimeField()
    participants = models.ManyToManyField(User, related_name='lesson_participants',
                                          limit_choices_to={'is_staff': False})

    lesson_type = models.CharField(max_length=100)

    def __str__(self):
        return f"Lesson Plan on {self.date} at {self.time}"

    class Meta:
        verbose_name_plural = 'Lesson Plans'
