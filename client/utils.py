from .models import ServiceInfo


def get_cas_token():
    services = ServiceInfo.objects.filter(is_cas=True)
    if services.count() > 0:
        return services.first().token
    else:
        return None
