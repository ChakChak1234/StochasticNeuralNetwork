from argparse import ArgumentParser
import logging
from run_tests import run_test


def main():
    """

    :return:
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--testing",
        type=bool,
        default=True
    )
    parser.add_argument(
        "--test_type",
        type=str,
        default="BaseNetworkGeneration"
    )

    args = parser.parse_args()

    if args.testing:
        run_test(test_type=args.test_type)
    else:
        print(f"Args: {args.testing}")
        for d in dir(args):
            if d[0] != "_":
                print(d)


if __name__ == "__main__":
    main()
