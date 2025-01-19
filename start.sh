#!/bin/bash
./setup.sh
echo "Starting gunicorn"
gunicorn app:app
