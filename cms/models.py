from django.db import models

class PageManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)

class Page(models.Model):
	title = models.CharField(max_length=200)
	is_public = models.BooleanField(default=False)
	objects = PageManager()

	def __str__(self):
		return self.title

class Component(models.Model):
	page = models.ForeignKey(Page, models.CASCADE, related_name='pages')
	GRID_CHOICES = (
	    ("ROW", "Row"),
	    ("COLUMN", "Column"),
	    ("TABPANEL", "TabPanel"),
	    ("ACCORDION", "Accordion"),
		("RICHTEXT", "RichText"),
	)

	grid = models.CharField(max_length=20,
                  choices=GRID_CHOICES,
                  default="ROW")
	content = models.CharField(max_length=250)
	rank = models.IntegerField()

	def __str__(self):
		return '%s %s' % (self.page, self.grid)
