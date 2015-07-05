from rest_framework import viewsets

from ..models import SshHackIP, SshHackLocation
from .serializers import HackIpSerializer, HackLocationSerializer


class HackIPViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hack attempt IPs to be viewed
    """
    queryset = SshHackIP.objects.all()
    serializer_class = HackIpSerializer
    paginate_by = 500


class HackLocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint to view hack attempt locations
    """
    queryset = SshHackLocation.objects.all()
    serializer_class = HackLocationSerializer
    paginate_by = 500
