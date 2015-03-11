from threading import local


class TrackRequest(object):
    def process_request(self, request):
        d = local()
        d.django_current_request = request
