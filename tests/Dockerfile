FROM fedora:31

WORKDIR /usr/src/app

# NOTE: C.UTF-8 defs could be removed after support for Python <3.7 is dropped
ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

RUN dnf --setopt=install_weak_deps=False install -y \
    python3-tox \
    python36 \
    python38
