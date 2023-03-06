import argparse
import pathlib


def _parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', type=pathlib.Path)
  parser.add_argument('sigma', type=float)
  parser.add_argument('output', type=pathlib.Path)
  return parser


def parse_args():
  return _parser().parse_args()
