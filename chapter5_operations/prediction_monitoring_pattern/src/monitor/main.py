import time
import click
import datetime
from logging import getLogger, DEBUG, Formatter, StreamHandler

from src.db import cruds, schemas
from src.db.database import get_context_db


logger = getLogger(__name__)
logger.setLevel(DEBUG)
formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

handler = StreamHandler()
handler.setLevel(DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)


@click.command(name="request job")
@click.option("--interval", type=int, default=1)
@click.option("--threshold_min_sepal_length", type=float, default=5.84 * 0.95)
@click.option("--threshold_max_sepal_length", type=float, default=5.84 * 1.05)
@click.option("--threshold_min_sepal_width", type=float, default=3.06 * 0.95)
@click.option("--threshold_max_sepal_width", type=float, default=3.06 * 1.05)
@click.option("--threshold_min_petal_length", type=float, default=3.76 * 0.95)
@click.option("--threshold_max_petal_length", type=float, default=3.76 * 1.05)
@click.option("--threshold_min_petal_width", type=float, default=1.20 * 0.95)
@click.option("--threshold_max_petal_width", type=float, default=1.20 * 1.05)
@click.option("--outlier_rate_threshold", type=float, default=0.8)
def main(
    interval: int,
    threshold_min_sepal_length: float,
    threshold_max_sepal_length: float,
    threshold_min_sepal_width: float,
    threshold_max_sepal_width: float,
    threshold_min_petal_length: float,
    threshold_max_petal_length: float,
    threshold_min_petal_width: float,
    threshold_max_petal_width: float,
    outlier_rate_threshold: float,
):
    logger.info("start monitoring...")
    while True:
        now = datetime.datetime.now()
        interval_ago = now - datetime.timedelta(minutes=interval)
        time_later = now.strftime("%Y-%m-%d %H:%M:%S")
        time_before = interval_ago.strftime("%Y-%m-%d %H:%M:%S")
        with get_context_db() as db:
            prediction_logs = cruds.select_prediction_log_betwenn(db=db, time_before=time_before, time_later=time_later)
            outlier_logs = cruds.select_outlier_log_betwenn(db=db, time_before=time_before, time_later=time_later)
        logger.info(f"prediction_logs between {time_before} and {time_later}: {len(prediction_logs)}")
        logger.info(f"outlier_logs between {time_before} and {time_later}: {len(outlier_logs)}")
        time.sleep(interval * 60)


if __name__ == "__main__":
    main()