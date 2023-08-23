# from rest_framework import generics
# from .models import Apartment, SavedListing
# from .serializers import ApartmentSerializer
# from .filters import CustomFilter
# from django.http import JsonResponse
# from .models import SavedListing
#
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .filters import price_choices, bedroom_choices, state_choices, land_choices, bathroom_choices, office_choices
from .models import Apartment, Land, Offices


def index(request):
    apartment_listings = Apartment.objects.filter(is_published=True).order_by('-list_date')
    land_listings = Land.objects.filter(is_published=True).order_by('-list_date')
    office_listings = Offices.objects.filter(is_published=True).order_by('-list_date')


    all_listings = list(apartment_listings) + list(land_listings) + list(office_listings)

    paginator = Paginator(all_listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return JsonResponse(context)

def listing(request, listing_id):
    apartment_listing = get_object_or_404(Apartment, pk=listing_id)
    land_listing = get_object_or_404(Land, pk=listing_id)
    office_listings = Offices.objects.filter(is_published=True).order_by('-list_date')


    context = {
        'apartment_listing': {
            'id': apartment_listing.id,
            'title': apartment_listing.apart_name,

        },
        'land_listing': {
            'id': land_listing.id,
            'title': land_listing.land_name,

        },
        'office_listing': {
            'id': office_listings.id,
            'title': office_listings.office_name,

        }
    }

    return JsonResponse(context)

def search(request):

        apartment_queryset = Apartment.objects.order_by('-list_date')
        land_queryset = Land.objects.order_by('-list_date')
        office_queryset = Offices.objects.order_by('-list_date')
        queryset_list = apartment_queryset.union(land_queryset,office_queryset)

        # Keywords
        if 'keywords' in request.GET:
            keywords = request.GET['keywords']
            if keywords:
                queryset_list = queryset_list.filter(description__icontains=keywords)

        # City
        if 'city' in request.GET:
            city = request.GET['city']
            if city:
                queryset_list = queryset_list.filter(city__iexact=city)

        # State
        if 'state' in request.GET:
            state = request.GET['state']
            if state:
                queryset_list = queryset_list.filter(state__iexact=state)

        # Bedrooms
        if 'bedrooms' in request.GET:
            bedrooms = request.GET['bedrooms']
            if bedrooms:
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

        # Price
        if 'cost' in request.GET:
            cost = request.GET['cost']
            if cost:
                queryset_list = queryset_list.filter(cost__lte=cost)

        if 'size' in request.GET:
            size = request.GET['size']
            if size:
                queryset_list=queryset_list.filter(size__lte=size)

        listings = queryset_list.values()  # Convert QuerySet to list of dictionaries

        is_searching_for_land = request.GET.get('property_type') == 'land'
        is_searching_for_office = request.GET.get('property_type') == 'office'

        if is_searching_for_land:
            land_listings = [listing for listing in listings if listing['property_type'] == 'land']
            response_data = {
                'land_listings': land_listings,
                'state_choices': state_choices,
                'land_choices': land_choices,

                'values': request.GET
            }
        elif is_searching_for_office:
            office_listings = [listing for listing in listings if listing['property_type'] == 'office']
            response_data = {
                'office_listings': office_listings,
                'state_choices': state_choices,
                'office_choices': office_choices,
                'values': request.GET
            }
        else:
            response_data = {
                'apartment_listings': listings,
                'state_choices': state_choices,
                'bedroom_choices': bedroom_choices,
                'bathroom_choices':bathroom_choices,
                'price_choices': price_choices,
                'values': request.GET
            }

        return JsonResponse(response_data)



#
# class ApartmentList(generics.ListCreateAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#     filter_backends = [CustomFilter]
#
# class ApartmentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Apartment.objects.all()
#     serializer_class = ApartmentSerializer
#
#
#
# def add_favorite(request):
#     if request.method == 'POST':
#         listing_id = request.POST.get('id')
#         # Get the listing and user profiles
#         listing = Apartment.objects.get(pk=listing_id)
#         user_profile = request.user.userprofile
#
#         # Create a new SavedListing object
#         SavedListing.objects.create(user=user_profile, listing=listing)
#
#         return JsonResponse({'success': True})
#
# def remove_favorite(request):
#     if request.method == 'POST':
#         listing_id = request.POST.get('id')
#         # Get the listing and user profiles
#         listing = Apartment.objects.get(pk=listing_id)
#         user_profile = request.user.userprofile
#
#         # Remove the SavedListing object
#         saved_listing = SavedListing.objects.get(user=user_profile, listing=listing)
#         saved_listing.delete()
#
#         return JsonResponse({'success': True})
#
#
#
# def saved_listings(request):
#     if request.user.is_authenticated:
#         user_profile = request.user.userprofile
#         saved_listings = user_profile.saved_listings.all()
#
#         # Serialize the saved listings data into JSON
#         saved_listings_data = [
#             {
#                 'listing_id': saved_listing.listing.id,
#                 'listing_title': saved_listing.listing.title,
#                 # Add more fields as needed
#             }
#             for saved_listing in saved_listings
#         ]
#
#         return JsonResponse({'saved_listings': saved_listings_data})
#     else:
#         return JsonResponse({'error': 'User not logged in'})
