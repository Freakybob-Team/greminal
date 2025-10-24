import urllib.request
import json
import difflib

def python(app):
    with urllib.request.urlopen("https://food.freakybob.site/autumn/food.json") as url:
        data = json.load(url)
        print("Packages fetched! [autumn, food.json]")
    if (app in data["pypackages"]):
        print("Package found!")
        urllib.request.urlretrieve(
            "https://food.freakybob.site/packages/python/" + app + ".py", app + ".py"
        )
        print("Package downloaded!")
        print("The package will now run.")
        print("-----")
        with open(app + ".py") as file:
            exec(file.read())
    else:
        suggestions = difflib.get_close_matches(app, data['pypackages'], n=3, cutoff=0.6)
        if suggestions:
            print(f"Package not found. Did you mean: {', '.join(suggestions)}?")
        else:
            print("Package not found. No similar packages detected.")