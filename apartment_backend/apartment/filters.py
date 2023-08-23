from rest_framework import filters

bedroom_choices = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10
}
land_choices = {
    '1': 10000,
    '2': 20000,
    '4': 30000,
    '5': 70000
}
bathroom_choices = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
}
office_choices = {
    '1':100000,
    '2':200000,
    '3':500000,
    '4':400000,
}
price_choices = {
    '100000': '$100,000',
    '200000': '$200,000',
    '300000': '$300,000',
    '400000': '$400,000',
    '500000': '$500,000',
    '600000': '$600,000',
    '700000': '$700,000',
    '800000': '$800,000',
    '900000': '$900,000',
    '1000000': '$1M+',
}

state_choices = {

    'NAI': 'Nairobi',
    'KIS': 'Kisumu',
    'MSA': 'Mombasa',
    'ELD': 'Eldoret',
    'GAR':  'Garissa',


}
class CustomFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        location = request.query_params.get('location')
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        property_type = request.query_params.get('property_type')
        min_bedrooms = request.query_params.get('min_bedrooms')
        min_bathrooms = request.query_params.get('min_bathrooms')

        if location:
            queryset = queryset.filter(address__icontains=location)
        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if property_type:
            queryset = queryset.filter(property_type=property_type)
        if min_bedrooms:
            queryset = queryset.filter(bedrooms__gte=min_bedrooms)
        if min_bathrooms:
            queryset = queryset.filter(bathrooms__gte=min_bathrooms)

        return queryset





