import api
import webbrowser

def main():
    print('*+*+*+ SEARCH TALK PYTHON *+*+*+')
    search_term = input('Please enter a search term: ')

    search_results = api.search_training_site(search_term)

    print(f"There are {len(search_results)} results:")

    for idx, things in enumerate(search_results, 1):
        print(f"{idx}. {things.title}")

    idx_to_view = int(input('Which result would you like to view? '))-1
    full_url = api.get_url(idx_to_view, search_results)
    webbrowser.open(full_url, new=2)


if __name__ == "__main__":
    main()
