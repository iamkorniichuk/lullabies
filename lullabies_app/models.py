from django.db import models
from django.urls import reverse


class RegionChoices(models.IntegerChoices):
    CRIMEA = 1, "Autonomous Republic of Crimea"
    VINNYTSIA = 2, "Vinnytsia Oblast"
    VOLYN = 3, "Volyn Oblast"
    DNIPROPETROVSK = 4, "Dnipropetrovsk Oblast"
    DONETSK = 5, "Donetsk Oblast"
    ZHYTOMYR = 6, "Zhytomyr Oblast"
    ZAKARPATTIA = 7, "Zakarpattia Oblast"
    ZAPORIZHZHIA = 8, "Zaporizhzhia Oblast"
    IVANO_FRANKIVSK = 9, "Ivano-Frankivsk Oblast"
    KYIV = 10, "Kyiv Oblast"
    KIROVOHRAD = 11, "Kirovohrad Oblast"
    LUHANSK = 12, "Luhansk Oblast"
    LVIV = 13, "Lviv Oblast"
    MYKOLAIV = 14, "Mykolaiv Oblast"
    ODESA = 15, "Odesa Oblast"
    POLTAVA = 16, "Poltava Oblast"
    RIVNE = 17, "Rivne Oblast"
    SUMY = 18, "Sumy Oblast"
    TERNOPIL = 19, "Ternopil Oblast"
    KHARKIV = 20, "Kharkiv Oblast"
    KHERSON = 21, "Kherson Oblast"
    KHMELNYTSKYI = 22, "Khmelnytskyi Oblast"
    CHERKASY = 23, "Cherkasy Oblast"
    CHERNIVTSI = 24, "Chernivtsi Oblast"
    CHERNIHIV = 25, "Chernihiv Oblast"


class Lullaby(models.Model):
    class Meta:
        verbose_name_plural = "lullabies"

    name = models.CharField(max_length=64)
    region = models.IntegerField(choices=RegionChoices.choices)
    lyrics = models.TextField()
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"
