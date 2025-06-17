from prometheus_client import Counter, Histogram
import time

requests_total = Counter('http_requests_total', 'Total HTTP requests')
request_duration_seconds = Histogram('http_request_duration_seconds', 'HTTP request duration')

@app.before_request
def before_request():
request.start_time = time.time()
requests_total.inc()

@app.after_request
def after_request(response):
request_duration = time.time() - request.start_time
request_duration_seconds.observe(request_duration)
return response