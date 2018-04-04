from seaworthy.definitions import ContainerDefinition


container = ContainerDefinition(
    'gem-molo-unicore-redirect',
    'praekeltfoundation/gem-molo-unicore-redirect',
    create_kwargs={'ports': {'80/tcp': None}}
)

fixture = container.pytest_fixture('redirect_container')


def test_bare_domain_redirect(redirect_container):
    redirect = redirect_container.http_client().get(
        '/',
        allow_redirects=False,
        headers={'Host': 'gem.molo.unicore.io'},
    )
    assert redirect.status_code == 301
    assert redirect.headers['Location'] == 'http://id.heyspringster.com/'


def test_country_code_redirect(redirect_container):
    redirect = redirect_container.http_client().get(
        '/',
        allow_redirects=False,
        headers={'Host': 'za.gem.molo.unicore.io'},
    )
    assert redirect.status_code == 301
    assert redirect.headers['Location'] == 'http://za.heyspringster.com/'
