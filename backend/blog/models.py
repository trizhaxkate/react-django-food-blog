from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            password=password,
            email=self.normalize_email(email)
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser):
    email = models.EmailField(default=None, verbose_name='email',max_length=60,unique=True)
    username = models.CharField(max_length=15, default=None, unique=True)
    first_name = models.CharField(verbose_name='First Name', max_length=30)
    last_name = models.CharField(verbose_name='Last Name', max_length=30)
    contact_number = models.CharField(verbose_name='Contact Number', max_length=20)
    avatar = models.ImageField(verbose_name='avatar', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name='Date Joined', auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] # Email & Password are required by default.

    objects = UserManager()
    
    def get_full_name(self):
        # The user is identified by their email address
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    # def create_staffuser(self, email, password):
    #     """
    #     Creates and saves a staff user with the given email and password.
    #     """
    #     user = self.create_user(
    #         email,
    #         password=password,
    #     )
    #     user.staff = True
    #     user.save(using=self._db)
    #     return user

# hook in the New Manager to our Model
# class User(AbstractBaseUser): # from step 2
#     ...
    


    # username = models.OneToOneField(User, default=1, on_delete=models.CASCADE)
    # USER_TYPE_CHOICES = (
    #   ('admin', 'admin'),
    #   ('guest', 'guest')
    # )
    # username = models.CharField(max_length=10, default=None)
    # user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=None)
    # is_admin = models.BooleanField(default=False)
    # user_image = models.ImageField()
    # user_image = models.ImageField(default=1)
    # password = models.CharField(max_length=20,default=None)
    # email = models.CharField(max_length=20, default=None)
    # first_name = models.CharField(max_length=20, default=None)
    # last_name = models.CharField(max_length=20, default=None)
    # contact_number = models.CharField(max_length=20, default=None)
    
    # USERNAME_FIELD = 'username'
    # PASSWORD_FIELD = 'password'
    # EMAIL_FIELD = 'email'
    # REQUIRED_FIELDS = []
    
    # def __str__(self):
    #     return self.username
    
    # class Meta:
    #     verbose_name_plural = 'Users'
        
        
class Category(models.Model):
    category_title = models.CharField(max_length=10)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name_plural = 'Categories'

class Recipe(models.Model):
    recipe_title = models.CharField(max_length=100)
    recipe_ingredient = models.TextField()
    recipe_timestamp = models.DateTimeField(auto_now_add=True)
    recipe_author = models.ForeignKey(Users, to_field="id", on_delete=models.CASCADE)
    recipe_image = models.ImageField()
    recipe_category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    recipe_duration =  models.CharField(max_length=20, default=None)
    recipe_serving =  models.CharField(max_length=20, default=None)
    recipe_description = models.TextField(default=None)
    
    def __str__(self):
        return self.recipe_title

    class Meta:
        verbose_name_plural = 'Recipes'


class Procedure(models.Model):
    instruction = models.TextField()
    recipe_id = models.ForeignKey(Recipe, related_name='procedures', default=None, on_delete=models.CASCADE)
    # procedure_id = models.AutoField(default=1, primary_key=True)

    
    def __str__(self):
        # return '%d: %s' % (self.recipe_order, self.instruction)
        return self.instruction
