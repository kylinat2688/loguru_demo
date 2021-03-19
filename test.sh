if ps -ef | grep 'client_request.py'|grep -v grep;then
    ps -ef | grep 'client_request.py'|grep -v grep|awk '{print $2}'|xargs kill
fi
if ps -ef | grep 'flask_api:app'|grep -v grep;then
    ps -ef | grep 'flask_api:app'|grep -v grep|awk '{print $2}'|xargs kill
fi
sleep 2s
nohup gunicorn -c gunicorn_conf.py flask_api:app > start.log 2>&1 &
sleep 1s
nohup python client_request.py >> start.log 2>&1 &