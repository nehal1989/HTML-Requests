import api


def main():
    print('* * * * * * * SEARCH TALK PYTHON * * * * * * *')
    search_term = input('Please enter a search term: ')

    search_results = api.search_training_site(search_term)

    print(f"There are {len(search_results)} results:")

    for idx, things in enumerate(search_results, 1):
        print(f"{idx}. {things.title}")


if __name__ == "__main__":
    main()
