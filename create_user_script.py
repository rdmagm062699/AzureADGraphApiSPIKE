import click
import yaml

from user_operations import create_user


@click.command()
@click.argument('first_name')
@click.argument('last_name')
@click.argument('email')
def create(first_name, last_name, email):
    with open("config/config.yml", 'r') as ymlfile:
        config = yaml.load(ymlfile)

    result = create_user(first_name, last_name, email, config)
    print(result)


if __name__ == "__main__":
    create()
