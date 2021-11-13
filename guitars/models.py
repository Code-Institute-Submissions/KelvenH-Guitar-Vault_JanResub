from django.db import models

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    """
    String method
    """
    def __str__(self):
        return self.name

    
    """
    Model method
    """
    def get_friendly_name(self):
        return self.get_friendly_name


class Guitar(models.Model):
    ELECTRIC = '1'
    BASS = '2'
    ACOUSTIC = '3'

    CATEGORY_CHOICES = [
        (ELECTRIC, 'Electric'),
        (BASS, 'Bass'),
        (ACOUSTIC, 'Acoustic'),
    ]
    category = models.ForeignKey('Category', choices=CATEGORY_CHOICES, default=ELECTRIC, on_delete=models.PROTECT) # PROTECT prevents deletion of the primary key (categories)
    brand = models.CharField(max_length=25)
    guitar_model = models.CharField(max_length=25)
    tier = models.CharField(max_length=25, null=True, blank=True)
    status = models.CharField(max_length=25, null=True, blank=True)
    owner = models.CharField(max_length=25, null=True, blank=True)
    handed = models.CharField(max_length=25, null=True, blank=True)
    no_strings = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    approx_age_years = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)

    """ Choices to create dropdown selection for users """
    EXCELLENT = 'Excellent'
    GOOD = 'Good'
    COSMETIC = 'Cosmetic'
    DEFECTIVE = 'Defective'
    CONDITION_CHOICES = [
        (EXCELLENT, 'Excellent'),
        (GOOD, 'Good'),
        (COSMETIC, 'Well Used (displays cosmetic signs of use only)'),
        (DEFECTIVE, 'Some form of damage / wear which affects performance. (No guitars can be added to the vault if defective. Existing guitars rated by users as defective will be marked as "unavailable" until inspected by Guitar Vault'),
        ]
    condition = models.CharField(max_length=25, choices=CONDITION_CHOICES, default=GOOD)
    construction = models.CharField(max_length=25, null=True, blank=True)
    body_wood = models.CharField(max_length=25, null=True, blank=True)
    body_top = models.CharField(max_length=25, null=True, blank=True)
    tuners = models.CharField(max_length=25, null=True, blank=True)
    
    FRETS_20 = '20'
    FRETS_22 = '22'
    FRETS_24 = '24'
    FRETS_CHOICES = [
        (FRETS_20, '20'),
        (FRETS_22, '22'),
        (FRETS_24, '24'),
        ]
    frets = models.DecimalField(max_digits=2, decimal_places=0, choices=FRETS_CHOICES, default=FRETS_22)
    scale_length = models.CharField(max_length=25, null=True, blank=True)
    neck_wood = models.CharField(max_length=25, null=True, blank=True)
    neck_profile = models.CharField(max_length=25, null=True, blank=True)
    no_pickups = models.DecimalField(max_digits=1, decimal_places=0, null=True, blank=True)
    pickups_desc = models.TextField()
    controls = models.CharField(max_length=25, null=True, blank=True)
    owners_additional_comments = models.TextField()
    rating_condition = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    rating_overall = models.DecimalField(max_digits=2, decimal_places=0, null=True, blank=True)
    image_id = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.guitar_model
