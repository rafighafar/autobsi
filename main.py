from src import get_from_config, write_entry_point


def main():
    setup = {
        'get': get_from_config,
        'mail': False,
        'verbose': False,
        'cloud': True,
    }

    write_entry_point(**setup)


if __name__ == '__main__':
    main()
