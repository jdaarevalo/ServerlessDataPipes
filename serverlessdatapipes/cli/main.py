import argparse
from .commands import init_project, delete_project

def main():
    parser = argparse.ArgumentParser(description='ServerlessDataPipes CLI')

    subparsers = parser.add_subparsers(dest='command')

    # Subparser to command 'init'
    parser_init = subparsers.add_parser('init', help='Initialize a new ServerlessDataPipes project')
    parser_init.add_argument('-n', '--name', default='ServerlessDataPipes_Project', 
                             help='Optional project name')
    parser_init.set_defaults(func=init_project)

    # Subparser to command 'delete'
    parser_delete = subparsers.add_parser('delete', help='Delete an existing ServerlessDataPipes project')
    parser_delete.add_argument('-n', '--name', default='ServerlessDataPipes_Project', 
                               help='Optional project name')
    parser_delete.set_defaults(func=delete_project)

    # Parse the arguments
    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
