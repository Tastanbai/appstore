from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name='Пользователи'

    class Meta:
        db_table ='user'
        verbose_name ='Пользователя'
        verbose_name_plural='Пользователи'

    def __str__(self):
        return self.username