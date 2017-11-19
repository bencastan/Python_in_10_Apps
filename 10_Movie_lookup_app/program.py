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
    search = 'ONCE_THROUG_LOOP'
    while search != 'x':
        search = input("Movie search text (x to exit): ")
        if search != 'x':
            results = movie_svc.find_movies(search)
            print("Found {} results".format(len(results)))
            for r in results:
                print("{} -- {}".format(
                    r.year, r.title
                ))
            print()

    print("Exiting...")


if __name__ == '__main__':
    main()
