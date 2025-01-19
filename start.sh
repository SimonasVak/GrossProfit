#!/bin/bash
chmod +x drivers/geckodriver.exe
gunicorn app:app
