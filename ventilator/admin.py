
from django.contrib import admin
from . models import Booking, Department, Doc

class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_email', 'p_phone', 'd_name', 'booking_date', 'booked_on')
admin.site.register(Department)
admin.site.register(Doc)
admin.site.register(Booking, BookingAdmin)