

for nb_users in [1.e+00 1.e+01 1.e+02 1.e+03 1.e+04]:
    //locust -f async.py --host "https://qualityestimation-staging-ng.unbabel.net" --run-time 300 --autostart -u 1 -r 1 --headless --csv test