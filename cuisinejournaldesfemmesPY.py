from bs4 import BeautifulSoup

import urllib.parse
import urllib.request
import ast
import re

class CuisineJournalDesFemmes(object):
    @staticmethod
    def get(url):
        html_content = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html_content, 'html.parser')
        
        image_url=soup.find("img", {"class": "bu_cuisine_img_noborder photo"})["src"]

        list_ingredients=[]
        ingredients_data = soup.findAll("h3", {"class": "app_recipe_ing_title"})

        for i in range(len(ingredients_data)):
            list_ingredients.append(ingredients_data[i].find("span")["data-quantity"]+ingredients_data[i].find("span")["data-mesure-singular"]+" "+ingredients_data[i].find('a')["alt"])

        list_step=[]
        step_data=soup.findAll("li", {"class": "bu_cuisine_recette_prepa"})
        for i in step_data:
            list_step.append(i.text.replace("  ", "").replace("\n", ""))        
        
        rate=soup.find("span", {"class": "jAverage"}).text.replace("                                    ", "").replace("    ", "")+"/5"

        name=soup.find("h1", {"class": "app_recipe_title_page"}).text

        data = {
            "url": url,
            "image": image_url,
            "name": name,
            "ingredients": list_ingredients,
            "step": list_step,
            "rate": rate
        }

        return data