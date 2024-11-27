#!/bin/bash

jupyter-book clean --html .
python convert_roles.py roles.yaml roles.md --header roles_header
jupyter-book build .
