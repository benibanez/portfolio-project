from django.db import models

# Create A Blog models
#title
# pub_date
#body
#image


#Add the Blog app to the settings

#create a migration

# migrate

#add to the admin

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
