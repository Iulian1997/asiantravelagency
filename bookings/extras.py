from django.conf import settings
import random
import string
from datetime import date
import datetime
from bookings.models import Booking

def generate_ref_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str