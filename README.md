# django_simple_auth
Simple base authentication (шаблон стандартной аутентификации в Django).

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
 * первая миграция выполнена после описания модели пользователей
 
 * Варианты:  
    __AbstractUser__: Наследуемся от этого класса, если нас устраивают существующие поля в модели User.  
    __AbstractBaseUser__: Наследуемся от этого класса, если нам необходимо создать собственную, новую модель User.
