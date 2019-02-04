# -*- coding: utf-8 -*-
import sys

from commons.logging_ import add_loggers
from diff_1c import logger as main_logger
from diff_1c.cli import get_argparser


def run() -> None:
    argparser = get_argparser()
    args = argparser.parse_args(sys.argv[1:])
    add_loggers(args, main_logger)
    args.func(args)
