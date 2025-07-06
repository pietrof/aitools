to start:
pip install fastapi uvicorn
uvicorn main:app --reload

to test:
curl -G "http://127.0.0.1:8000/GetStartMethod" \
     --data-urlencode "businessCase=explain to me Day 3 Part 2"
