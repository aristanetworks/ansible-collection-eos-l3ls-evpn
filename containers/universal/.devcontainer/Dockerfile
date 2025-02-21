ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

# RFC3339 time to set label
ARG RFC3339_TIMESTAMP
# Image version will be set by the build workflow
ARG IMAGE_VERSION
# set labels
LABEL org.opencontainers.image.description="AVD universal image with pre-installed AVD collection. The image is still in preview and under active development."
LABEL com.arista.license_terms="https://github.com/aristanetworks/avd/blob/devel/LICENSE"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.authors="Arista AVD Team <ansible@arista.com>"
LABEL org.opencontainers.image.url="https://github.com/orgs/aristanetworks/packages?repo_name=avd"
LABEL org.opencontainers.image.documentation="https://avd.arista.com/"
LABEL org.opencontainers.image.source="https://github.com/aristanetworks/avd/tree/devel/containers"
LABEL org.opencontainers.image.created=${RFC3339_TIMESTAMP}
LABEL org.opencontainers.image.version=${IMAGE_VERSION}
LABEL org.opencontainers.image.vendor="Arista Networks"

ARG PYAVD_INSTALL_LOCATION
ARG ANSIBLE_INSTALL_LOCATION
ARG USERNAME

# Switch user to given USERNAME otherwise Ansible will be installed as root.
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
# Install Ansible AVD collection.
RUN pip install "pyavd[ansible] @ ${PYAVD_INSTALL_LOCATION}" \
    && ansible-galaxy collection install ${ANSIBLE_INSTALL_LOCATION} \
    # install community.general to support callback plugins in ansible.cfg, etc.
    && ansible-galaxy collection install community.general
