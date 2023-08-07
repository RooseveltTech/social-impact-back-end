from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def get_ip_address(request):
    # Get IP ADDRESS
    address = request.META.get('HTTP_X_FORWARDED_FOR')
    if address:
        ip_addr = address.split(',')[-1].strip()
    else:
        ip_addr = request.META.get('REMOTE_ADDR')
    
    return ip_addr

def get_aqi_status(aqi):
    if aqi <= 50:
        return "Good", "bg-success", "Air quality is considered satisfactory, and air pollution poses little or no risk"
    elif aqi <= 100:
        return "Moderate", "bg-warning", "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups", "bg-orange", "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
    elif aqi <= 200:
        return "Unhealthy", "bg-danger", "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion"
    elif aqi <= 300:
        return "Very Unhealthy", "bg-purple", "Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion."
    else:
        return "Hazardous", "bg-maroon", "Everyone should avoid all outdoor exertion"
    
class CustomPaginator:
    @staticmethod
    def paginate(request, queryset, page):
        # request_get_data = request.GET

        # queryset_size = 30
        # if int(page) > 1:
        #     queryset_size = 20

        paginator = Paginator(queryset, per_page=10)

        try:
            paginated_data = paginator.page(page)
        except PageNotAnInteger:
            paginated_data = paginator.page(1)
        except EmptyPage:
            paginated_data = []

        return paginated_data