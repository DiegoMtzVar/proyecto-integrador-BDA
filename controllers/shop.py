from flask import render_template, session
from models.products import getProductById, getProductsByType, getRecommendedProducts, getRecentlyPurchased

def index():
    recently_purchased = getRecentlyPurchased(session["user"].id) if session.get("user") else []
    
    return render_template('index.html', recommended_products = getRecommendedProducts(), recently_purchased = recently_purchased)



def patinetas():
    return render_template('patinetas.html', productos=getProductsByType("Completa"))
