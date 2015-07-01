from django.contrib import admin

from .models import SshHackIP, SshHackUsername, SshHackAttempt


admin.site.register(SshHackIP)
admin.site.register(SshHackUsername)
admin.site.register(SshHackAttempt)
