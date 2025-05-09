import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from apex_engine.main_engine import run_daily_predictions

if __name__ == '__main__':
    run_daily_predictions()