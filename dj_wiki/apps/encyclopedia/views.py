import markdown2
from django.contrib import messages
from django.shortcuts import render, redirect

from . import util
from .forms import EntryForm


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

    return render(request, "encyclopedia/wiki_entry.html", {"title": title, "body": entry_text})


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


def create_entry(request):
    """Creates a new entry or shows the create form"""
    if request.method == 'POST':
        new_entry = EntryForm(request.POST)
        if new_entry.is_valid():
            # create the entry
            util.save_entry(new_entry.cleaned_data['title'], new_entry.cleaned_data['entry'])
            messages.success(request, 'The entry was saved successfully')
            return redirect('index')
        else:
            messages.error(request, "Entry couldn't be saved")
            return render(request, "encyclopedia/entry_form.html", {"form": new_entry})
    else:
        form = EntryForm()
        return render(request, "encyclopedia/entry_form.html", {"form": form})


def edit_entry(request, title):
    if request.method == 'POST':
        edited_entry = EntryForm(request.POST)
        if edited_entry.is_valid():
            # create the entry
            util.save_entry(edited_entry.cleaned_data['title'], edited_entry.cleaned_data['entry'])
            messages.success(request, 'The entry was updated successfully')
            return redirect('index')
        else:
            messages.error(request, "Entry couldn't be updated")
            return render(request, "encyclopedia/entry_form.html", {"form": edited_entry})
    else:
        entry = util.get_entry(title)
        if not entry:
            messages.error(request, "The requested entry does not exist")
            return redirect('index')

        form = EntryForm({'title': title, 'entry': entry})
        return render(request, "encyclopedia/entry_form.html", {"form": form})

