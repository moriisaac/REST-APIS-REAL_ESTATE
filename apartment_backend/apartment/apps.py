from django.apps import AppConfig



class ApartmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apartment'
    # def ready(self):
    #     from .signals import save_user_profile, create_user_profile
    #     User = self.get_model('UserProfile')
    #     save_user_profile(save_user_profile,sender=User)
    #     create_user_profile(create_user_profile,sender=User)



