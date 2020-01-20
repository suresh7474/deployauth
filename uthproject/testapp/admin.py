from django.contrib import admin

# Register your models here.
import logging

logging.basicConfig(filename='rr.txt' ,level=logging.WARNING)
print(logging.debug('This is degug'))
print(logging.warning('This is warning'))
print(logging.critical('This is critical'))
print(logging.info('This is info'))
print(logging.error('This is error'))
