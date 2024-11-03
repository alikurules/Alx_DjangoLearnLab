deletion = Book.objects.all()
deletion.delete()

from bookshelf.models import Book
retrieve = Book.objects.all()

# Python for confirming the deletion.
