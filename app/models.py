from django.db import models

# Create your models here.

class BannerVideo(models.Model):
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return f"Banner Video {self.id}"
    

    class Meta:
        verbose_name = "Banner Video"
        verbose_name_plural = "Banner Videos"
    

class Language_courses(models.Model):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"Language Course {self.id}"
    
    class Meta:
        verbose_name = "Language Course"
        verbose_name_plural = "Language Courses"
    

class Courses(models.Model):
    image = models.ImageField(upload_to='images/')
    country_choice = [
        ('India', 'India'),
        ('Abroad', 'Abroad'),
    ]
    country = models.CharField(max_length=20, choices=country_choice)
    Course_title = models.CharField(max_length=100)
    course1 = models.CharField(max_length=100,null=True, blank=True)
    course2 = models.CharField(max_length=100,null=True, blank=True)
    course3 = models.CharField(max_length=100,null=True, blank=True)
    course4 = models.CharField(max_length=100,null=True, blank=True)
    course5 = models.CharField(max_length=100,null=True, blank=True)
    course6 = models.CharField(max_length=100,null=True, blank=True)
    course7 = models.CharField(max_length=100,null=True, blank=True)
    course8 = models.CharField(max_length=100,null=True, blank=True)
    course9 = models.CharField(max_length=100,null=True, blank=True)
    course10 = models.CharField(max_length=100,null=True, blank=True)
    course11 = models.CharField(max_length=100,null=True, blank=True)
    course12 = models.CharField(max_length=100,null=True, blank=True)


    def __str__(self):
        return self.Course_title
    
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
    


class Testimonial(models.Model):
    image = models.ImageField(upload_to='images/',null=True, blank=True)
    rating = models.IntegerField()
    name = models.CharField(max_length=100)
    feedback = models.TextField()
    choice = [
        ('India', 'India'),
        ('Abroad', 'Abroad'),
    ]
    studied_at = models.CharField(max_length=20, choices=choice)

    def __str__(self):
        return f"Testimonial by {self.name} Studied at ({self.studied_at})"
    
    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"


class Graduate(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    country = models.CharField(max_length=100,null=True, blank=True)
    choice = [
        ('India', 'India'),
        ('Abroad', 'Abroad'),
    ]
    studied_at = models.CharField(max_length=20, choices=choice)

    def __str__(self):
        return f"Graduate {self.name} Studied at ({self.studied_at})"
    

    class Meta:
        verbose_name = "Graduate"
        verbose_name_plural = "Graduates"
    
    

class CEO(models.Model):
    image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return f"CEO Image: {self.id}"
    
    class Meta:
        verbose_name = "CEO"
        verbose_name_plural = "CEOs"
    
class COO(models.Model):
    image = models.ImageField(upload_to='images/')
 
    def __str__(self):
        return f"COO Image: {self.id}"
    
    class Meta:
        verbose_name = "COO"
        verbose_name_plural = "COOs"
    

class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='countries/')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"
    
    
class Destination(models.Model):
    
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='destinations/')
    country_choice = [
        ('India', 'India'),
        ('Abroad', 'Abroad'),
    ]
    country = models.CharField(max_length=20, choices=country_choice)

    highlight1 = models.CharField(max_length=200, blank=True, null=True)
    highlight2 = models.CharField(max_length=200, blank=True, null=True)
    highlight3 = models.CharField(max_length=200, blank=True, null=True)
    highlight4 = models.CharField(max_length=200, blank=True, null=True)
    highlight5 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.title} ({self.country})"
    
    class Meta:
        verbose_name = "Destination"
        verbose_name_plural = "Destinations"


class University(models.Model):
    country_choice = [
        ('India', 'India'),
        ('Abroad', 'Abroad'),
    ]
    country = models.CharField(max_length=20, choices=country_choice,null=True, blank=True)
    image = models.ImageField(upload_to='universities/')
 

    def __str__(self):
        return f"University Image: {self.id}"
    
    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
