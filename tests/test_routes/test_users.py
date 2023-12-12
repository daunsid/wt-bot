import json
from apgar_health import models
from apgar_health.core.config import settings


def test_login_access_token(client, db_session):
    data = {
        "username":settings,
        "password":settings
    }

    response = client.post("users/login/access-token", data=data)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert "token_type" in response.json()