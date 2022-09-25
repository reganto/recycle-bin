#! /bin/env bash

gunicorn config.wsgi:application

