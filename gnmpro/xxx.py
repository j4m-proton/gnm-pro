#!/usr/bin/env python
# filename: load_heroku_data.py

import os
import django
from contextlib import contextmanager
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.core.management import call_command

# =========================
# 1. Set Django settings
# =========================
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomprj.settings")
django.setup()

# =========================
# 2. Context manager to disable all model signals
# =========================
@contextmanager
def disable_signals():
    signals = [pre_save, post_save, pre_delete, post_delete]
    backup = {signal: signal.receivers[:] for signal in signals}
    try:
        for signal in signals:
            signal.receivers = []
        yield
    finally:
        for signal in signals:
            signal.receivers = backup[signal]

# =========================
# 3. Load fixture safely
# =========================
fixture_file = "data.json"  # make sure this file is in your project root

with disable_signals():
    print(f"Loading fixture '{fixture_file}' into database...")
    call_command('loaddata', fixture_file)
    print(f"Finished loading '{fixture_file}' successfully!")


# fix_stock.py
import os
import django

# Badilisha hii kwa path ya settings yako
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecomprj.settings")
django.setup()

from core.models import Product

def fix_stock_counts():
    total_fixed = 0
    for p in Product.objects.all():
        try:
            # jaribu convert stock_count kuwa int
            p.stock_count = int(p.stock_count)
        except (ValueError, TypeError):
            # kama haiwezi convert, weka 0
            p.stock_count = 0
        p.save()
        total_fixed += 1
    print(f"Successfully fixed stock_count for {total_fixed} products!")

if __name__ == "__main__":
    fix_stock_counts()

