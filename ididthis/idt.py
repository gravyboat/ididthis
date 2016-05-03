#!/usr/bin/python

import click
import logging

logger = logging.getLogger(__name__)


class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--log-dir', type=click.Path())
@pass_config
def cli(config, log_dir):
    if log_dir is None:
        log_dir = '.'
    config.log_dir = log_dir

@cli.command()
@click.option('--m', default = 'world',
              help = 'This is your commit message')
@click.argument('out', type=click.File('w'), default='idt.log',
                required=False)


def c(m, out):
    """
    Add a timestamped commit to your log file.
    """

    handler = logging.FileHandler('idt.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

#    click.echo(m)
    logger.error(m)
