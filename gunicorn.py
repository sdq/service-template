import multiprocessing

bind = "0.0.0.0:5000"
workers = 2
timeout = 180
# workers = multiprocessing.cpu_count() * 2 + 1