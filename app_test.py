from app import app

#first positive test case for '/hello' route
def test_hello_route_success():
    tester = app.test_client() #It will create a dummy website for testing
    response = tester.get('/hello')

    assert response.status_code==200 #assert is especially used in testing to check the condition and 200 means working fine

    # app_test.py . # '.' means the test has been passed

# def test_hello_route_failure():
#     tester = app.test_client() #It will create a dummy website for testing
#     response = tester.get('/hello')

#     assert response.status_code==500 #in terminal, 1 Failed and 1 passed

#     # app_test.py .F # 'F' means Failed test case


def test_hello_route_wrong_url():
    tester = app.test_client() #It will create a dummy website for testing
    response = tester.get('/jello')

    assert response.status_code==404 #Wrong url Error