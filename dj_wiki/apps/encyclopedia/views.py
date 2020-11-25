from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki_entry(request, title):
    entry = util.get_entry(title=title)
    if not entry:
        return render(request, "encyclopedia/not_found.html")
    return render(request, "encyclopedia/wiki_entry.html", {"title": "Ejemplo", "body": "xdxdxd"})
