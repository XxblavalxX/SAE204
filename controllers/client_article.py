#! /usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import Flask, request, render_template, redirect, url_for, abort, flash, session, g

from connexion_db import get_db

client_article = Blueprint('client_article', __name__,
                        template_folder='templates')

@client_article.route('/client/index')
@client_article.route('/client/article/show')      # remplace /client
def client_article_show():                                 # remplace client_index
    mycursor = get_db().cursor()
    sql = ''' SELECT * FROM voiture '''
    mycursor.execute(sql)
    articles = mycursor.fetchall()
    sql = ''' SELECT * FROM type_voiture '''
    mycursor.execute(sql)
    types_articles = mycursor.fetchall()
    # print(types_articles)
    sql = ''' SELECT * FROM panier 
    INNER JOIN voiture ON panier.id_voiture=voiture.id_voiture'''

    mycursor.execute(sql)
    articles_panier  = mycursor.fetchall()
    print(articles_panier)
    # print(articles_panier, "caca")
    sql = '''SELECT SUM(quantite*prix_unitair) as prix_total FROM panier'''
    mycursor.execute(sql)
    prix_total=mycursor.fetchone()['prix_total']
    print(prix_total)
    # print(types_articles)
    # print(articles_panier)
    return render_template('client/boutique/panier_article.html', articles=articles, articlesPanier=articles_panier, prix_total=prix_total, itemsFiltre=types_articles)

@client_article.route('/client/article/details/<int:id>', methods=['GET'])
def client_article_details(id):
    mycursor = get_db().cursor()
    article= ''' SELECT * FROM voiture WHERE id_voiture=%s'''
    commentaires= ''' SELECT * FROM commentaire WHERE id_voiture=%s'''
    commandes_articles='''SELECT * FROM ligne_commande WHERE id_voiture=%s'''
    return render_template('client/boutique/article_details.html', article=article, commentaires=commentaires, commandes_articles=commandes_articles)