from flask import render_template, session
from models.products import getProductById, getProductsByCategory, getRecommendedProducts, getRecentlyPurchased

def index():
    recently_purchased = getRecentlyPurchased(session["user"]["ID"]) if session.get("user") else []
    
    return render_template('index.html', recommended_products = getRecommendedProducts(), recently_purchased = recently_purchased)

def patinetas():
    return render_template('patinetas.html', products=getProductsByCategory("Completa"))

def productGallery(category):
    return render_template('productGallery.html', products=getProductsByCategory(category), category=category)