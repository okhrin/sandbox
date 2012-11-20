from django.views.generic import TemplateView, DetailView
from app.models import UserProfile

class HomeView(TemplateView):
    template_name = 'home.html'

    class Meta:
        app_name = 'app'

class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return self.request.user