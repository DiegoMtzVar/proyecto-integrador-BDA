from flask import render_template, session, request, flash, redirect, url_for
from models.products import getProductById, getProductsByCategory, getRecommendedProducts, getRecentlyPurchased, aniadirResena, getResenas, getCompras, aniadirCompra,aniadirContiene, ultimaCompra

def index():
    if session.get("user"):
        recently_purchased = getRecentlyPurchased(session["user"]["ID"]) if session.get("user") and session["user"].get("ID") else []
    else:
        recently_purchased = []
    
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
    compras = getCompras(session['user']['ID'])
    cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
    total = sum([product['price'] * product['quantity'] for product in cart_products])
    return render_template('cart.html', products=cart_products, total=total, compras=compras)

def single_product(id):
    product = getProductById(id)
    resenas = getResenas(id)
    if product:
        return render_template('single-product.html', product=product, resenas=resenas)
    else:
        flash('Producto no encontrado', category='error')
        return redirect(url_for('productGallery'))
    
def resena(id):
    if not session.get("user"):
        flash('Debes iniciar sesión para hacer reseñas', category='error')
        return redirect(url_for('login'))
    rating=request.form['rating']
    comentario=request.form['resena']
    idU=session['user']['ID']   
    if aniadirResena(idU,id,rating,comentario):
        flash('Reseña añadida', category='info')
        return redirect(url_for('single_product', id=id))
    else:
        flash('No has comprado ese producto', category='error')
    return redirect(url_for('single_product', id=id))

def checkout():
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
    compras = getCompras(session['user']['ID'])
    cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
    total = sum([product['price'] * product['quantity'] for product in cart_products])
    return render_template('checkout.html', products=cart_products, total=total, compras=compras)

def finalizarCompra():
    if not session.get("user"):
        flash('Debes iniciar sesión para comprar cosas', category='error')
        return redirect(url_for('login'))
    if request.method == 'POST':
        entrega = request.form['entrega']
        pais = request.form['pais']
        estado = request.form['estado']
        municipio = request.form['municipio']
        calle = request.form['calle']
        postal = request.form['postal']
        direccion = pais+", "+estado+", "+municipio+", "+calle+", "+postal
        cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
        aniadirCompra(session['user']['ID'],direccion,entrega)
        id=ultimaCompra(session['user']['ID'])
        print(id)
        if id:
            for product in cart_products:
                aniadirContiene(product['ID'],id,product['quantity'])
            session['cart'] = {}
            flash('Compra realizada', category='info')
        else:
            flash('Error al realizar la compra', category='error')
    return redirect(url_for('cart'))
