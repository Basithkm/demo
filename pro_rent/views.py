from django.shortcuts import render,redirect
from .models import *
from pro_sale.models import *
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from PIL import Image as PilImage
from io import BytesIO


# Create your views here.


def product_filter(request):
    products = RentProperty.objects.filter(approved=True)

    # Filter by price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    category = request.GET.get('rent_category_head_name')
    sub_category = request.GET.get('type') 
    rent_category_head_name_late = request.GET.get('rent_category_head_name_late')

    if min_price:
        products = products.filter(approved=True,rent_price__gte=min_price)

    if max_price:
        products = products.filter(approved=True,rent_price__lte=max_price)



    if min_price and max_price:

        products = products.filter(approved=True,rent_price__range=(min_price, max_price))


    if category :
        products = products.filter(approved=True,rent_property_category__id=category
                                    ) 
    


    if sub_category :
        products = products.filter(approved=True,reny_type_category__id= sub_category)

   
    if rent_category_head_name_late:
        products = products.filter(approved=True,rent_property_category__rent_property_category=category
                                       )|products.filter(approved=True,reny_type_category__reny_type_category =rent_category_head_name_late)





        
    # Filter by category
    # category = request.GET.get('rent_category_head_name')
    # if category:
    #         products = products.filter(approved=True,rent_property_category__rent_property_category=category
    #                                    )|products.filter(approved=True,reny_type_category__reny_type_category =category)
            
    location = request.GET.get('rent_district_head_name')

    if location:
            products = products.filter(approved=True ,district__district_name=location
                                       )| products.filter(city__city_name =location)
        
        

    youare = request.GET.get('trogh')
    if youare:
        products = products.filter(approved=True,you_are__id=youare)

    rent_type_id = request.GET.get('rent_type')
    if rent_type_id:
        products = products.filter(approved=True,rent_type__id=rent_type_id)
    


    context = {'products': products}
    return render(request,'abcd.html',context)

    

def index(request):
    rent_category=RentPropertyCategory.objects.all()
    districts = District.objects.all()
    you_are =YouAre.objects.all()
    rent_type =RentType.objects.all()
    products =RentProperty.objects.filter(approved=True)
    
    context ={
            'rent_category':rent_category,
            'districts': districts,
            'you_are':you_are,
            'rent_type':rent_type,
            'products':products
            }
    return render(request,'index.html',context)



def locate_sale_autocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')
        # if SellProperty.objects.filter(approved=True):
        # Filter products based on search query
        
        products = SellProperty.objects.filter(
                approved=True,district__district_name__icontains=query
            ) | SellProperty.objects.filter(
                approved=True,city__city_name__icontains=query
            )

        # Create list of autocomplete data
        data = []
        for product in products:

            data.append(product.city.city_name)
            data.append(product.district.district_name)

            # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

            # Return data as JSON response
        return JsonResponse(data, safe=False)
    

def locate_rent_autocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')
        # if SellProperty.objects.filter(approved=True):
        # Filter products based on search query
        
        products = RentProperty.objects.filter(
                approved=True,district__district_name__icontains=query
            ) | RentProperty.objects.filter(
                approved=True,city__city_name__icontains=query
            )

        # Create list of autocomplete data
        data = []
        for product in products:

            data.append(product.city.city_name)
            data.append(product.district.district_name)

            # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

            # Return data as JSON response
        return JsonResponse(data, safe=False)



def category_rent_autocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')
        # if SellProperty.objects.filter(approved=True):
        # Filter products based on search query
        
        products = RentProperty.objects.filter(
                approved=True,rent_property_category__rent_property_category__icontains=query
            ) | RentProperty.objects.filter(
                approved=True,reny_type_category__reny_type_category__icontains=query
            )

        # Create list of autocomplete data
        data = []
        for product in products:

            data.append(product.rent_property_category.rent_property_category)
            data.append(product.reny_type_category.reny_type_category)

            # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

            # Return data as JSON response
        return JsonResponse(data, safe=False)
    

    
def category_sale_autocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')
        # if SellProperty.objects.filter(approved=True):
        # Filter products based on search query
        
        products = SellProperty.objects.filter(
                approved=True,rent_property_category__rent_property_category__icontains=query
            ) | SellProperty.objects.filter(
                approved=True,reny_type_category__reny_type_category__icontains=query
            )

        # Create list of autocomplete data
        data = []
        for product in products:
            data.append(product.rent_property_category.rent_property_category)
            data.append(product.reny_type_category.reny_type_category)

            # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

            # Return data as JSON response
        return JsonResponse(data, safe=False)
    




def spaceautocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')

        # Filter products based on search query
        products = RentProperty.objects.filter(
            approved=True,rent_title__icontains=query
        )

        data = []
        for product in products:
            data.append(product.rent_title)
            

        # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

        # Return data as JSON response
        return JsonResponse(data, safe=False)
    


def search(request):
    rent_category=RentPropertyCategory.objects.all()
    districts = District.objects.all()
    you_are =YouAre.objects.all()
    rent_type =RentType.objects.all()
    
    form = RentProperty.objects.filter(approved=True)
    if request.method == 'GET':
 
        # Retrieve search query from GET request
        query = request.GET.get('query', '')

        # Filter products based on search query
        products = RentProperty.objects.filter(
            approved=True,rent_title__icontains=query)

        context = {
            'rent_category':rent_category,
            'districts': districts,
            'you_are':you_are,
            'rent_type':rent_type,
            'products':products,
            'form':form
        }
        return render(request,'property_for_rent.html', context)
    context = {
            'rent_category':rent_category,
            'districts': districts,
            'you_are':you_are,
            'rent_type':rent_type,
            'form':products,
 
        }
    return render(request,'property_for_rent.html', context)





def property_for_rent(request):
    rent_category=RentPropertyCategory.objects.all()
    districts = District.objects.all()
    you_are =YouAre.objects.all()
    rent_type =RentType.objects.all()
    
    form =RentProperty.objects.filter(approved=True)

   
    if request.method == 'POST':
        you_are_id = request.POST.get('you_are', None)
        rent_type_id =request.POST.get('rent_type', None)



        you_are_id =request.POST['you_are']
        rent_type_id =request.POST['rent_type']
        

        get_you_are_id =YouAre.objects.get(id=you_are_id)
        name_get_you_are_id= get_you_are_id.you_are

        get_rent_type_id =RentType.objects.get(id=rent_type_id)
        name_get_rent_type_id= get_rent_type_id.rent_type_name

        if name_get_you_are_id and name_get_rent_type_id :
            products = RentProperty.objects.filter(Q(approved=True,you_are__you_are__icontains=name_get_you_are_id
                                                     )& Q(approved=True,rent_type__rent_type_name__icontains=name_get_rent_type_id
                                                          ))
            context= {
                'products':products,'youare':you_are,'rent_type':rent_type,'form':form
            }
            return render(request,'property_for_rent.html',context)
        
        elif name_get_you_are_id and name_get_rent_type_id:
            products = RentProperty.objects.filter(Q(approved=True,you_are__you_are__icontains=name_get_you_are_id
                                                     )& Q(approved=True,rent_type__rent_type_name__icontains=name_get_rent_type_id
                                                          ))                                                      
            
            context= {
                'products':products,'youare':you_are,'rent_type':rent_type,'form':form
            }
            return render(request,'property_for_rent.html',context)

    context ={
            'rent_category':rent_category,
            'districts': districts,
            'you_are':you_are,
            'form':form,
            'rent_type':rent_type
            }
    return render(request,'property_for_rent.html',context)


def get_rent_property(request,id):
    get_sale_property =RentProperty.objects.get(id=id)
    other_property = RentProperty.objects.filter(approved=True,reny_type_category=get_sale_property.reny_type_category).exclude(id=get_sale_property.id)
    if request.method=="POST":
        if request.user.is_authenticated:
            user =request.user
            get_sale_property =RentProperty.objects.get(id=id)
            full_name =request.POST['full_name']
            phone =request.POST['phone']
            email =request.POST['email']
            intrest =request.POST['intrest']
            file =RentMessages(user=user,sale_property=get_sale_property,full_name=full_name,phone=phone,email=email,intrest=intrest)
            file.save()
            messages.success(request,'message successfully ,our teams will you contact immeadiatly')
            return redirect('property_for_rent')
        else:
            url = reverse('signin') 
            return redirect(url)
    return render(request,'get_rent_property.html',{'get_property':get_sale_property,'other_property':other_property})
    



def my_rent_properies(request,id):
    if request.user.is_authenticated:
        user = request.user
        get_rent_property =RentProperty.objects.get(id=id)
        context ={
            'get_property':get_rent_property
        }
        return render(request,'my_rent_properies.html',context)
    else:
        url = reverse('signin') 
        return redirect(url)
    

