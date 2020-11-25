import markdown2
from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki_entry(request, title):
    """Gets the default page for a wiki entry, returns 404 if not found"""

    entry = util.get_entry(title=title)

    if not entry:
        return render(request, "encyclopedia/not_found.html")

    # cast the text to markdown
    entry_text = markdown2.markdown(entry)

    return render(request, "encyclopedia/wiki_entry.html", {"body": entry_text})
