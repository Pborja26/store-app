from django.contrib import admin

# Register your models here.
class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by', 'created_at', 'updated_by', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in instances:
            if obj._state.adding:
                obj.created_by = request.user
            obj.updated_by = request.user
            obj.save()
        for obj in formset.deleted_objects:
            obj.delete()
        formset.save_m2m()