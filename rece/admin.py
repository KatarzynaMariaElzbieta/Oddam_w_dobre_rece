from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, AdminPasswordChangeForm
from .models import User, Institution


# class UserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError("Passwords don't match")
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField()
#
#
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')
#
#     def clean_password(self):
#         return self.initial["password"]


class UserAdmin(UserAdmin):
    # form = UserChangeForm
    # add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'
    list_display = ('name', 'description', 'type', 'categories',)
    # fieldsets = (
    #
    # )
admin.site.register(User, UserAdmin)
admin.site.register(Institution)
admin.site.unregister(Group)
