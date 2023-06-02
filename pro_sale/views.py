from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from pro_rent.models import *
import os
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q



# Create your views here.





def sale_product_filter(request):
    products = SellProperty.objects.filter(approved=True)

    # Filter by price
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        products = products.filter(approved=True,rent_price__gte=min_price)

    if max_price:
        products = products.filter(approved=True,rent_price__lte=max_price)



    if min_price and max_price:

        products = products.filter(approved=True,rent_price__range=(min_price, max_price))

        
    # Filter by category

    category = request.GET.get('rent_category_head_name')
    sub_category = request.GET.get('type')   
    rent_category_head_name_late = request.GET.get('rent_category_head_name_late')   
    



    if category :
        products = products.filter(approved=True,rent_property_category__id=category
                                    ) 
    


    if sub_category :
        products = products.filter(approved=True,reny_type_category__id= sub_category)

   
    if rent_category_head_name_late:
        products = products.filter(approved=True,rent_property_category__rent_property_category=category
                                       )|products.filter(approved=True,reny_type_category__reny_type_category =rent_category_head_name_late)






    # if category and sub_category:
    #         products = products.filter(approved=True,rent_property_category__rent_property_category=category
    #                                    ) | products.filter(approved=True,reny_type_category__reny_type_category = sub_category)
    

    # sub_category = request.GET.get('type')        
    # if sub_category:
    #     products =products.filter(approved=True,reny_type_category__reny_type_category = sub_category)
    

    location = request.GET.get('rent_district_head_name')
    if location:
            products = products.filter(approved=True ,district__district_name=location
                                       )| products.filter(city__city_name =location)
        
        

    youare = request.GET.get('trogh')
    if youare:
        products = products.filter(approved=True,you_are__id=youare)

 


    context = {'products': products,
               }
    return render(request,'sale.html',context)


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
    

def property_for_sale(request):
    rent_category=RentPropertyCategory.objects.all()
    districts = District.objects.all()
    you_are =YouAre.objects.all()
    form = SellProperty.objects.filter(approved=True)
    if request.method == 'POST':
        youare =request.POST.get('youare', None)
        if youare is not None:
            get_you_are_id =YouAre.objects.get(id=youare)
            name_get_you_are_id = get_you_are_id.you_are

        if name_get_you_are_id:
            products = SellProperty.objects.filter(Q(approved=True,you_are__you_are__icontains=name_get_you_are_id
                                                     ))
            context= {
                'form':products,
                'youare':you_are
            }
            return render(request,'property_for_sale.html',context)


    context ={
            'rent_category':rent_category,
            'districts': districts,
            'youare':you_are,
            'form':form,
            }
    return render(request,'property_for_sale.html',context)


def salesearch(request):
    rent_category=RentPropertyCategory.objects.all()
    districts = District.objects.all()
    you_are =YouAre.objects.all()
    form = SellProperty.objects.filter(approved =True)
  
    if request.method == 'GET':
          # Retrieve search query from GET request
        query = request.GET.get('query', '')

            # Filter products based on search query
        products = SellProperty.objects.filter(approved=True,
                rent_title__icontains=query)

        context = {
                'sale_products': products,
                'rent_category':rent_category,
                'districts': districts,
                'youare':you_are,
                'form':form
            }
        return render(request, 'property_for_sale.html', context)
    context = {
            'rent_category':rent_category,
            'districts': districts,
            'youare':you_are,
            'form':products,
 
        }
    return render(request,'property_for_rent.html', context)



def saleautocomplete(request):
    if request.method == 'GET':
        # Retrieve search query from GET request
        query = request.GET.get('term', '')

        # if SellProperty.objects.filter(approved=True):
        # Filter products based on search query
        
        products = SellProperty.objects.filter(approved=True,rent_title__icontains=query)

        # Create list of autocomplete data
        data = []
        for product in products:
            data.append(product.rent_title)
            # Remove duplicates and empty strings
        data = list(set(filter(None, data)))

            # Return data as JSON response
        return JsonResponse(data, safe=False)



