from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import json, os


def get_basedir():
    BASE_DIR = Path(__file__).resolve().parent.parent
    return BASE_DIR


def get_secret(setting):
    # json 기반 비밀 모듈
    with open(os.path.join(get_basedir(), 'secrets.json')) as f:
        secrets = json.loads(f.read())

    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)