def daily_rent(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.daily_rent = request.POST['daily_rent']
            person.save()
            messages.success(request,'property added successfully ')
            return redirect('index')
        return render(request,'rent/residenteial_purpose/rent_type/daily_rent.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def monthly_rent(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.monthly_rent = request.POST['monthly_rent']
            person.save()
            messages.success(request,'property added successfully ')
            return redirect('index')
        return render(request,'rent/residenteial_purpose/rent_type/monthly_rent.html')
    else:
        url = reverse('signin') 
        return redirect(url)
    


def lease_rent(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.lease_rent = request.POST['lease_rent']
            person.save()
            messages.success(request,' property added successfully ')
            return redirect('index')
        return render(request,'rent/residenteial_purpose/rent_type/lease_rent.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def flatmate(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.monthly_rent = request.POST['monthly_rent']
            person.number_of_persons = request.POST['number_of_persons']
            person.num_of_bathrooms = request.POST['number_of_bathrooms']
            person.number_of_beds = request.POST['number_of_beds']
            person.save()
            messages.success(request,' please complete your property details ')
            return redirect('you_are',pk=person.id)
        return render(request,'rent/residenteial_purpose/rent_type/flatmate.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def rent_type(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        rent_type=RentType.objects.all()
        if request.method == 'POST':
            rent_type_id = request.POST['rent_type']
            a=person.rent_type=RentType.objects.get(id=rent_type_id)
            person.save()
            messages.success(request,' please complete your property details ')
            if a.rent_type_name == "Daily":
                return redirect('daily_rent',pk=person.id)
            elif a.rent_type_name == "Monthly":
                return redirect('monthly_rent',pk=person.id)
            elif a.rent_type_name == "Lease":
                return redirect('lease_rent',pk=person.id)
            else :
                return redirect('index')

        return render(request,'rent/residenteial_purpose/rent_type/rent_type.html',{'rent_type':rent_type})
    else:
        url = reverse('signin') 
        return redirect(url)



def you_are_form(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.agent_name = request.POST['agent_name']
            person.agent_company = request.POST['agent_company']
            person.save()
            messages.success(request,' please complete your property details ')
            return redirect('rent_type',pk=person.id)
        return render(request,'rent/residenteial_purpose/you_are_form.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def you_are(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        you_are =YouAre.objects.all()
        if request.method == 'POST':
            you_are_id = request.POST['you_are']
            a=person.you_are =YouAre.objects.get(id=you_are_id)
            person.save() 
            messages.success(request,' please complete your property details ')
            if a.you_are == "Agent":
                return redirect('you_are_form',pk=person.id)
            else:
                return redirect('rent_type',pk=person.id)
        return render(request,'rent/residenteial_purpose/you_are.html',{'youare':you_are})
    else:
        url = reverse('signin') 
        return redirect(url)

from PIL import Image as PILImage

def residenteial_purpose(request,pk):
    if request.user.is_authenticated:
        user =request.user
        person = get_object_or_404(RentProperty,id=pk)
        if person.reny_type_category.reny_type_category == "Flatmate(Room mate)":
            if request.method == 'POST':
                person.property_name = request.POST['propertyName']
                person.rent_image=request.FILES['image']

                # person.image1 = request.GET.get('image1')

                person.rent_price=request.POST['price']
                person.number_of_persons = request.POST['number_of_persons']
                person.num_of_bathrooms = request.POST['number_of_bathrooms']
                person.number_of_beds = request.POST['number_of_beds']
                person.extras = ", ".join(request.POST.getlist('amenities'))
                person.save()

                for image_file in request.FILES.getlist('images'):  
                  RentMultipleImages.objects.create(user =user,rent_property =person, images=image_file)

                messages.success(request,' please complete your property details ')
                return redirect('you_are',pk=person.id)
            return render(request,'rent/residenteial_purpose/rent_type/flatmate.html')
        elif request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.num_of_rooms = request.POST['numRooms']
            person.num_of_bathrooms = request.POST['numBathrooms']
            person.balcony = request.POST['balcony']
            person.rent_image=request.FILES['image']

            # person.image1 = request.GET.get('image1')

            person.furnished = request.POST['furnished']
            person.rent_size_in_squrefeet =request.POST['propertySqft']
            person.rent_price=request.POST['price']
            person.rent_description=request.POST['description']
            person.extras = ", ".join(request.POST.getlist('amenities'))
            person.save()

            for image_file in request.FILES.getlist('images'):  
               RentMultipleImages.objects.create(user =user,rent_property =person, images=image_file)

            messages.success(request,' please complete your property details ')
            return redirect('you_are',pk=person.id)
        return render(request,'rent/residenteial_purpose/residenteial_purpose.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def commertial_purpose(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(RentProperty,id=pk)
        user =request.user
        if request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.admin_area = request.POST['admin_area']
            person.confrence_room = request.POST['confrence_room']
            person.num_of_bathrooms = request.POST['numBathrooms']
            person.balcony = request.POST['balcony']
            person.rent_image=request.FILES['image']

            

            person.furnished = request.POST['furnished']
            person.rent_size_in_squrefeet =request.POST['propertySqft']
            person.rent_price=request.POST['price']
            person.rent_description=request.POST['description']
            person.extras = ", ".join(request.POST.getlist('amenities'))
            person.save()

            for image_file in request.FILES.getlist('images'):  
               RentMultipleImages.objects.create(user =user,rent_property =person, images=image_file)
            
            messages.success(request,' please complete your property details ')
            return redirect('you_are',pk=person.id)
        return render(request,'rent/commertial_purpose/commertial_purpose.html')
    else:
        url = reverse('signin') 
        return redirect(url)

def land_view(request,pk):
    if request.user.is_authenticated:
        user =request.user
        person = get_object_or_404(RentProperty,id=pk)
        if request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.type_of_soil = request.POST['type_of_soil']
            person.rent_price=request.POST['price']
            person.rent_description = request.POST['description']
            person.property_acre = request.POST['property_acre']
            person.rent_image=request.FILES['image']

            # person.image1 = request.GET.get('image1')

            person.save()

            for image_file in request.FILES.getlist('images'):  
               RentMultipleImages.objects.create(user =user,rent_property =person, images=image_file)

            messages.success(request,' please complete your property details ')
            return redirect('you_are',pk=person.id)
        return render(request,'rent/land/land_view.html')
    else:
        url = reverse('signin') 
        return redirect(url)


def post_free_add_property_for_rent(request):
    if request.user.is_authenticated:
        rent_category=RentPropertyCategory.objects.all()
        districts = District.objects.all()
        if request.method == 'POST':
            try: 
                rent_category_id = request.POST['rent_category']
                type_id =request.POST['type']
                rent_title = request.POST['name']
                district_id = request.POST['district']
                city_id = request.POST['city']
                user =request.user
            except MultiValueDictKeyError:
                return HttpResponse('Error: Form data is missing or invalid')
            rent_category = RentPropertyCategory.objects.get(id=rent_category_id)
            type =RentTypeCategory.objects.get(id=type_id)
            district = District.objects.get(id=district_id)
            city = City.objects.get(id=city_id)
            prod=RentProperty(user =user,reny_type_category=type,rent_title=rent_title,rent_property_category=rent_category,district=district,city=city)
            prod.save()
            messages.success(request,' please complete your property details ')
            if rent_category.rent_property_category == 'Residenteial Purpose':
                return redirect('residenteial_purpose',pk=prod.id)
            
            elif rent_category.rent_property_category== 'Commertial Purpose':
                return redirect('commertial_purpose',pk=prod.id)
            
            elif rent_category.rent_property_category=='Land':
                return redirect('land_view',pk=prod.id)
            else:
                return redirect('residenteial_purpose',pk=prod.id)

        else:
            context ={
            'rent_category':rent_category,
            'districts': districts,
            }
        return render(request,'post_free_add_property_for_rent.html',context)
    

    else:
        url = reverse('signin') 
        return redirect(url)
    
def get_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district__id=district_id)
    city_data = {}
    for city in cities:
        city_data[city.id] = city.city_name
    return JsonResponse(city_data)


def get_types(request):
    rent_category_id = request.GET.get('rent_category_id')
    rent_categories = RentTypeCategory.objects.filter(rent_property_category__id=rent_category_id)
    rent_categories_data= {}
    for rent_categories in rent_categories:
        rent_categories_data[rent_categories.id] = rent_categories.reny_type_category
    return JsonResponse(rent_categories_data)



def delete_your_rent_property(request,id):
    if request.user.is_authenticated:
        datas =RentProperty.objects.get(pk=id)
        datas.delete()
        messages.success(request,' Property deleted successfully ')
        return redirect('property_for_rent')
    else:
        url = reverse('signin') 
        return redirect(url)
    