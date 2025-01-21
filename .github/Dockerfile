FROM ghcr.io/maheshgslab/avd-slim-test5:0.1
COPY ansible_collections/arista/avd/requirements-dev.txt /requirements-dev.txt
RUN uv python install 3.10 3.11 3.12 3.13 && \
    /UV3.10/bin/python -m pip install mock pytest pytest-mock pytest-xdist pyyaml "ansible-core<2.19.0" -r /requirements-dev.txt --upgrade && \
    /UV3.11/bin/python -m pip install mock pytest pytest-mock pytest-xdist pyyaml "ansible-core<2.19.0" -r /requirements-dev.txt --upgrade && \
    /UV3.12/bin/python -m pip install mock pytest pytest-mock pytest-xdist pyyaml "ansible-core<2.19.0" -r /requirements-dev.txt --upgrade && \
    /UV3.13/bin/python -m pip install mock pytest pytest-mock pytest-xdist pyyaml "ansible-core<2.19.0" -r /requirements-dev.txt --upgrade
