from django.contrib import admin
from app.models import State, City, Hospital, Service
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Hospital)
def afterHospitalSave(signal, instance, **kwargs):
    service = Service(hospital=instance)
    service.save()

class ServiceAdmin(admin.ModelAdmin):
    model=Service
    list_display=['hospital',
                    'oxygen_beds',
                    'oxygen_cylinder',
                    'oxygen_ventilator',
                    
                    
                    ]

    def oxygen_beds(self, object):
        return f'{object.oxygen_beds_available}/{object.oxygen_beds_total}'
    
    def oxygen_cylinder(self, object):
        return f'{object.oxygen_cylinder_available}/{object.oxygen_cylinder_total}'

    def oxygen_ventilator(self, object):
        return f'{object.ventilator_available}/{object.ventilator_total}'


# Register your models here.

admin.site.register(State)
admin.site.register(City)
admin.site.register(Hospital)
admin.site.register(Service)