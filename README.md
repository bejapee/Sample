# Sample project <put here the name of your project or software>

## Intro

This document is the first document a user would read about your software.
It is the **face** of your software; so make it crisp and clear; keep it short.

## Installation

  sh
    python -m venv venv
    source venv/bin/activate

## Get Dependencies

  pip install -r requirements.txt

## Run

  From the "inner" project folder, i.e. sample\sample

  FLASK_APP=core.py flask run

## Smoketest

  The run-action starts a webserver; so now from another Terminal, position in the
  tests directory and enter:

  source test_script.sh

  If the result printed on the screen is True, the program works correctly
