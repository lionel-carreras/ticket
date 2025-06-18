

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class RoleBasedLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        # Ajusta los nombres de grupo exactamente como los creaste en el Admin
        if user.groups.filter(name='usuario').exists():
            return reverse_lazy('soporte:dashboard_usuario')
        if user.groups.filter(name='agente').exists():
            return reverse_lazy('soporte:dashboard_agente')
        # Fallback (por ejemplo, admin u otros)
        return super().get_success_url()
