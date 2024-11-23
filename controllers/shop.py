from flask import render_template, session, request, flash, redirect, url_for
from models.products import getProductById, getProductsByCategory, getRecommendedProducts, getRecentlyPurchased

def index():
    recently_purchased = getRecentlyPurchased(session["user"]["ID"]) if session.get("user") else []
    
    return render_template('index.html', recommended_products = getRecommendedProducts(), recently_purchased = recently_purchased)

def productGallery(category):
    return render_template('productGallery.html', products=getProductsByCategory(category), category=category)



def addProductToCart(product, quantity):
    cart = session.get('cart', {})
    if cart.get(product):
        cart[product]["quantity"] += quantity
    else:
        cart[product] = {'quantity': quantity, **getProductById(product)}
    session['cart'] = cart

def cart():
    if not session.get("user"):
        flash('Debes iniciar sesión para agregar productos al carrito', category='error')
        return redirect(url_for('login'))
    
    productID = request.args.get('p')
    if productID:
        addProductToCart(productID, 1)
        return redirect(url_for('cart'))


    cart_products = list(session.get('cart', {}).values())
    total = sum([product['price'] * product['quantity'] for product in cart_products])
    return render_template('cart.html', products=cart_products, total=total)