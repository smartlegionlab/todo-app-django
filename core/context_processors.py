from core.models import AppSetting


def app_settings(request):
    app_setting = AppSetting.objects.first()
    return {'app_setting': app_setting}
