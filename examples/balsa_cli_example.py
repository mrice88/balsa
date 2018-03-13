

from balsa import init_logger, get_logger

from examples import application_name, author, something_useful
from examples.error_callback import balsa_example_error_callback

log = get_logger(name=application_name)


def main():
    init_logger(application_name, author, use_app_dirs=True, error_callback=balsa_example_error_callback,
                delete_existing_log_files=True, verbose=True)

    something_useful()


if __name__ == '__main__':
    main()