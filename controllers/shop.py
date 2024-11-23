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
    
    newProduct = request.args.get('p')
    if newProduct:
        addProductToCart(newProduct, 1)
        return redirect(url_for('cart'))
    
    removedProduct = request.args.get('r')
    if removedProduct:
        cart = session.get('cart', {})
        cart.pop(removedProduct, None)
        session['cart'] = cart
        return redirect(url_for('cart'))


    cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
    total = sum([product['price'] * product['quantity'] for product in cart_products])
    return render_template('cart.html', products=cart_products, total=total)

def single_product(id):
    product = getProductById(id)
    if product:
        return render_template('single-product.html', product=product)
    else:
        flash('Producto no encontrado', category='error')
        return redirect(url_for('productGallery'))