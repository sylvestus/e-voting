
"""
Authentication URLs

Ben Adida (ben@adida.net)
"""

from django.urls import include, re_path


from settings import AUTH_ENABLED_SYSTEMS
from . import views, url_names

urlpatterns = [
    # basic static stuff
    re_path(r'^$', views.index, name=url_names.AUTH_INDEX),
    re_path(r'^logout$', views.logout, name=url_names.AUTH_LOGOUT),
    re_path(r'^start/(?P<system_name>.*)$', views.start, name=url_names.AUTH_START),
    # weird facebook constraint for trailing slash
    re_path(r'^after/$', views.after, name=url_names.AUTH_AFTER),
    re_path(r'^why$', views.perms_why, name=url_names.AUTH_WHY),
    re_path(r'^after_intervention$', views.after_intervention, name=url_names.AUTH_AFTER_INTERVENTION),
]

# password auth
if 'password' in AUTH_ENABLED_SYSTEMS:
    from .auth_systems.password import urlpatterns as password_patterns
    urlpatterns.extend(password_patterns)

# twitter
if 'twitter' in AUTH_ENABLED_SYSTEMS:
    from .auth_systems.twitter import urlpatterns as twitter_patterns
    urlpatterns.extend(twitter_patterns)
