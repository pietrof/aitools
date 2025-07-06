to start:
pip install fastapi uvicorn
uvicorn main:app --reload

to test:
curl -G "http://127.0.0.1:8000/GetStartMethod" \
     --data-urlencode "businessCase=explain to me Day 3 Part 2"

or on gitpod something like this:
curl -X GET https://8000-pietrof-aitools-jnwg5l3sngk.ws-eu120.gitpod.io/GetStartMethod?businessCase=Day3%20Part2

