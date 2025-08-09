# celery -A tasks worker --loglevel=info  # run the worker

# celery multi start w1 -A videoflix -l info  # start one or more workers in the background

python manage.py rqworker default