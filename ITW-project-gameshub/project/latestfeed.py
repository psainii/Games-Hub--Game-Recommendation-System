from django.contrib.syndication.views import Feed
from django.urls import reverse
from games.models import popular,description
class PopularFeed(Feed):
    title = "Top 5 games"
    link = "/games"
    description = "These games are the choice of the generation"
    def items(self):
        return popular.objects.order_by('-votes')[:5]
    def item_title(self, item):
        return item.name
    def item_description(self, item):
        f=description.objects.get(name=item.name)
        return f.description
    
        