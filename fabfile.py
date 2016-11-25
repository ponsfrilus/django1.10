#!/usr/bin/env python
"""
    Author : Bancal Samuel

    Fabric3 file to deploy project.
    usage :
    $ pww
    $ fab -H test --password=${PASS} deploy
    $ fab -H prod --password=${PASS} full_deploy
"""


from fabric.utils import abort
from fabric.api import run, cd, env, task
from fabric.contrib.project import rsync_project
from fabric.operations import sudo

HOSTS = {
    "test": "sbancal@vas-y-test",
    "prod": "sbancal@vas-y",
}

try:
    env.hosts = [HOSTS[h] for h in env.hosts]
except KeyError:
    abort("""\
Unknown host.
Supported hosts are :
{allowed_hosts}
""".format(
            allowed_hosts="\n".join(["+ '%s' for %s" % (k, HOSTS[k]) for k in HOSTS])
        )
    )


def sub(s):
    if env.host == "vas-y-test":
        return s.format(
            code_dir="/django_app/shortme",
            server_config_dir="/django_app/shortme/server_config/vas-y-test",
            virtualenv_dir="/django_app/venv3",
            python="/django_app/venv3/bin/python",
            pip="/django_app/venv3/bin/pip",
        )
    elif env.host == "vas-y":
        return s.format(
            code_dir="/django_app/shortme",
            server_config_dir="/django_app/shortme/server_config/vas-y",
            virtualenv_dir="/django_app/venv3",
            python="/django_app/venv3/bin/python",
            pip="/django_app/venv3/bin/pip",
        )


# Related tools : Apache, Virtualenv

@task
def apache_setup():
    sudo(sub("cp {server_config_dir}/etc/apache2/sites-available/shortme_app.conf /etc/apache2/sites-available/shortme_app.conf"))
    sudo("a2ensite shortme_app")
    apache_reload()


@task
def mod_wsgi_express_setup():
    sudo(sub("{virtualenv_dir}/bin/mod_wsgi-express install-module"))
    sudo(sub("cp {server_config_dir}/etc/apache2/mods-available/wsgi_express.load /etc/apache2/mods-available/wsgi_express.load"))
    sudo(sub("cp {server_config_dir}/etc/apache2/mods-available/wsgi_express.conf /etc/apache2/mods-available/wsgi_express.conf"))
    sudo("a2enmod wsgi_express")


@task
def apache_reload():
    sudo("service apache2 reload")


@task
def apache_restart():
    sudo("service apache2 restart")


@task
def virtualenv_init():
    run(sub("mkdir -p {virtualenv_dir}"))
    # This will fail on active environments because Celery & Apache use the virtualenv
    run(sub("virtualenv -p python3 {virtualenv_dir}"))


@task
def virtualenv_setup():
    # requirements.txt is prepared this way :
    # pip freeze --local > shortme/requirements.txt
    run(sub("{pip} install --upgrade -r {code_dir}/requirements.txt"))


# Application related

@task
def rsync():
    rsync_project(
        local_dir="/home/sbancal/kata/django1.10/shortme/",
        remote_dir=sub("{code_dir}"),
        exclude=("*.sqlite3", "/static/*", "*.pyc", "__pycache__"),
        delete=True,
    )


@task
def rsync_n():
    rsync_project(
        local_dir="/home/sbancal/kata/django1.10/shortme/",
        remote_dir=sub("{code_dir}"),
        exclude=("*.sqlite3", "/static/*", "*.pyc", "__pycache__"),
        extra_opts="-n",
        delete=True,
    )


@task
def rm_pyc():
    run(sub(r"find {code_dir} -name '*.pyc' -exec rm -f \{{\}} \;"))


@task
def migrate():
    with cd(sub("{code_dir}")):
        run(sub("{python} manage.py migrate"))


@task
def collect_static():
    with cd(sub("{code_dir}")):
        run(sub("{python} manage.py collectstatic --noinput"))


@task
def clear_collect_static():
    with cd(sub("{code_dir}")):
        run(sub("{python} manage.py collectstatic --noinput -c"))


@task
def initadmins():
    with cd(sub("{code_dir}")):
        run(sub("{python} manage.py initadmins"))


# @task
# def compress():
#     with cd(sub("{code_dir}")):
#         run(sub("{python} manage.py compress"))


@task
def deploy():
    rsync()
    apache_reload()


@task
def full_deploy():
    rsync()
    rm_pyc()
    virtualenv_init()
    virtualenv_setup()
    migrate()
    clear_collect_static()
    initadmins()
    mod_wsgi_express_setup()
    apache_setup()
    apache_restart()
