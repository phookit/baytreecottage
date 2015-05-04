from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Create initial pages for bay tree cottage'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        call_command("loaddata", "baytreecottage_required.json")

    #def handle(self, *args, **options):
    #    for poll_id in options['poll_id']:
    #        try:
    #            poll = Poll.objects.get(pk=poll_id)
    #        except Poll.DoesNotExist:
    #            raise CommandError('Poll "%s" does not exist' % poll_id)
    #
    #        poll.opened = False
    #        poll.save()
    #
    #        self.stdout.write('Successfully closed poll "%s"' % poll_id)