def get_sale_property(request,id):
    get_sale_property =SellProperty.objects.get(id=id)
    other_property = SellProperty.objects.filter(approved=True,reny_type_category=get_sale_property.reny_type_category).exclude(id=get_sale_property.id)
    if request.method=="POST":
        if request.user.is_authenticated:
            user = request.user
            get_sale_property =SellProperty.objects.get(id=id)
            full_name =request.POST['full_name']
            phone =request.POST['phone']
            email =request.POST['email']
            intrest =request.POST['intrest']
            file =SaleMessages(user=user,sale_property=get_sale_property,full_name=full_name,phone=phone,email=email,intrest=intrest)
            file.save()
            messages.success(request,'message successfully ,our teams will contact immeadiatly')
            return redirect('property_for_sale')
        else:
            url = reverse('signin') 
            return redirect(url)
    
    return render(request,'get_sale_property.html',{'get_property':get_sale_property,'other_property':other_property})


def get_my_sale_properies(request,id):
    if request.user.is_authenticated:
        user = request.user
        get_sale_property =SellProperty.objects.get(id=id)
        context ={
            'get_property':get_sale_property
        }
        return render(request,'my_sale_properies.html',context)
    else:
        url = reverse('signin') 
        return redirect(url)
    
    
def sale_you_are(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(SellProperty,id=pk)
        you_are =YouAre.objects.all()
        if request.method == 'POST':
            you_are_id = request.POST['you_are']
            a=person.you_are =YouAre.objects.get(id=you_are_id)
            person.save()
            messages.success(request,' almost added complete in your property  ')
            if a.you_are == "Agent":
                return redirect('sale_you_are_form',pk=person.id)
            else:
                messages.success(request,'added successfully')
                return redirect('/')
        return render(request,'rent/residenteial_purpose/you_are.html',{'youare':you_are})
    else:
        url = reverse('signin') 
        return redirect(url)
    

def sale_residenteial_purpose(request,pk):
    if request.user.is_authenticated:
        user =request.user
        person = get_object_or_404(SellProperty,id=pk)
        if person.reny_type_category.reny_type_category == "Flatmate(Room mate)":
            if request.method == 'POST':
                person.property_name = request.POST['propertyName']
                person.rent_image=request.FILES['image']

                # person.image1 = request.POST.get('image1')

                person.rent_price=request.POST['price']
                person.number_of_persons = request.POST['number_of_persons']
                person.num_of_bathrooms = request.POST['number_of_bathrooms']
                person.rent_size_in_squrefeet =request.POST['propertySqft']
                person.number_of_beds = request.POST['number_of_beds']
                person.rent_description=request.POST['description']
                person.extras = ", ".join(request.POST.getlist('amenities'))
                person.save()

                for image_file in request.FILES.getlist('images'):  
                   SaleMultipleImages.objects.create(user =user,sell_property =person, images=image_file)

                messages.success(request,' please complete your property details ')
                return redirect('sale_you_are',pk=person.id)
            return render(request,'rent/residenteial_purpose/rent_type/flatmate.html')
        elif request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.num_of_rooms = request.POST['numRooms']
            person.num_of_bathrooms = request.POST['numBathrooms']
            person.balcony = request.POST['balcony']
            person.rent_image=request.FILES['image']

            # person.image1 = request.POST.get('image1')

            person.furnished = request.POST['furnished']
            person.rent_size_in_squrefeet =request.POST['propertySqft']
            person.rent_price=request.POST['price']
            person.rent_description=request.POST['description']
            person.extras = ", ".join(request.POST.getlist('amenities'))
            person.save()

            for image_file in request.FILES.getlist('images'):  
                SaleMultipleImages.objects.create(user =user,sell_property =person, images=image_file)

            messages.success(request,' please complete your property details ')
            return redirect('sale_you_are',pk=person.id)
        return render(request,'rent/residenteial_purpose/residenteial_purpose.html')
    else:
        url = reverse('signin') 
        return redirect(url)
    

def sale_commertial_purpose(request,pk):
    if request.user.is_authenticated:
        user =request.user
        person = get_object_or_404(SellProperty,id=pk)
        if request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.admin_area = request.POST['admin_area']
            person.confrence_room = request.POST['confrence_room']
            person.num_of_bathrooms = request.POST['numBathrooms']
            person.balcony = request.POST['balcony']
            person.rent_image=request.FILES['image']

            # person.image1 = request.POST.get('image1')

            person.furnished = request.POST['furnished']
            person.rent_size_in_squrefeet =request.POST['propertySqft']
            person.rent_price=request.POST['price']
            person.rent_description=request.POST['description']
            person.extras = ", ".join(request.POST.getlist('amenities'))
            person.save()


            for image_file in request.FILES.getlist('images'):  
                SaleMultipleImages.objects.create(user=user, sell_property =person, images=image_file)

            messages.success(request,' please complete your property details ')
            return redirect('sale_you_are',pk=person.id)
        return render(request,'rent/commertial_purpose/commertial_purpose.html')
    else:
        url = reverse('signin') 
        return redirect(url)
    
def sale_land_view(request,pk):
    if request.user.is_authenticated:
        user =request.user
        person = get_object_or_404(SellProperty,id=pk)
        if request.method == 'POST':
            person.property_name = request.POST.get('propertyName')
            person.type_of_soil = request.POST['type_of_soil']
            person.rent_description = request.POST['description']
            person.property_acre = request.POST['property_acre']
            person.rent_price=request.POST['price']
            person.rent_image=request.FILES['image']

            # person.image1 = request.POST.get('image1')

            person.save()

            for image_file in request.FILES.getlist('images'):  
                SaleMultipleImages.objects.create(user =user,sell_property =person, images=image_file)

            messages.success(request,' please complete your property details ')
 
            return redirect('sale_you_are',pk=person.id)
        return render(request,'rent/land/land_view.html')
    else:
        url = reverse('signin') 
        return redirect(url)


    

def sale_you_are_form(request,pk):
    if request.user.is_authenticated:
        person = get_object_or_404(SellProperty,id=pk)
        if request.method == 'POST':
            person.agent_name = request.POST['agent_name']
            person.agent_company = request.POST['agent_company']
            person.save()
            messages.success(request,'added successfully ')
            return redirect('/')
        return render(request,'rent/residenteial_purpose/you_are_form.html')
    else:
        url = reverse('signin') 
        return redirect(url)



def post_free_add_property_for_sale(request):
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
            prod=SellProperty(user =user,reny_type_category=type,rent_title=rent_title,rent_property_category=rent_category,district=district,city=city)
            prod.save()
            messages.success(request,' please complete your property details ')
            if rent_category.rent_property_category == 'Residenteial Purpose':
                return redirect('sale_residenteial_purpose',pk=prod.id)
            
            elif rent_category.rent_property_category== 'Commertial Purpose':
                return redirect('sale_commertial_purpose',pk=prod.id)
            
            elif rent_category.rent_property_category=='Land':
                return redirect('sale_land_view',pk=prod.id)
            else:
                return redirect('sale_residenteial_purpose',pk=prod.id)

        else:
            context ={
            'rent_category':rent_category,
            'districts': districts,
            }
        return render(request,'post_free_add_property_for_sale.html',context)
    else:
        url = reverse('signin') 
        return redirect(url)


def delete_your_sale_property(request,id):
    if request.user.is_authenticated:
        datas =SellProperty.objects.get(pk=id)
        datas.delete()
        messages.success(request,'Property deleted successfully ')
        return redirect('property_for_sale')
    else:
        url = reverse('signin') 
        return redirect(url)