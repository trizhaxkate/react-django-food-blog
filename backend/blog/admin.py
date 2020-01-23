from django.contrib import admin
from .models import Recipe, Users, Category, Procedure
from django import forms
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class ProcedureInline(admin.TabularInline):
    model = Procedure
    extra = 3

class RecipeAdmin(admin.ModelAdmin):

    inlines = [ProcedureInline]
    list_display = ('recipe_title', 'recipe_timestamp')

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, help_text="Enter the same password as before, for verification.")

    class Meta:
        model = Users
        fields = ('username', 'email')
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two Passwords didn't match")
        return password2
    
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class UsersAdmin(UserAdmin):
    add_form = UserCreationForm
    
    list_display = ('username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ('date_joined',)
    fieldsets = ()
    add_fieldsets = (
        ('Account Information', {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'username', 'email', 'contact_number', 'password1', 'password2', 'avatar'),
        }),
        ('Privileges', {
            'classes': ('wide',),
            'fields': ('is_admin', 'is_staff')
        })
    )
    
admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Procedure)
admin.site.register(Users, UsersAdmin)