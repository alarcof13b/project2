"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a href="/about" class="nav-link text-white" >About</a>' in response.data
    assert b'<a href="/git" class="nav-link text-white">Git</a>' in response.data
    assert b'<a href="/docker" class="nav-link text-white">Docker</a>' in response.data
    assert b'<a href="/python" class="nav-link text-white">Python</a>' in response.data
    assert b'<a href="/cid" class="nav-link text-white">CID</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/python")
    assert response.status_code == 200
    assert b"Python" in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/cid")
    assert response.status_code == 200
    assert b"CID" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
