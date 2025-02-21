ARG FROM_IMAGE
ARG FROM_VARIANT
FROM ${FROM_IMAGE}:${FROM_VARIANT}

# RFC3339 time to set label
ARG RFC3339_TIMESTAMP
# Image version will be set by the build workflow
ARG IMAGE_VERSION
# set labels
LABEL org.opencontainers.image.description="AVD base image. This image MUST NOT be used directly and only required to optimize build process for other images."
LABEL com.arista.license_terms="https://github.com/aristanetworks/avd/blob/devel/LICENSE"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.authors="Arista AVD Team <ansible@arista.com>"
LABEL org.opencontainers.image.url="https://github.com/orgs/aristanetworks/packages?repo_name=avd"
LABEL org.opencontainers.image.documentation="https://avd.arista.com/"
LABEL org.opencontainers.image.source="https://github.com/aristanetworks/avd/tree/devel/containers"
LABEL org.opencontainers.image.created=${RFC3339_TIMESTAMP}
LABEL org.opencontainers.image.version=${IMAGE_VERSION}
LABEL org.opencontainers.image.vendor="Arista Networks"

# Install essential tools.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    make \
    git \
    # xz-utils required for docker import to work
    xz-utils \
    && rm -rf /var/lib/apt/lists/* \
    && rm -Rf /usr/share/doc && rm -Rf /usr/share/man \
    && apt-get clean

# set ANSIBLE_CONFIG to ansible.cfg in local directory
# this is required to address Ansible ignoring config in a world writable directory
# on Codespaces, Gitlab Runner, etc.
ENV ANSIBLE_CONFIG="ansible.cfg"

# Add entrypoint script.
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
# Use ENTRYPOINT instead of CMD to ensure that entryscript is always executed.
ENTRYPOINT [ "/bin/entrypoint.sh" ]
