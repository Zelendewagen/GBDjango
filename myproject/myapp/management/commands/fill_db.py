from random import choices

from django.core.management.base import BaseCommand
from myapp.models import Author, Post

LOREM = ("Lorem ipsum dasfsdagfsdafsdafsdfsdafsdfsadf"
         "asdfsadfasdfasdfsadfasdfsadf sdfdgsdf 12341235 dfg 453q2tyw "
         "asdfsadfasdfasdfsadfasdfsadf sdfdgsdf 12341235 dfg 453q2tyw "
         " asdf sdaf sdadfsg dsfgdsfg sdfg dsfg sdfgdsfg dfgdsdfgdsf gdsf"
         " 4234324 wegsdfg 45wyt dfg45wtg ervb453t 34t sfdgvaerfgxdCVxczv"
         " asdf sdaf sdadfsg dsfgdsfg sdfg dsfg sdfgdsfg dfgdsdfgdsf gdsf")


class Command(BaseCommand):
    help = "Generate fake authors and posts"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **options):
        text = LOREM.split()
        count = options.get('count')
        for i in range(1, count + 1):
            author = Author(name=f"Author_{i}", email=f"mail_{i}@mail.ru")
            author.save()
            for j in range(1, count + 1):
                post = Post(
                    title=f"Title-{j}",
                    content=" ".join(choices(text, k=64)),
                    author=author
                )
                post.save()

        self.stdout.write(f'{count} fake posts added')