from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        def __unicode__(self):
            return 'Profile: %s %s' % (self.user.first_name, self.user.last_name)
