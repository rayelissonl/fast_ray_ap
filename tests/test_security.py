from jwt import decode

from fast_ray_ap.security import ALGORITHM, SECRET_KEY, create_access_token


def test_jwt():
    data = {'sub': 'test@test,com'}
    result = create_access_token(data)

    result = decode(result, SECRET_KEY, algorithms=[ALGORITHM])

    assert result['sub'] == data['sub']
    assert result['exp']
