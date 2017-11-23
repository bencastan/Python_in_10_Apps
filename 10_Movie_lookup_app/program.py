import requests
import movie_svc


def main():
    print_header()
    search_event_loop()


def print_header():
    print("--------------------")
    print("  Movie Search APP")
    print("--------------------")
    print("")


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'
    while search != 'x':
        try:
            search = input("Movie search text (x to exit): ")
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results".format(len(results)))
                for r in results:
                    print("{} -- {}".format(
                        r.year, r.title
                    ))
                print()
        except ValueError:
            print("Search text is required")
        except requests.exceptions.ConnectionError:
            print("Error the network is down!...")
        except Exception as x:
            print("Unexpected error. Details: {}".format(x))

    print("Exiting...")


if __name__ == '__main__':
    main()
