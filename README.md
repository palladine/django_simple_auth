# django_simple_auth
Simple base authentication (шаблон стандартной аутентификаци в Django).

#### Модель User была дополнена новым полем role.
 * в setting.py добавлена строка идентификации модели пользователей  
   ```python
   AUTH_USER_MODEL = 'base.User'
   ```
 * модель User унаследовала модель AbstractUser  
   ```python
   from django.contrib.auth.models import AbstractUser  
   ...  
   class User(AbstractUser):  
       ...  
   ```
 * первая миграция выполнена после описание модели пользователей