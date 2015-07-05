from rest_framework import viewsets

from ..models import SshHackIP
from .serializers import HackIpSerializer


class HackIPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hack attempt IPs to be viewed
    """
    queryset = SshHackIP.objects.all()
    serializer_class = HackIpSerializer
    paginate_by = 500
