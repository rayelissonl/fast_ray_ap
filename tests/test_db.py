from sqlalchemy import select

from fast_ray_ap.models import User


def test_create_user(session):
    user = User(
        username='testertr',
        email='test@test.com',
        password='secret_terdr',
    )

    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'test@test.com'))
    assert result.id == 1
