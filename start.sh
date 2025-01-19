#!/bin/bash
chmod +x drivers/geckodriver
gunicorn app:app
