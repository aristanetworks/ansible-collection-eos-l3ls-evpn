ARG FROM_IMAGE
ARG FROM_VARIANT

FROM ${FROM_IMAGE}:${FROM_VARIANT}

# RFC3339 time to set label
ARG RFC3339_TIMESTAMP
# Image version will be set by the build workflow
ARG IMAGE_VERSION
# set labels
LABEL org.opencontainers.image.description="AVD dev image. This image can only be used for AVD development and not to support production deployments."
LABEL com.arista.license_terms="https://github.com/aristanetworks/avd/blob/devel/LICENSE"
LABEL org.opencontainers.image.licenses="Apache-2.0"
LABEL org.opencontainers.image.authors="Arista AVD Team <ansible@arista.com>"
LABEL org.opencontainers.image.url="https://github.com/orgs/aristanetworks/packages?repo_name=avd"
LABEL org.opencontainers.image.documentation="https://avd.arista.com/"
LABEL org.opencontainers.image.source="https://github.com/aristanetworks/avd/tree/devel/containers"
LABEL org.opencontainers.image.created=${RFC3339_TIMESTAMP}
LABEL org.opencontainers.image.version=${IMAGE_VERSION}
LABEL org.opencontainers.image.vendor="Arista Networks"

ARG USERNAME

# Add entrypoint script.
COPY ./entrypoint.sh /bin/entrypoint.sh
RUN chmod +x /bin/entrypoint.sh
# Use ENTRYPOINT instead of CMD to ensure that entryscript is always executed.
ENTRYPOINT [ "/bin/entrypoint.sh" ]

# Switch user to given USERNAME otherwise Ansible will be installed as root.
USER ${USERNAME}
ENV PATH=$PATH:/home/${USERNAME}/.local/bin
# make sure that path required to mount Ansible collection exists
RUN mkdir -p /home/${USERNAME}/.ansible/collections/ansible_collections/arista/avd
