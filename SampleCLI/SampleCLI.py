#!/usr/bin/env python-real

import sys

import InnerLibrary
import OuterLibrary

if __name__ == "__main__":
  args = InnerLibrary.parse_args()

  OuterLibrary.gaussian(args.input, args.sigma, args.output)
