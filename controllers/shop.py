from flask import render_template, session, request, flash, redirect, url_for
from models.products import *

def index():
    return render_template('shop/index.html', recommended_products = getRecommendedProducts())

def productGallery(category):
    return render_template('shop/productGallery.html', products=getProductsByCategory(category), category=category)

def comprasRecientes():
    if not session.get("user"):
        flash('Debes iniciar sesión para ver tus compras', category='error')
        return redirect(url_for('login'))
    return render_template('shop/comprasRecientes.html', 
                           compras=getUserPurchases(session['user']['ID']),
                           host_url=request.host_url)

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
    promocion=session.get('promocion', {})
    return render_template('shop/cart.html', products=cart_products, total=total,promocion=promocion)

def single_product(id):
    product = getProductById(id)
    resenas = getResenas(id)
    if product:
        return render_template('shop/single-product.html', product=product, resenas=resenas)
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
    cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
    if not cart_products:
        flash('No tienes productos en el carrito', category='error')
        return redirect(url_for('cart'))
    total = sum([product['price'] * product['quantity'] for product in cart_products])
    promocion=session.get('promocion', {})    
    return render_template('shop/checkout.html', products=cart_products, total=total,promocion=promocion)

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
        promocion=session.get('promocion', {})
        discount = promocion.get('discount', 0)
        cart_products = [{'ID': product_id, **details} for product_id, details in session.get('cart', {}).items()]
        total = sum([product['price'] * product['quantity'] for product in cart_products])
        if discount>0:
            total=total-(total*discount/100) 
        aniadirCompra(session['user']['ID'],direccion,entrega,total)
        id=ultimaCompra(session['user']['ID'])
        #para calcular total de la compra
        if id:
            for product in cart_products:
                aniadirContiene(product['ID'],id,product['quantity'],discount)
            session['cart'] = {}
            session['promocion'] = {}
            flash('Compra realizada', category='info')
        else:
            flash('Error al realizar la compra', category='error')
    return redirect(url_for('cart'))

def cupon():
    if not session.get("user"):
        flash('Debes iniciar sesión para agregar productos al carrito', category='error')
        return redirect(url_for('login'))
    nCupon=request.form['cupon']
    cupon=getCuponesbyID(nCupon)
    if cupon:
        session['promocion']=cupon
        flash('Cupon añadido', category='info')
    return redirect(url_for('cart'))
