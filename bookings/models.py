from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from simple_email_confirmation import SimpleEmailConfirmationUserMixin
from django.core import validators


class TimeRange(models.Model):
    start = models.TimeField()
    end = models.TimeField()

    def __unicode__(self):
        return "{} - {}".format(self.start, self.end)


class AvailabilityCalender(models.Model):
    name = models.CharField(max_length=30)
    monday = models.BooleanField(default=True)
    tuesday = models.BooleanField(default=True)
    wednesday = models.BooleanField(default=True)
    thursday = models.BooleanField(default=True)
    friday = models.BooleanField(default=True)
    saturday = models.BooleanField(default=True)
    sunday = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class StoreClosedDates(models.Model):
    date = models.DateField(null=True)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return "{}: {}".format(self.name, self.date)


class BaseUser(AbstractBaseUser, PermissionsMixin, SimpleEmailConfirmationUserMixin):
    username = models.CharField(_('username'), max_length=30, unique=True, help_text=_('Required. 30 characters or '
                                                                                       'fewer. Letters, digits and '
                                                                                       '@/./+/-/_ only.'),
                                validators=[validators.RegexValidator(r'^[\w.@+-]+$',
                                                                      _('Enter a valid username. This value may '
                                                                        'contain only letters, numbers and @/./+/-/_ '
                                                                        'characters.'), 'invalid')],
                                error_messages={'unique': _("A user with that username already exists.")})
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log '
                                                                                 'into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True, help_text=_('Designates whether this user should be '
                                                                           'treated as active. Unselect this instead '
                                                                           'of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    phone = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=10)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """ Returns the first_name plus the last_name, with a space in between. """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """ Returns the short name for the user. """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Sends an email to this User. """
        send_mail(subject, message, from_email, [self.email])


class Service(models.Model):
    time_slots = models.ManyToManyField(TimeRange)
    availability = models.ForeignKey(AvailabilityCalender)
    name = models.CharField(max_length=30)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()

    def __unicode__(self):
        return self.name

    @property
    def price(self):
        return "${}".format(self.cost)


class Booking(models.Model):
    BOOKING_STATUS = (
        ('CF', 'Confirmed'),
        ('CM', 'Completed'),
        ('UF', 'Unfulfilled'),
        ('CN', 'Canceled'),
    )

    customer = models.ForeignKey(BaseUser, related_name='customer')
    service = models.ForeignKey(Service)
    service_employee = models.ForeignKey(BaseUser, related_name='employee')
    booking_day = models.DateField(null=True)
    booking_time = models.TimeField(null=True)
    status = models.CharField(choices=BOOKING_STATUS, default=BOOKING_STATUS[0], max_length=20)
    additional_information = models.TextField()
    registration_number = models.CharField(max_length=10, null=True)

    def __unicode__(self):
        return "{}'s booking".format(self.customer.first_name)



