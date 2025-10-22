# config.py
from pathlib import Path
import os

# Корень проекта (папка, где лежит config.py)
PROJECT_ROOT = Path(__file__).resolve().parent

# Папка с данными:
# 1) берётся из переменной окружения DATA_DIR, если она задана
# 2) иначе берём локальную папку внутри проекта
DATA_DIR = Path(os.getenv("DATA_DIR", PROJECT_ROOT)).resolve()

# Конкретные подкаталоги/файлы
TRAIN_IMAGES_DIR = DATA_DIR / "train_images"
TEST_IMAGES_DIR  = DATA_DIR / "test_images"

CROWD_ANN_PATH   = DATA_DIR / "CrowdAnnotations.tsv"
EXPERT_ANN_PATH  = DATA_DIR / "ExpertAnnotations.tsv"
TRAIN_CSV        = DATA_DIR / "train_dataset.csv"
TEST_IMAGES_CSV  = DATA_DIR / "test_images.csv"
TEST_QUERIES_CSV = DATA_DIR / "test_queries.csv"
README_PATH      = PROJECT_ROOT / "README.md"
