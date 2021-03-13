import markdown2
from django.shortcuts import render, redirect

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


def search(request):
    """Searches for an entry in current ones, if name fully matches,
    directly redirect, if not, redirects to a results page"""
    query = str(request.GET['q'])

    entry = util.get_entry(title=query)

    # if exact matches, redirect to directly
    if entry:
        return redirect('wiki_entry', title=query)

    # look for full list
    all_entries = util.list_entries()
    # filter titles starting with
    filtered_entries = [entry for entry in all_entries if entry.lower().startswith(query.lower())]

    return render(request, "encyclopedia/results.html", {"result": filtered_entries})
