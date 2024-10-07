from django.shortcuts import render, get_object_or_404, redirect
from home.models import Product,Address
from django.http import HttpResponseBadRequest
# Home view function
def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home/index.html', context)

# Product detail view
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {'product': product}
    return render(request, 'home/product.html', context)

from django.shortcuts import redirect, render, get_object_or_404

def addrase(request):
    if request.method == "POST":
        action = request.POST.get('action')

        # When the user selects the product and clicks "Buy Now"
        if action == 'select_product':
            product_slug = request.POST.get('product_slug')
            if product_slug:
                # Store the product slug in the session for later use
                request.session['order_data'] = {
                    'product_slug': product_slug
                }
                # Redirect to the address form after selecting the product
                return redirect('addrase')
            else:
                return HttpResponseBadRequest("No product selected.")

        # When the user submits the address form
        elif action == 'save_address':
            full_name = request.POST.get('fullName')
            mobile_number = request.POST.get('mobileNumber')
            pincode = request.POST.get('pincode')
            city = request.POST.get('city')
            state = request.POST.get('state')
            house_no = request.POST.get('houseNo')
            road_name = request.POST.get('roadName')

            # Ensure that a product is already selected
            order_data = request.session.get('order_data', {})
            if not order_data:
                return HttpResponseBadRequest("No product selected.")

            # Retrieve the selected product
            product_slug = order_data.get('product_slug')
            product = get_object_or_404(Product, slug=product_slug)

            # Create and save the address in the database
            address = Address(
                full_name=full_name,
                mobile_number=mobile_number,
                pincode=pincode,
                city=city,
                state=state,
                house_no=house_no,
                road_name=road_name,
                product=product  # Link the address to the selected product
            )
            address.save()

            # Update order data in the session to include address details
            order_data.update({
                'full_name': full_name,
                'mobile_number': mobile_number,
                'pincode': pincode,
                'city': city,
                'state': state,
                'house_no': house_no,
                'road_name': road_name,
            })
            request.session['order_data'] = order_data  # Save updated order data in the session

            # Redirect to the order summary page
            return redirect('order')  # Ensure this URL is defined in your urls.py

        else:
            return HttpResponseBadRequest("Invalid action.")

    # If it's a GET request, render the address form
    order_data = request.session.get('order_data', {})
    product_slug = order_data.get('product_slug')

    if product_slug:
        # Retrieve the selected product from the database using the slug
        product = get_object_or_404(Product, slug=product_slug)
    else:
        # If no product is selected, redirect back to the home page
        return redirect('home')

    return render(request, 'home/addrase.html', {'product': product})
def order(request):
    # Retrieve the order and address data from the session
    order_data = request.session.get('order_data', {})

    # If no order data is present, redirect back to the address form
    if not order_data:
        return redirect('addrase')

    # Retrieve the selected product from the session data
    product_slug = order_data.get('product_slug')
    if not product_slug:
        return redirect('addrase')

    selected_product = get_object_or_404(Product, slug=product_slug)

    # Render the order summary page, showing the product and address details
    return render(request, 'home/order2.html', {
        'order_data': order_data,  # This contains address details
        'selected_product': selected_product,
    })



def payment(request):
    # Retrieve order data from the session
    order_data = request.session.get('order_data', {})

    # If no order data, redirect back to the address page
    if not order_data:
        return redirect('addrase')

    # Get the selected product slug
    product_slug = order_data.get('product_slug')
    if not product_slug:
        return redirect('addrase')

    # Get the selected product details
    selected_product = get_object_or_404(Product, slug=product_slug)

    # Render the payment page, passing all the product and order details
    return render(request, 'home/payment.html', {
        'selected_product': selected_product,
        'order_data': order_data,  # This will include the address and other details
    })
