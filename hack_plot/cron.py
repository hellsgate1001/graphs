from datetime import datetime
import gzip
import json
import re

from unipath import Path, FILES

from models import SshHackIP, SshHackUsername, SshHackAttempt


class AuthAttempt(object):
    def __init__(self, *args, **kwargs):
        self.ip_pattern = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
        self.username_pattern1 = r'Invalid user (?P<username>\w+) from'
        self.username_pattern2 = r'User (?P<username>\w+) from'
        self.required_keys = [
            'ip_address', 'username', 'attempted'
        ]

        self.ip_address = None
        self.username = None
        self.attempted = None

    def set_ip_from_line(self, line):
        match = re.search(self.ip_pattern, line)
        if match is not None:
            self.ip_address = match.groups()[0]

    def set_username_from_line(self, line):
        match = re.search(self.username_pattern1, line)
        if match is not None:
            self.username = match.groups()[0]
            return

        match = re.search(self.username_pattern2, line)
        if match is not None:
            self.username = match.groups()[0]

    @property
    def has_all_keys(self):
        for key in self.required_keys:
            if getattr(self, key) is None:
                return False
        return True

    def save(self):
        ip, created = SshHackIP.objects.get_or_create(
            ip_address=self.ip_address
        )
        if not ip.located:
            ip.set_location()

        username, u_created = SshHackUsername.objects.get_or_create(
            username=self.username
        )
        auth_attempt = SshHackAttempt(
            attempted=self.attempted, ip=ip, username=username, ssh_id=self.ssh_id
        )
        auth_attempt.save()


def get_date_from_line(line):
    date_string = line[:15].strip()
    dt = datetime.strptime(
        date_string, '%b %d %H:%M:%S'
    ).replace(year=datetime.now().year)
    remainder = line[15:].strip()
    return dt, remainder


def get_id_from_line(line):
    return line[
        (line.find('[')) + 1:
        line.find(']')
    ]


def parse_auth_log(log_folder='/var/log/'):
    directory = Path(log_folder)
    for auth_file in directory.listdir('auth*.*', FILES):
        if auth_file.ext == '.gz':
            auth = gzip.open(auth_file, 'rb')
        else:
            auth = open(auth_file, 'rU')

        prev_id = ''
        attempt = None
        for line in auth.readlines():
            line = line.strip()

            # Skip sudo entries
            if line.find('sudo') >= 0:
                continue
            # Grab the date/time of the attempt and remove that from line
            attempted, line = get_date_from_line(line)

            # Grab the attempt ID
            attempt_id = get_id_from_line(line)

            # Is this a dup?
            if SshHackAttempt.objects.filter(ssh_id=attempt_id).count() > 0:
                continue

            # Is this a new attempt?
            new_attempt = prev_id != attempt_id

            if new_attempt:
                if getattr(attempt, 'has_all_keys', None):
                    # Store the previous attempt and start a new one
                    attempt.save()
                attempt = AuthAttempt()
                attempt.ssh_id = attempt_id
                attempt.attempted = attempted

            # Grab the IP address
            attempt.set_ip_from_line(line)

            # Is the username in this line?
            attempt.set_username_from_line(line)

            # Does the ID need updated?
            if prev_id != attempt_id:
                prev_id = attempt_id

        auth.close()
