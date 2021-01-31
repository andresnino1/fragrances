from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', ]
    # fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    # add_fieldsets = UserAdmin.add_fieldsets + ((None,{'fields':('age',)}),)

#this class shows the comments of each fragrance in fragrances models
class CommentInline(admin.TabularInline):
    model = CommentsModel

class FragrancesAdmin(admin.ModelAdmin):
    inlines = [CommentInline,
               ]


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(ApplicationModel)
admin.site.register(FirstFamilyModel)
admin.site.register(SecondFamilyModel)
admin.site.register(ThirdFamilyModel)
admin.site.register(TechnologyModel)
admin.site.register(CollectionModel)
admin.site.register(NaturalExtractsModel)
admin.site.register(MarketTypeModel)
admin.site.register(NotaSalidaModel)
admin.site.register(NotaCuerpoModel)
admin.site.register(NotaFondoModel)
admin.site.register(CommentsModel)
admin.site.register(FragrancesModel,FragrancesAdmin)
