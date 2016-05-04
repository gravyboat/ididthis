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
@click.option('-m', default = 'commit message',
              help = 'This is your commit message')
@click.option('-log', default = 'idt.log',
              help = 'This is your log file location')
#@click.option('--out', type=click.File('w'), default='idt.log',
#                required=False)


def c(m, log):
    """
    Add a timestamped commit to your log file
    """

    handler = logging.FileHandler(log)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    click.echo('Message logged: {0}'.format(m))
    logger.error(m)
