from django.db import models


COCKTAIL_TYPE = (
    ('custom', "Custom"),
    ('api', 'CocktailDB_API'))


class Cocktail(models.Model):
    drink_id = models.IntegerField()
    cocktail_name = models.CharField(max_length=800, null=False)
    cocktail_details = models.JSONField()
    cocktail_type = models.CharField(max_length=16, choices=COCKTAIL_TYPE,
                                     default='api')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.drink_id} - {self.drink_id}'

    class Meta:
        db_table = 'tbl_cocktails'
