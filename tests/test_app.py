import os

import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_landing_page(app, client):
    res = client.get('/')
    assert res.status_code == 200

def test_about_page(app, client):
    res = client.get('/about')
    assert res.status_code == 200

