from uuid import uuid4

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

class GetUserMixin(object):
    def _create_anon_user(self):
        request = self.request

        anon_user = User.objects.create_user(uuid4().hex[:30])
        anon_password = User.objects.make_random_password()
        anon_user.set_password(anon_password)
        anon_user.is_active = False
        anon_user.save()

        request.session["temp_user"] = anon_user.username

        user = authenticate(username=anon_user.username,
            password=anon_password)

        if user is not None:
            login(request, user)

        return user

    def get_user(self):
        request = self.request

        if request.user.is_authenticated():
            return request.user

        elif request.session.get("temp_user"):
            try:
                return User.objects.get(username=request.session["temp_user"])
            except User.DoesNotExist:
                user = self._create_anon_user()
        else:
            user = self._create_anon_user()

        return User.objects.get(username=user.username)
