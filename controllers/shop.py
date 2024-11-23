from flask import render_template, session, request, flash, redirect, url_for
from models.products import getProductById, getProductsByCategory, getRecommendedProducts, getRecentlyPurchased, addProductToCart, getCartProducts

def index():
    recently_purchased = getRecentlyPurchased(session["user"]["ID"]) if session.get("user") else []
    
    return render_template('index.html', recommended_products = getRecommendedProducts(), recently_purchased = recently_purchased)

def productGallery(category):
    return render_template('productGallery.html', products=getProductsByCategory(category), category=category)

def cart():
    if not session.get("user"):
        flash('Debes iniciar sesión para agregar productos al carrito', category='error')
        return redirect(url_for('login'))
    
    productID = request.args.get('p')
    if productID:
        success = addProductToCart(session["user"]["ID"], productID)
        if success:
            flash('Producto agregado al carrito', category='success')
        else:
            flash('Error al agregar el producto al carrito', category='error')

    return render_template('cart.html', products=getCartProducts(session["user"]["ID"]))