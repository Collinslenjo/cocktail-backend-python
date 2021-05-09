## Backend Task
> Create a REST API
- endpoint that would fetch 5 random drinks from the cocktails API
  ```http://localhost:8000/api/cocktails/random```
- endpoint to fetch the details of one cocktail and its ingredients
  ```http://localhost:8000/api/cocktail?cocktail_id=13936```
- endpoint to create a custom drink stored in a local database
  ```http://localhost:8000/api/custom/cocktails/```
- endpoint to update the custom drink
  methods = [PUT, PATCH]
  ```http://localhost:8000/api/custom/cocktails/1/```
- endpoint to view the custom drink
  ```http://localhost:8000/api/custom/cocktails/1/```
- endpoint to fetch 5 latest custom drinks 
```http://localhost:8000/api/cocktails/latest```

> Custom Cocktail sample data
```json
{
    "drink_id": "13936",
    "cocktail_name": "Miami Vice",
    "cocktail_type": "custom",
    "cocktail_details": {
        "idDrink": "13936",
        "strDrink": "Miami Vice",
        "strTags": "IBA",
        "strCategory": "Cocktail",
        "strAlcoholic": "Alcoholic",
        "strGlass": "Cocktail glass",
        "strInstructions": "First: Mix pina colada with 2.5 oz. of rum with ice(set aside). Second: Mix daiquiri with 2.5 oz. of rum with ice. Third: While frozen, add pina colada mix then daiquiri mix in glass (Making sure they do not get mixed together).",
        "strDrinkThumb": "https://www.thecocktaildb.com/images/media/drink/qvuyqw1441208955.jpg",
        "strIngredient1": "151 proof rum",
        "strIngredient2": "Pina colada mix",
        "strIngredient3": "Daiquiri mix",
        "strMeasure1": "5 oz Bacardi ",
        "strMeasure2": "frozen ",
        "strMeasure3": "frozen ",
        "strCreativeCommonsConfirmed": "No",
        "dateModified": "2015-09-02 16:49:15"
    }
}
```

### How to set up
* clone the repository
* create a virtual environment and install the packages from the requirements file using the below command
  ```pip install -r requirements.txt```
* create a postgres database
* create a ```.env``` file from the env-sample file & fill in the db details, and the cocktail db api key
* run the following commands after.
- ```./manage.py makemigrations cocktail_app```
- ```./manage.py migrate```
- ```./manage.py runserver```
