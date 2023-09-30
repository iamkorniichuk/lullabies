from django.db import models
from django.urls import reverse


class RegionChoices(models.TextChoices):
    CRIMEA = "AK", "Autonomous Republic of Crimea"
    VINNYTSIA = "AB", "Vinnytsia Oblast"
    VOLYN = "AC", "Volyn Oblast"
    DNIPROPETROVSK = "AR", "Dnipropetrovsk Oblast"
    DONETSK = "AH", "Donetsk Oblast"
    ZHYTOMYR = "AM", "Zhytomyr Oblast"
    ZAKARPATTIA = "AO", "Zakarpattia Oblast"
    ZAPORIZHZHIA = "AP", "Zaporizhzhia Oblast"
    IVANO_FRANKIVSK = "AT", "Ivano-Frankivsk Oblast"
    KYIV = "AA", "Kyiv Oblast"
    KIROVOHRAD = "BA", "Kirovohrad Oblast"
    LUHANSK = "BB", "Luhansk Oblast"
    LVIV = "BC", "Lviv Oblast"
    MYKOLAIV = "BE", "Mykolaiv Oblast"
    ODESA = "BH", "Odesa Oblast"
    POLTAVA = "BI", "Poltava Oblast"
    RIVNE = "BK", "Rivne Oblast"
    SUMY = "BM", "Sumy Oblast"
    TERNOPIL = "BO", "Ternopil Oblast"
    KHARKIV = "AX", "Kharkiv Oblast"
    KHERSON = "BT", "Kherson Oblast"
    KHMELNYTSKYI = "BX", "Khmelnytskyi Oblast"
    CHERKASY = "CA", "Cherkasy Oblast"
    CHERNIVTSI = "CE", "Chernivtsi Oblast"
    CHERNIHIV = "CB", "Chernihiv Oblast"


class Lullaby(models.Model):
    class Meta:
        verbose_name_plural = "lullabies"

    name = models.CharField(max_length=64)
    region = models.CharField(max_length=64, choices=RegionChoices.choices)
    lyrics = models.TextField()
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("lullaby-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Lullaby({self.name})"
